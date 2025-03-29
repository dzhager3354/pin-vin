from typing import Dict, List, Tuple
import spacy
from spacy.tokens import Doc
from collections import defaultdict
from config.settings import settings


class NLPAnalyzer:
    def __init__(self):
        try:
            self.nlp = spacy.load("ru_core_news_md")
        except OSError:
            raise ImportError(
                "Russian language model not found. Please install it with: python -m spacy download ru_core_news_md")

    def analyze_text(self, text: str) -> Dict:
        """Анализирует текст и возвращает расширенные метрики"""
        if not text or not text.strip():
            return self._empty_response()

        doc = self.nlp(text)

        # Основные метрики
        metrics = {
            "category": "cold",
            "probability": 0,
            "transcript": text,
            "keywords": [],
            "sentiment": "neutral",
            "recommendations": "Перезвонить не скоро",
            "details": {}
        }

        # Анализ ключевых слов
        hot_keywords = self._extract_keywords(doc, settings.HOT_KEYWORDS)
        warm_keywords = self._extract_keywords(doc, settings.WARM_KEYWORDS)
        negative_keywords = self._extract_keywords(doc, ["нет", "не надо", "идите", "не интересует", "отстаньте"])

        # Анализ тональности
        sentiment_score, sentiment_words = self._advanced_sentiment_analysis(doc)

        # Анализ вопросов и намерений
        questions = self._count_questions(doc)
        intentions = self._detect_intentions(doc)

        # Определение категории
        metrics.update(self._determine_category(
            hot_keywords,
            warm_keywords,
            negative_keywords,
            sentiment_score,
            questions,
            intentions
        ))

        # Формирование детализированного отчета
        metrics["details"] = {
            "hot_keywords": hot_keywords,
            "warm_keywords": warm_keywords,
            "negative_keywords": negative_keywords,
            "sentiment_score": sentiment_score,
            "sentiment_words": sentiment_words,
            "questions_count": questions,
            "intentions": intentions
        }

        return metrics

    def _empty_response(self):
        """Возвращает пустой ответ при отсутствии текста"""
        return {
            "category": "undefined",
            "probability": 0,
            "transcript": "",
            "keywords": [],
            "sentiment": "neutral",
            "recommendations": "Текст не распознан",
            "details": {}
        }

    def _extract_keywords(self, doc: Doc, keywords: List[str]) -> List[Tuple[str, int]]:
        """Извлекает ключевые слова с частотой их появления"""
        keyword_counts = defaultdict(int)
        for token in doc:
            lower_text = token.text.lower()
            if lower_text in keywords:
                keyword_counts[lower_text] += 1
        return sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

    def _advanced_sentiment_analysis(self, doc: Doc) -> Tuple[float, List[Tuple[str, str]]]:
        """Расширенный анализ тональности с определением эмоциональных слов"""
        positive_words = {
            "хорошо": 1, "отлично": 1.5, "интересно": 1, "нравится": 1.5,
            "прекрасно": 2, "замечательно": 2, "супер": 1.5, "отлично": 1.5
        }
        negative_words = {
            "плохо": 1, "дорого": 0.8, "не нравится": 1.5, "сомневаюсь": 0.7,
            "ужасно": 2, "отвратительно": 2, "кошмар": 2, "разочарован": 1.5
        }

        sentiment_words = []
        pos_score = 0
        neg_score = 0

        for token in doc:
            lower_text = token.text.lower()
            if lower_text in positive_words:
                pos_score += positive_words[lower_text]
                sentiment_words.append((token.text, "positive"))
            elif lower_text in negative_words:
                neg_score += negative_words[lower_text]
                sentiment_words.append((token.text, "negative"))

        total_score = 0.5  # нейтральный по умолчанию
        if pos_score + neg_score > 0:
            total_score = pos_score / (pos_score + neg_score)

        return total_score, sentiment_words

    def _count_questions(self, doc: Doc) -> int:
        """Подсчет вопросов с учетом русской грамматики"""
        question_count = 0
        for sent in doc.sents:
            # Проверяем вопросительный знак в конце предложения
            if sent.text.endswith('?'):
                question_count += 1
            # Проверяем вопросительные слова в начале предложения
            elif any(token.text.lower() in ["как", "почему", "когда", "где"]
                     for token in sent[:3]):  # проверяем только первые 3 токена
                question_count += 1
        return question_count

    def _detect_intentions(self, doc: Doc) -> List[str]:
        """Определение намерений клиента"""
        intentions = []
        for sent in doc.sents:
            text = sent.text.lower()
            if any(phrase in text for phrase in ["хочу купить", "готов заказать", "оформить заказ"]):
                intentions.append("purchase_intent")
            elif any(phrase in text for phrase in ["узнать подробнее", "расскажите", "информация"]):
                intentions.append("information_request")
            elif any(phrase in text for phrase in ["жалоба", "претензия", "недоволен"]):
                intentions.append("complaint")
        return intentions

    def _determine_category(self, hot_kw, warm_kw, negative_kw, sentiment, questions, intentions):
        """Определяет категорию клиента на основе всех метрик"""
        probability = 0

        # Положительные факторы
        if hot_kw:
            probability += len(hot_kw) * 15
        if warm_kw:
            probability += len(warm_kw) * 8
        if "purchase_intent" in intentions:
            probability += 30
        if sentiment > 0.7:
            probability += 20
        elif sentiment < 0.3:
            probability -= 15

        # Отрицательные факторы
        if negative_kw:
            probability -= len(negative_kw) * 20
        if "complaint" in intentions:
            probability -= 25

        probability = max(0, min(100, probability))

        # Определение категории
        if probability >= 70:
            category = "hot"
            recommendations = "Клиент готов к покупке, нужно срочно связаться"
        elif probability >= 40:
            category = "warm"
            recommendations = "Клиент проявляет интерес, перезвонить в ближайшее время"
        elif probability >= 15:
            category = "cold"
            recommendations = "Клиент не проявил явного интереса, перезвонить через неделю"
        else:
            category = "negative"
            recommendations = "Клиент негативно настроен, перезвонить через месяц или исключить из списка"

        return {
            "category": category,
            "probability": probability,
            "recommendations": recommendations,
            "keywords": [kw[0] for kw in hot_kw + warm_kw + negative_kw]
        }