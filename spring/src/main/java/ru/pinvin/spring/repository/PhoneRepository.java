package ru.pinvin.spring.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.pinvin.spring.dao.Phone;

@Repository
public interface PhoneRepository extends JpaRepository<Phone, Long> {
    Phone findByPhone(String phone);
}