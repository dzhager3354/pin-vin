from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class NLPConfig:
    HOT_KEYWORDS: List[str] = field(default_factory=lambda: ["купить", "заказ", "цена", "доставка", "срочно", "оформить"])
    WARM_KEYWORDS: List[str] = field(default_factory=lambda: ["интересно", "подробнее", "характеристики", "отзывы"])
    NEGATIVE_KEYWORDS: List[str] = field(default_factory=lambda: ["нет", "не надо", "идите", "не интересует", "отстаньте"])
    MODEL_NAME: str = "ru_core_news_md"
    POSITIVE_WORDS: Dict[str, float] = field(default_factory=lambda: {
        "хорошо": 1, "отлично": 1.5, "интересно": 1, "нравится": 1.5,
        "прекрасно": 2, "замечательно": 2, "супер": 1.5
    })
    NEGATIVE_WORDS: Dict[str, float] = field(default_factory=lambda: {
        "плохо": 1, "дорого": 0.8, "не нравится": 1.5, "сомневаюсь": 0.7,
        "ужасно": 2, "отвратительно": 2, "кошмар": 2, "разочарован": 1.5
    })