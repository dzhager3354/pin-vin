package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.AnswerNeuron;
import ru.pinvin.spring.dao.Call;
import ru.pinvin.spring.dao.CallResponseDAO;
import ru.pinvin.spring.dao.Phone;

@Service
public class KafkaConsumerService {
    @Autowired
    private CallService callService;
    @Autowired
    private AnswerNeuronService service;

    @KafkaListener(topics = "topicPython", groupId = "myGroup")
    public void consume(CallResponseDAO dao) {
        System.out.println("dzhager3354: consume message from python");
        Call call = callService.getCallById(dao.getId());
        AnswerNeuron answerNeuron = new AnswerNeuron();
        answerNeuron.setCategory(dao.getCategory());
        answerNeuron.setKeywords(dao.getKeywords());
        answerNeuron.setSentiment(dao.getSentiment());
        answerNeuron.setProbability(dao.getProbability());
        answerNeuron.setRecommendation(dao.getRecommendation());
        answerNeuron.setTranscript(dao.getTranscript());
        answerNeuron = service.saveAnswerNeuron(answerNeuron);
        call.setAnswerNeuron(answerNeuron);
        callService.updateCall(call);
    }
}