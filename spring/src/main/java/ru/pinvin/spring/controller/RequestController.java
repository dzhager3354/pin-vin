package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.pinvin.spring.service.KafkaProducerService;

@RestController
@RequestMapping("/request")
public class RequestController {
    @Autowired
    private KafkaProducerService service;

    @GetMapping("/send/{id}")
    public ResponseEntity<Boolean> send(@PathVariable("id")String phone) {
        service.processing(phone);
        return ResponseEntity.ok(true);
    }
}
