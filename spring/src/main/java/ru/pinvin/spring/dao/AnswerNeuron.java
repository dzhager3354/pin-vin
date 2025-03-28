package ru.pinvin.spring.dao;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.List;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "answer_neurons")
public class AnswerNeuron {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "category", nullable = false)
    private String category;

    @Column(name = "probability", nullable = false)
    private double probability;

    @Column(name = "transcript", columnDefinition = "TEXT")
    private String transcript;

    @ElementCollection
    @CollectionTable(name = "call_keywords", joinColumns = @JoinColumn(name = "call_id"))
    @Column(name = "keywords")
    private List<String> keywords;

    @Column(name = "sentiment", nullable = false)
    private String sentiment;

    @Column(name = "recommendation")
    private String recommendation;
}
