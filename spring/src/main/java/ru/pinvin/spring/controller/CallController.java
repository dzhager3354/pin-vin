package ru.pinvin.spring.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CallController {
    @GetMapping("/")
    public ResponseEntity getCallers() {
        return ResponseEntity.ok(null);
    }
}
