class KafkaConfig:
    KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"
    AUDIO_TOPIC = "audio_calls"
    PROCESSED_TOPIC = "processed_calls"
    GROUP_ID = "client-readiness-group"


kafka_config = KafkaConfig()