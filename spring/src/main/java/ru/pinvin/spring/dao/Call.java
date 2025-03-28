package ru.pinvin.spring.dao;

import com.fasterxml.jackson.annotation.JsonBackReference;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.Date;
import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table
public class Call {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "phone", nullable = false)
    @ManyToOne
    private Phone phone;

    @ManyToOne
    @JoinColumn(name = "managers_id", nullable = false)
    private Manager manager;

    @OneToOne
    @JoinColumn(name = "answer_neurons_id")
    private AnswerNeuron answerNeuron;

    @Column(name = "date", nullable = false)
    private LocalDateTime date;

}
