package ru.pinvin.spring.dao;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "calls")
public class Call {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "phones_id", nullable = false)
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
