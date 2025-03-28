package ru.pinvin.spring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.pinvin.spring.dao.Phone;
import ru.pinvin.spring.repository.PhoneRepository;

import java.util.List;

@Service
public class PhoneService {

    @Autowired
    private PhoneRepository phoneRepository;

    public List<Phone> getAllPhones() {
        return phoneRepository.findAll();
    }

    public Phone getPhoneById(Long id) {
        return phoneRepository.findById(id).orElse(null);
    }

    public Phone savePhone(Phone phone) {
        return phoneRepository.save(phone);
    }

    public void deletePhone(Long id) {
        phoneRepository.deleteById(id);
    }

    public Phone getPhoneByNumber(String phoneNumber) {
        return phoneRepository.findByPhone(phoneNumber);
    }
}