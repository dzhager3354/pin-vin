import os


class Settings:
    # Настройки аудио обработки
    AUDIO_SAMPLE_RATE = 16000
    AUDIO_CHANNELS = 1
    AUDIO_FORMAT = "wav"

    # Настройки NLP
    NLP_MODEL = "en_core_web_md"  # или "ru_core_news_md" для русского

    # Критерии оценки
    HOT_KEYWORDS = ["купить", "заказ", "цена", "доставка", "срочно", "оформить"]
    WARM_KEYWORDS = ["интересно", "подробнее", "характеристики", "отзывы"]

    # Пороговые значения
    HOT_THRESHOLD = 0.7
    WARM_THRESHOLD = 0.4


settings = Settings()