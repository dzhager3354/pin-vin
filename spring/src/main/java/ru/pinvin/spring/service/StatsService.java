package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.AnswerNeuron;
import ru.pinvin.spring.dao.StatsDAO;
import ru.pinvin.spring.repository.AnswerNeuronRepository;

import java.util.List;

@Service
public class StatsService {
    @Autowired
    private AnswerNeuronRepository repository;

    public StatsDAO getStats() {
        StatsDAO dao = new StatsDAO();
        List<AnswerNeuron> answers = repository.findAll();
        dao.setHot((int) answers.stream().filter(answerNeuron -> answerNeuron.getCategory().equals("hot")).count());
        dao.setWarm((int) answers.stream().filter(answerNeuron -> answerNeuron.getCategory().equals("warm")).count());
        dao.setCold((int) answers.stream().filter(answerNeuron -> answerNeuron.getCategory().equals("cold")).count());
        dao.setAmount(answers.size());
        dao.setConversion(dao.getAmount() == 0 ? 0 : (dao.getHot())/dao.getAmount());
        return dao;
    }
}
