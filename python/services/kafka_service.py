from confluent_kafka import Consumer, Producer
import json
from config.kafka_config import kafka_config


class KafkaService:
    def __init__(self):
        # Инициализация consumer с правильными настройками
        self.consumer = Consumer({
            'bootstrap.servers': kafka_config.KAFKA_BOOTSTRAP_SERVERS,
            'group.id': kafka_config.GROUP_ID,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False  # Рекомендуется отключить авто-коммит для большего контроля
        })

        # Инициализация producer
        self.producer = Producer({
            'bootstrap.servers': kafka_config.KAFKA_BOOTSTRAP_SERVERS,
            'message.timeout.ms': 5000  # Таймаут отправки сообщения
        })

        # Подписка на топик
        self.consumer.subscribe([kafka_config.AUDIO_TOPIC])

    def consume_audio_messages(self):
        """
        Получает аудио сообщения из Kafka
        """
        try:
            while True:
                msg = self.consumer.poll(1.0)  # Таймаут 1 секунда

                if msg is None:
                    continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                    continue

                yield msg.value()
        except KeyboardInterrupt:
            print("Остановка consumer...")
        finally:
            self.consumer.close()

    def produce_processed_message(self, result: dict):
        """
        Отправляет обработанные данные в Kafka
        """
        try:
            self.producer.produce(
                topic=kafka_config.PROCESSED_TOPIC,
                value=json.dumps(result).encode('utf-8'),
                callback=self._delivery_report  # Добавляем callback для обработки статуса доставки
            )
            self.producer.flush()  # Ожидаем отправки всех сообщений
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")

    @staticmethod
    def _delivery_report(err, msg):
        """Callback для обработки статуса доставки сообщения"""
        if err is not None:
            print(f'Сообщение не доставлено: {err}')
        else:
            print(f'Сообщение доставлено в {msg.topic()} [{msg.partition()}]')