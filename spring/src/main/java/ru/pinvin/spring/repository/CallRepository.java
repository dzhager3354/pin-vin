package ru.pinvin.spring.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.pinvin.spring.dao.Call;

import java.util.List;

@Repository
public interface CallRepository extends JpaRepository<Call, Long> {
    List<Call> findByManagerId(Long managerId);
    List<Call> findByPhoneId(Long phoneId);
}
