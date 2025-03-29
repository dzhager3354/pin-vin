from typing import Dict, List, Tuple
import re
import spacy
from spacy.tokens import Doc
from collections import defaultdict
from config.npl_config import NLPConfig


class NLPAnalyzer:
    def __init__(self):
        self.config = NLPConfig()
        try:
            self.nlp = spacy.load(self.config.MODEL_NAME)
            # Убираем ненужные pipeline компоненты для русского
            if "merge_noun_chunks" in self.nlp.pipe_names:
                self.nlp.remove_pipe("merge_noun_chunks")
            if "merge_entities" in self.nlp.pipe_names:
                self.nlp.remove_pipe("merge_entities")
        except OSError:
            raise ImportError(
                f"Russian language model not found. Please install it with: python -m spacy download {self.config.MODEL_NAME}")

    def analyze_text(self, text: str) -> Dict:
        """Анализирует текст и возвращает расширенные метрики"""
        if not text or len(text.strip()) < self.config.MIN_TEXT_LENGTH:
            return self._empty_response()

        doc = self.nlp(text)

        # Основные метрики
        metrics = {
            "category": "cold",
            "probability": 0,
            "transcript": text,
            "keywords": [],
            "sentiment": "neutral",
            "recommendations": "Перезвонить не скоро"
        }

        # Анализ ключевых фраз с весами
        hot_score = self._calculate_phrase_score(text, self.config.HOT_KEYWORDS, self.config.HOT_PHRASES)
        warm_score = self._calculate_phrase_score(text, self.config.WARM_KEYWORDS, self.config.WARM_PHRASES)
        negative_score = self._calculate_phrase_score(text, self.config.NEGATIVE_KEYWORDS, self.config.NEGATIVE_PHRASES)

        # Анализ тональности
        sentiment_score, sentiment_words = self._contextual_sentiment_analysis(doc)

        # Анализ вопросов и намерений
        questions = self._count_questions(text)
        intentions = self._detect_intentions(text)

        # Определение категории
        metrics.update(self._determine_category(
            hot_score,
            warm_score,
            negative_score,
            sentiment_score,
            questions,
            intentions,
            text  # Передаем текст для извлечения ключевых слов
        ))

        return metrics

    def _calculate_phrase_score(self, text: str, keywords: Dict[str, float], phrases: Dict[str, float]) -> float:
        """Вычисляет общий балл для категории на основе ключевых слов и фраз"""
        text_lower = text.lower()
        total_score = 0.0

        # Проверяем отдельные слова
        for word, weight in keywords.items():
            if re.search(rf'\b{re.escape(word)}\b', text_lower):
                total_score += weight

        # Проверяем фразы
        for phrase, weight in phrases.items():
            if re.search(rf'\b{re.escape(phrase)}\b', text_lower):
                total_score += weight * 1.5  # Фразы имеют больший вес

        return total_score

    def _contextual_sentiment_analysis(self, doc: Doc) -> Tuple[float, List[Tuple[str, str]]]:
        """Анализ тональности с учетом контекста и весов"""
        sentiment_words = []
        pos_score = 0
        neg_score = 0
        text_lower = doc.text.lower()

        # Проверяем позитивные фразы
        for phrase, weight in self.config.POSITIVE_PHRASES.items():
            if phrase in text_lower:
                pos_score += weight
                sentiment_words.append((phrase, "positive"))

        # Проверяем негативные фразы
        for phrase, weight in self.config.NEGATIVE_PHRASES.items():
            if phrase in text_lower:
                neg_score += weight
                sentiment_words.append((phrase, "negative"))

        # Проверяем отдельные слова с контекстом
        for token in doc:
            lower_text = token.text.lower()
            if lower_text in self.config.POSITIVE_WORDS:
                # Проверяем отрицание перед словом
                if token.i > 0 and doc[token.i - 1].text.lower() in ["не", "нет"]:
                    neg_score += self.config.POSITIVE_WORDS[lower_text] * 0.8
                    sentiment_words.append((f"{doc[token.i - 1].text} {token.text}", "negative"))
                else:
                    pos_score += self.config.POSITIVE_WORDS[lower_text]
                    sentiment_words.append((token.text, "positive"))
            elif lower_text in self.config.NEGATIVE_KEYWORDS:
                neg_score += self.config.NEGATIVE_KEYWORDS[lower_text]
                sentiment_words.append((token.text, "negative"))

        total_score = 0.5  # нейтральный по умолчанию
        if pos_score + neg_score > 0:
            total_score = pos_score / (pos_score + neg_score)

        return total_score, sentiment_words

    def _count_questions(self, text: str) -> int:
        """Подсчет вопросов с учетом вопросительных фраз"""
        question_count = 0
        text_lower = text.lower()

        # Проверяем вопросительные знаки
        if '?' in text_lower:
            question_count += 1

        # Проверяем вопросительные слова
        for q_word in self.config.QUESTION_WORDS:
            if q_word in text_lower:
                question_count += 1
                break

        return question_count

    def _detect_intentions(self, text: str) -> List[str]:
        """Определение намерений по ключевым фразам"""
        intentions = []
        text_lower = text.lower()

        return intentions

    def _determine_category(self, hot_score, warm_score, negative_score,
                            sentiment, questions, intentions, text: str):
        """Определяет категорию клиента на основе всех метрик"""
        probability = 0

        # Положительные факторы
        probability += hot_score * 1.5  # Горячие слова имеют больший вес
        probability += warm_score * 0.8
        if "payment_request" in intentions:
            probability += 30
        if sentiment > 0.7:
            probability += 20
        elif sentiment < 0.3:
            probability -= 15

        # Отрицательные факторы
        probability -= negative_score * 2.0  # Негативные слова имеют больший вес

        probability = max(0, min(100, probability))

        # Определение категории по порогам из конфига
        if probability >= self.config.CLIENT_TYPE_THRESHOLDS["hot"]:
            category = "hot"
            recommendations = "Клиент готов к покупке, нужно срочно связаться"
        elif probability >= self.config.CLIENT_TYPE_THRESHOLDS["warm"]:
            category = "warm"
            recommendations = "Клиент проявляет интерес, перезвонить в ближайшее время"
        elif probability >= self.config.CLIENT_TYPE_THRESHOLDS["cold"]:
            category = "cold"
            recommendations = "Клиент не проявил явного интереса, перезвонить через неделю"
        else:
            category = "negative"
            recommendations = "Клиент негативно настроен, перезвонить через месяц или исключить из списка"

        return {
            "category": category,
            "probability": probability,
            "recommendations": recommendations,
            "keywords": self._extract_top_keywords(text)
        }

    def _extract_top_keywords(self, text: str) -> List[str]:
        """Извлекает топ-5 самых значимых ключевых слов"""
        text_lower = text.lower()
        keywords = []

        # Собираем все возможные ключевые слова и фразы
        all_keywords = {**self.config.HOT_KEYWORDS, **self.config.WARM_KEYWORDS,
                        **self.config.NEGATIVE_KEYWORDS, **self.config.HOT_PHRASES,
                        **self.config.WARM_PHRASES, **self.config.NEGATIVE_PHRASES}

        # Фильтруем только те, что есть в тексте
        found_keywords = {k: v for k, v in all_keywords.items()
                          if re.search(rf'\b{re.escape(k)}\b', text_lower)}

        # Сортируем по весу и берем топ-5
        top_keywords = sorted(found_keywords.items(), key=lambda x: x[1], reverse=True)[:5]
        return [kw[0] for kw in top_keywords]

    def _empty_response(self):
        """Возвращает пустой ответ при отсутствии текста"""
        return {
            "category": "undefined",
            "probability": 0,
            "transcript": "",
            "keywords": [],
            "sentiment": "neutral",
            "recommendations": "Текст не распознан"
        }