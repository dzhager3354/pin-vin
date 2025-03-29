package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.pinvin.spring.dao.StatsDAO;
import ru.pinvin.spring.service.StatsService;

@RestController
@RequestMapping("/stats")
@CrossOrigin(origins = "http://localhost:3333")
public class StatsController {
    @Autowired
    private StatsService service;

    @GetMapping("/get")
    public ResponseEntity<StatsDAO> getStats() {
        return ResponseEntity.ok(service.getStats());
    }
}
