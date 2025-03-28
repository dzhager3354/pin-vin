package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.Call;
import ru.pinvin.spring.repository.CallRepository;

import java.util.List;

@Service
public class CallService {

    @Autowired
    private CallRepository callRepository;

    public List<Call> getAllCalls() {
        return callRepository.findAll();
    }

    public Call getCallById(Long id) {
        return callRepository.findById(id).orElse(null);
    }

    public Call saveCall(Call call) {
        return callRepository.save(call);
    }

    public void deleteCall(Long id) {
        callRepository.deleteById(id);
    }

    public List<Call> getCallsByManagerId(Long managerId) {
        return callRepository.findByManagerId(managerId);
    }

    public List<Call> getCallsByPhoneId(Long phoneId) {
        return callRepository.findByPhoneId(phoneId);
    }
}