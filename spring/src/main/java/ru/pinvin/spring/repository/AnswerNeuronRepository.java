package ru.pinvin.spring.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.pinvin.spring.dao.AnswerNeuron;

import java.util.List;

@Repository
public interface AnswerNeuronRepository extends JpaRepository<AnswerNeuron, Long> {
    List<AnswerNeuron> findByCategory(String category);
}