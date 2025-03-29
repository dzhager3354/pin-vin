package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.Call;
import ru.pinvin.spring.repository.CallRepository;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

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

    public List<Map<String, Object>> getCallsByPhoneId(Long phoneId) {
        List<Call> calls = callRepository.findByPhoneId(phoneId);
        return calls.stream()
                .filter(call -> call.getManager() != null)
                .map(call -> {
                    Map<String, Object> result = new HashMap<>();
                    result.put("id", call.getId());
                    result.put("manager", call.getManager().getId());
                    result.put("date", call.getDate());
                    return result;
                })
                .collect(Collectors.toList());
    }

    public Call updateCall(Call call) {
        return callRepository.save(call);
    }
}