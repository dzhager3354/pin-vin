import React from 'react';
import './CallDetails.css';
import Header from '../../../CommonComponents/Header/Header';
import ProgressBar from './ProgressBar/ProgressBar';
import AnswerData from './AnswerData/AnswerData';

export default function CallDetails() {
    // Имитация данных из JSON
    const jsonData1 = {
        id: 123,
        phone: "79371459849",
    };

    const jsonData2 = {
        date: "2023-10-05T14:30:00",
    };

    const jsonData3 = {
        category: "Продажа",
        transcript: "Клиент интересовался продуктом, задавал вопросы о гарантии.",
        keywords: ["продукт", "гарантия", "цена", "продукт", "гарантия", "цена", "продукт", "гарантия", "цена"],
        sentiment: "позитивный",
        recommendation: "Предложить скидку для закрытия сделки.",
        probability: 70,
    };

    // Функция для форматирования даты
    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0'); // Месяцы начинаются с 0
        const year = date.getFullYear();
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');

        return `${day}.${month}.${year} ${hours}:${minutes}`;
    };

    return (
        <>
            <Header />
            <div className="details-area">
                <p className="details-name">Иван Петров</p>
                <p className="details-info">
                    +{jsonData1.phone} {formatDate(jsonData2.date)}
                </p>
                <ProgressBar value={jsonData3.probability} width={"100%"} />
                <p className="details-subtitle">Анализ разговора:</p>
                <p className="details-info">{jsonData3.transcript}</p>
                <div className="answer-data-container">
                    <AnswerData
                        title="Ключевые слова" 
                        items={jsonData3.keywords} 
                        width="49%" 
                        height="200px" 
                    />
                    <AnswerData
                        title="Эмоциональный тон" 
                        items={[jsonData3.sentiment]} 
                        width="49%" 
                        height="200px" 
                    />
                </div>
                <p className="details-subtitle">Рекомендации:</p>
                <p className="details-info">{jsonData3.recommendation}</p>
            </div>
        </>
    );
}