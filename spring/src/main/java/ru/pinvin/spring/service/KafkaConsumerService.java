package ru.pinvin.spring.service;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumerService {

    @KafkaListener(topics = "myTopic", groupId = "myGroup")
    public void consume(String message) {
        System.out.println("Consumed message: " + message);
        // Обработка сообщения
    }
}