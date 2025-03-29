import json
from services.audio_processor import AudioProcessor
from services.nlp_analyzer import NLPAnalyzer
from models.readiness_model import ReadinessModel
from services.kafka_service import KafkaService


def main():
    # Инициализация сервисов
    audio_processor = AudioProcessor()
    nlp_analyzer = NLPAnalyzer()
    readiness_model = ReadinessModel()
    kafka_service = KafkaService()
    print(kafka_service)

    print("Сервис оценки готовности клиента запущен...")

    for audio_message in kafka_service.consume_audio_messages():
        try:
            # Десериализация сообщения
            message_data = json.loads(audio_message)
            call_id = message_data.get('call_id')
            audio_bytes = message_data.get('audio_data').encode('latin-1')

            # Преобразование аудио в текст
            text = audio_processor.audio_to_text(audio_bytes)
            if not text:
                continue

            # NLP анализ текста
            metrics = nlp_analyzer.analyze_text(text)

            # Оценка готовности клиента
            assessment = readiness_model.assess_readiness(metrics)

            # Формирование результата
            result = {
                "call_id": call_id,
                "text": text,
                "assessment": assessment,
                "recommendation": generate_recommendation(assessment['category'])
            }

            # Отправка результата в Kafka
            kafka_service.produce_processed_message(result)

            print(f"Обработан звонок {call_id}. Категория: {assessment['category']}")

        except Exception as e:
            print(f"Ошибка при обработке сообщения: {e}")


def generate_recommendation(category: str) -> str:
    """
    Генерирует рекомендации на основе категории клиента
    """
    recommendations = {
        "hot": "Немедленно предложить оформить заказ, предоставить скидку или бонус",
        "warm": "Отправить дополнительную информацию, запланировать повторный звонок через 2 дня",
        "cold": "Добавить в долгосрочную кампанию удержания, отправить обучающие материалы"
    }
    return recommendations.get(category, "Неизвестная категория")

def test():
    # Пример использования
    audio_processor = AudioProcessor()
    audio_path = "C:/Users/dzhager3354/Desktop/q.mp3"  # Укажите путь к вашему аудиофайлу
    text = audio_processor.audio_to_text(audio_path)
    print("Распознанный текст:", text)

    # Далее вы можете использовать NLPAnalyzer для анализа текста
    nlp_analyzer = NLPAnalyzer()
    metrics = nlp_analyzer.analyze_text(text)
    print("Метрики анализа:", metrics)


if __name__ == "__main__":
    test()