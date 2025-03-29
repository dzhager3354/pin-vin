package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.pinvin.spring.dao.AnswerNeuron;
import ru.pinvin.spring.service.AnswerNeuronService;

@RestController
@RequestMapping("/answer")
@CrossOrigin(origins = "http://localhost:3333")
public class AnswersController {
    @Autowired
    private AnswerNeuronService service;

    @GetMapping("/get/{id}")
    public ResponseEntity<AnswerNeuron> getAnswerById(@PathVariable("id") long id) {
        return ResponseEntity.ok(service.getAnswerNeuronById(id));
    }

    @GetMapping("/get-by-call/{id}")
    public ResponseEntity<AnswerNeuron> getAnswerByCallId(@PathVariable("id") long id) {
        return ResponseEntity.ok(service.getAnswerNeuronByCallId(id));
    }
}
