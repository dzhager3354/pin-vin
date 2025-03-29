from config.settings import settings


class ReadinessModel:
    def assess_readiness(self, metrics: dict) -> dict:
        """
        Оценивает готовность клиента на основе метрик NLP
        Возвращает оценку и категорию
        """
        # Весовые коэффициенты для каждого параметра
        weights = {
            'hot_keywords': 0.4,
            'warm_keywords': 0.3,
            'sentiment': 0.2,
            'questions': 0.1
        }

        # Нормализация значений
        hot_score = min(metrics['hot_keywords'] / 5, 1.0)  # макс. 5 ключевых слов
        warm_score = min(metrics['warm_keywords'] / 3, 1.0)  # макс. 3 ключевых слова
        sentiment_score = metrics['sentiment']
        questions_score = min(metrics['questions'] / 3, 1.0)  # макс. 3 вопроса

        # Расчет общей оценки
        total_score = (
                hot_score * weights['hot_keywords'] +
                warm_score * weights['warm_keywords'] +
                sentiment_score * weights['sentiment'] +
                questions_score * weights['questions']
        )

        # Определение категории
        if total_score >= settings.HOT_THRESHOLD:
            category = "hot"
        elif total_score >= settings.WARM_THRESHOLD:
            category = "warm"
        else:
            category = "cold"

        return {
            "score": round(total_score, 2),
            "category": category,
            "metrics": metrics
        }