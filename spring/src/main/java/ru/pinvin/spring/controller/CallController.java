package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.pinvin.spring.dao.Call;
import ru.pinvin.spring.service.CallService;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/calls")
@CrossOrigin(origins = "http://localhost:3333")
public class CallController {
    @Autowired
    private CallService service;

    @GetMapping("/get/{id}")
    public ResponseEntity<List<Map<String, Object>>> getCallers(@PathVariable("id") long id) {
        return ResponseEntity.ok(service.getCallsByPhoneId(id));
    }

    @GetMapping("/get-call/{id}")
    public ResponseEntity<Call> getCallById(@PathVariable("id") long id) {
        return ResponseEntity.ok(service.getCallById(id));
    }
}
