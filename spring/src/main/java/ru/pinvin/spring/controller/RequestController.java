package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.pinvin.spring.service.KafkaProducerService;

@RestController
@RequestMapping("/request")
@CrossOrigin(origins = "http://localhost:3333")
public class RequestController {
    @Autowired
    private KafkaProducerService service;

    @GetMapping("/send/{id}")
    public ResponseEntity<Boolean> send(@PathVariable("id")String phone) {
        service.processing(phone);
        return ResponseEntity.ok(true);
    }
}
