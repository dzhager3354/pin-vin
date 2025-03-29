import spacy
from spacy.tokens import Doc
from typing import Dict, Tuple
from config.settings import settings


class NLPAnalyzer:
    def init(self):
        self.nlp = spacy.load(settings.NLP_MODEL)

    def analyze_text(self, text: str) -> Dict:
        """
        Анализирует текст и возвращает метрики
        """
        doc = self.nlp(text)

        # Анализ ключевых слов
        hot_keywords = self._count_keywords(doc, settings.HOT_KEYWORDS)
        warm_keywords = self._count_keywords(doc, settings.WARM_KEYWORDS)

        # Анализ тональности (упрощенный)
        sentiment = self._simple_sentiment_analysis(doc)

        # Анализ вопросов
        questions = self._count_questions(doc)

        return {
            "hot_keywords": hot_keywords,
            "warm_keywords": warm_keywords,
            "sentiment": sentiment,
            "questions": questions,
            "text_length": len(doc)
        }

    def _count_keywords(self, doc: Doc, keywords: list) -> int:
        """Подсчет ключевых слов"""
        return sum(1 for token in doc if token.text.lower() in keywords)

    def _simple_sentiment_analysis(self, doc: Doc) -> float:
        """Упрощенный анализ тональности"""
        positive_words = ["хорошо", "отлично", "интересно", "нравится"]
        negative_words = ["плохо", "дорого", "не нравится", "сомневаюсь"]

        pos = sum(1 for token in doc if token.text.lower() in positive_words)
        neg = sum(1 for token in doc if token.text.lower() in negative_words)

        if pos + neg == 0:
            return 0.5  # нейтральный

        return pos / (pos + neg)

    def _count_questions(self, doc: Doc) -> int:
        """Подсчет вопросов"""
        return sum(1 for sent in doc.sents if sent.text.endswith('?'))