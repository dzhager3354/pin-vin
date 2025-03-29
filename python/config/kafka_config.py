class KafkaConfig:
    KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
    AUDIO_TOPIC = "myTopic"
    PROCESSED_TOPIC = "topicPython"
    GROUP_ID = "myTopic"


kafka_config = KafkaConfig()