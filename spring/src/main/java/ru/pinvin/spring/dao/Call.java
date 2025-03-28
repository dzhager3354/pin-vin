package ru.pinvin.spring.dao;

import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.Date;
import java.util.UUID;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Call {
    @Id
    private UUID uuid;
    private int managerId;
    private String number;
    private Date callDate;

}
