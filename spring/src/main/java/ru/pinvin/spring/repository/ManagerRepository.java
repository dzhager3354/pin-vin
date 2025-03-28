package ru.pinvin.spring.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.pinvin.spring.dao.Manager;

@Repository
public interface ManagerRepository extends JpaRepository<Manager, Long> {
    Manager findByFullname(String fullname);
}