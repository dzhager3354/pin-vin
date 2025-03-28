package ru.pinvin.spring.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import ru.pinvin.spring.dao.Call;

@Repository
public interface CallRepository extends JpaRepository<Call, Long> {

}
