package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.pinvin.spring.dao.Call;
import ru.pinvin.spring.service.CallService;

import java.util.List;

@RestController
@RequestMapping("/calls")
public class CallController {
    @Autowired
    private CallService service;

    @GetMapping("/get/{id}")
    public ResponseEntity<List<Call>> getCallers(@PathVariable("id") long id) {
        return ResponseEntity.ok(service.getCallsByPhoneId(id));
    }
}
