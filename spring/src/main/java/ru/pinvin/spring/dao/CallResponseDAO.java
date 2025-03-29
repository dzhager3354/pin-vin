package ru.pinvin.spring.dao;

import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Data
public class CallResponseDAO {
    private long id;
    private String category;
    private double probability;
    private String transcript;
    private List<String> keywords;
    private String sentiment;
    private String recommendation;
}
