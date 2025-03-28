package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.Call;
import ru.pinvin.spring.repository.CallRepository;

import java.util.List;

@Service
public class CallService {
    @Autowired
    private CallRepository repository;

    public List<Call> getCalls() {
        return repository.findAll();
    }

    public List<Call> getCallsByPhone(String phone) {

    }

    public List<String> getAllPhones() {

    }

    public List<> getId
}
