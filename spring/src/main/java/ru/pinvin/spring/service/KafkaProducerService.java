package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.Call;
import ru.pinvin.spring.dao.Phone;

@Service
public class KafkaProducerService {

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
    @Autowired
    private CallService service;
    @Autowired
    private PhoneService phoneService;

    @Autowired
    private ManagerService managerService;

    private static final String TOPIC = "myTopic";

    public void processing(String phone) {
        Call call = new Call();
        Phone phoneObj = phoneService.getPhoneByNumber(phone);
        if (phoneObj == null) {
            Phone newPhone = new Phone();
            newPhone.setPhone(phone);
            phoneObj = phoneService.savePhone(newPhone);
        }
        call.setPhone(phoneObj);
        call.setManager(managerService.getManagerById(1L));
        call = service.updateCall(call);
        kafkaTemplate.send(TOPIC, String.valueOf(call.getId()));
    }
}