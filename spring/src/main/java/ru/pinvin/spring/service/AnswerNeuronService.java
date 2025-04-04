package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.AnswerNeuron;
import ru.pinvin.spring.repository.AnswerNeuronRepository;
import ru.pinvin.spring.repository.CallRepository;

import java.util.List;

@Service
public class AnswerNeuronService {

    @Autowired
    private AnswerNeuronRepository answerNeuronRepository;

    @Autowired
    private CallRepository repository;

    public List<AnswerNeuron> getAllAnswerNeurons() {
        return answerNeuronRepository.findAll();
    }

    public AnswerNeuron getAnswerNeuronById(Long id) {
        return answerNeuronRepository.findById(id).orElse(null);
    }

    public AnswerNeuron saveAnswerNeuron(AnswerNeuron answerNeuron) {
        return answerNeuronRepository.save(answerNeuron);
    }

    public void deleteAnswerNeuron(Long id) {
        answerNeuronRepository.deleteById(id);
    }

    public List<AnswerNeuron> getAnswerNeuronsByCategory(String category) {
        return answerNeuronRepository.findByCategory(category);
    }

    public AnswerNeuron getAnswerNeuronByCallId(long callId) {
        return repository.findById(callId).get().getAnswerNeuron();
    }
}