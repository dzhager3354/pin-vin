from dataclasses import dataclass, field
from typing import Dict, List
from dataclasses import dataclass, field


@dataclass
class NLPConfig:
    # Hot lead indicators
    HOT_KEYWORDS: Dict[str, float] = field(default_factory=lambda: {
        "срочно": 1.5, "горячий": 1.8, "быстро": 1.2, "немедленно": 1.7,
        "сегодня": 1.3, "сейчас": 1.4, "купить": 2.0, "заказать": 1.9,
        "оформить": 1.8, "договор": 1.6, "оплата": 1.7, "сделка": 1.9,
        "готов": 1.8, "решил": 1.7, "выбрал": 1.6, "нужно": 1.5
    })

    HOT_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "хочу купить": 2.2,
        "готов к покупке": 2.3,
        "можно оформить": 2.1,
        "срочно нужен": 2.4,
        "заключить договор": 2.0,
        "сделать заказ": 2.1,
        "прошу оформить": 2.0,
        "готов оплатить": 2.2
    })

    # Warm lead indicators
    WARM_KEYWORDS: Dict[str, float] = field(default_factory=lambda: {
        "интерес": 1.2, "подробнее": 1.1, "узнать": 1.0, "рассказать": 1.0,
        "варианты": 1.1, "выбор": 1.1, "сравнить": 1.2, "характеристики": 1.1,
        "обсудить": 1.2, "встреча": 1.3, "консультация": 1.3, "звонок": 1.1,
        "менеджер": 1.1, "условия": 1.2, "сотрудничество": 1.3, "партнерство": 1.3
    })

    WARM_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "хочу узнать": 1.5,
        "интересует информация": 1.4,
        "можно подробнее": 1.5,
        "какие варианты": 1.6,
        "хочу обсудить": 1.7,
        "нужна консультация": 1.8,
        "возможности сотрудничества": 1.7,
        "какие условия": 1.6
    })

    # Negative indicators
    NEGATIVE_KEYWORDS: Dict[str, float] = field(default_factory=lambda: {
        "дорого": 1.5, "неудобно": 1.3, "сложно": 1.2, "непонятно": 1.3,
        "подожду": 1.4, "позже": 1.2, "подумаю": 1.1, "не уверен": 1.5,
        "сомнения": 1.4, "отказ": 1.8, "не интересно": 1.7, "не нужно": 1.6,
        "не буду": 1.7, "не хочу": 1.6, "не подходит": 1.5, "не устраивает": 1.6
    })

    NEGATIVE_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "не подходит": 1.8,
        "не устраивает": 1.9,
        "слишком дорого": 2.0,
        "не буду покупать": 2.1,
        "отказываюсь": 2.2,
        "не интересно": 1.9,
        "не хочу": 1.8,
        "не нужно": 1.7
    })

    # Sentiment analysis
    POSITIVE_WORDS: Dict[str, float] = field(default_factory=lambda: {
        "хорошо": 1.0, "отлично": 1.5, "прекрасно": 1.6, "удобно": 1.2,
        "понятно": 1.1, "нравится": 1.4, "интересно": 1.2, "рад": 1.3,
        "доволен": 1.5, "супер": 1.4, "класс": 1.3, "рекомендую": 1.7,
        "спасибо": 1.2, "благодарю": 1.3, "удовлетворен": 1.6, "идеально": 1.7
    })

    POSITIVE_PHRASES: Dict[str, float] = field(default_factory=lambda: {
        "очень хорошо": 1.8,
        "все отлично": 1.9,
        "полностью доволен": 2.0,
        "отличный сервис": 2.1,
        "все нравится": 1.9,
        "очень удобно": 1.8,
        "все понятно": 1.7,
        "спасибо за помощь": 1.8
    })

    # Намерения
    QUESTION_WORDS: Dict[str, float] = field(default_factory=lambda: {
        "как": 0.7, "почему": 0.8, "когда": 0.7, "где": 0.6, "можно ли": 0.9,
        "вы можете": 0.8, "сколько стоит": 1.0, "какие условия": 0.9
    })

    # Other configs
    MODEL_NAME: str = "ru_core_news_md"
    MIN_TEXT_LENGTH: int = 10
    CLIENT_TYPE_THRESHOLDS: Dict[str, float] = field(default_factory=lambda: {
        "hot": 70,
        "warm": 40,
        "cold": 10
    })