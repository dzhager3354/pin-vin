package ru.pinvin.spring.dao;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class CallRequestDAO {
    private Long phoneId;
    private Long managerId;
}