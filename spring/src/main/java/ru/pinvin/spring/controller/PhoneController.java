package ru.pinvin.spring.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.pinvin.spring.dao.Phone;
import ru.pinvin.spring.service.PhoneService;

import java.util.List;

@RestController
@RequestMapping("/phone")
public class PhoneController {
    @Autowired
    private PhoneService service;

    @GetMapping("/get")
    public ResponseEntity<List<Phone>> getAllPhones() {
        return ResponseEntity.ok(service.getAllPhones());
    }

    @GetMapping("/get-phone/{id}")
    public ResponseEntity<Phone> getPhoneById(@PathVariable("id") long id) {
        return ResponseEntity.ok(service.getPhoneById(id));
    }
}
