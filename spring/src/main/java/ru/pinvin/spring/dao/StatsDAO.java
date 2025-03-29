package ru.pinvin.spring.dao;

import jakarta.persistence.Entity;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class StatsDAO {
    private int amount;
    private int hot;
    private int warm;
    private int cold;
    private double conversion;
}
