from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Settings:
    # Настройки аудио обработки
    AUDIO_SAMPLE_RATE: int = 16000
    AUDIO_CHANNELS: int = 1
    AUDIO_FORMAT: str = "wav"

    # Настройки NLP
    NLP_MODEL: str = "ru_core_news_md"

    # Ключевые слова с весами
    HOT_KEYWORDS: Dict[str, float] = field(default_factory=lambda: {
        "купить": 1.5, "заказ": 1.3, "цена": 1.2, "доставка": 1.1,
        "срочно": 1.7, "оформить": 1.4, "оплатить": 1.6
    })

    WARM_KEYWORDS: Dict[str, float] = field(default_factory=lambda: {
        "интересно": 1.0, "подробнее": 0.9, "характеристики": 0.8,
        "отзывы": 0.8, "узнать": 0.9, "консультация": 0.7
    })

    NEGATIVE_KEYWORDS: Dict[str, float] = field(default_factory=lambda: {
        "нет": 1.5, "не надо": 1.7, "идите": 2.0, "не интересует": 1.8,
        "отстаньте": 2.0, "не звоните": 1.9, "хватит": 1.6
    })

    # Фразы с весами
    HOT_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "готов к покупке": 2.0, "хочу купить": 1.8, "могу оплатить": 1.7,
        "вышлите счет": 1.6, "заключим договор": 1.9, "начнем работать": 1.5,
        "готовы сотрудничать": 1.4, "срочно нужно": 2.1, "давайте оформлять": 1.8
    })

    WARM_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "хочу узнать подробнее": 1.2, "интересует информация": 1.1,
        "можно попробовать": 1.0, "давайте обсудим": 0.9, "есть вопросы": 0.8,
        "хочу проконсультироваться": 0.9, "как это работает": 0.8,
        "какие условия": 0.9, "можно тестовый доступ": 1.0
    })

    NEGATIVE_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "не интересно": 1.8, "не актуально": 1.6, "не подходит": 1.7,
        "не буду": 1.5, "не хочу": 1.6, "не нужно": 1.7, "не сейчас": 1.4,
        "не наш вариант": 1.8, "отстаньте пожалуйста": 2.0,
        "не звоните больше": 2.0, "нам не подходит": 1.9
    })

    # Тональность
    POSITIVE_WORDS: Dict[str, float] = field(default_factory=lambda: {
        "хорошо": 1.0, "отлично": 1.5, "прекрасно": 2.0, "замечательно": 2.0,
        "супер": 1.5, "великолепно": 2.0, "восхитительно": 2.2, "понравилось": 1.5,
        "нравится": 1.5, "рекомендую": 1.7, "удобно": 1.2, "комфортно": 1.3
    })

    NEGATIVE_WORDS: Dict[str, float] = field(default_factory=lambda: {
        "плохо": 1.0, "ужасно": 2.0, "отвратительно": 2.2, "кошмар": 2.0,
        "разочарован": 1.8, "недоволен": 1.7, "неудобно": 1.3, "дорого": 1.5,
        "мусор": 2.0, "развод": 2.2, "обман": 2.3, "надувательство": 2.1
    })

    # Намерения
    QUESTION_WORDS: Dict[str, float] = field(default_factory=lambda: {
        "как": 0.7, "почему": 0.8, "когда": 0.7, "где": 0.6, "можно ли": 0.9,
        "вы можете": 0.8, "сколько стоит": 1.0, "какие условия": 0.9
    })

    PAYMENT_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "оплатить заказ": 1.5, "выставить счет": 1.3, "как оплатить": 1.2,
        "стоимость услуги": 1.4, "цена вопроса": 1.1, "условия оплаты": 1.3,
        "безналичный расчет": 1.2, "оплата картой": 1.1
    })

    TECH_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "техническая поддержка": 1.3, "не могу войти": 1.5, "проблемы с доступом": 1.4,
        "забыл пароль": 1.2, "как пользоваться": 1.1, "инструкция по применению": 1.0,
        "не работает система": 1.6, "нужна помощь": 1.3
    })

    # Пороговые значения
    HOT_THRESHOLD: float = 0.7
    WARM_THRESHOLD: float = 0.4
    MIN_TEXT_LENGTH: int = 10  # Минимальная длина текста для анализа

settings = Settings()