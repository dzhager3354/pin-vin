package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.pinvin.spring.dao.AnswerNeuron;
import ru.pinvin.spring.service.AnswerNeuronService;

@RestController
@RequestMapping("/answer")
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
