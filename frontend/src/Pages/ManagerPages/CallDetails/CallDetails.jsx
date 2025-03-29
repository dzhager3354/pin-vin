import React, { useEffect, useState } from 'react';
import axios from 'axios'; // Если хотите использовать fetch, замените на fetch
import { useParams } from 'react-router-dom'; // Для получения параметров из URL
import './CallDetails.css';
import Header from '../../../CommonComponents/Header/Header';
import ProgressBar from './ProgressBar/ProgressBar';
import AnswerData from './AnswerData/AnswerData';
import GoBackButton from '../../../CommonComponents/GoBackButton/GoBackButton';

export default function CallDetails() {
    // Имитация данных из JSON
    const jsonData1 = {
        id: 123,
        phone: "79371459849", // Заглушка для телефона
    };

    const jsonData2 = {
        date: "2023-10-05T14:30:00", // Заглушка для даты
    };

    const jsonData3 = {
        category: "Продажа",
        transcript: "Клиент интересовался продуктом, задавал вопросы о гарантии.",
        keywords: ["продукт", "гарантия", "цена", "продукт", "гарантия", "цена", "продукт", "гарантия", "цена"],
        sentiment: "позитивный",
        recommendation: "Предложить скидку для закрытия сделки.",
        probability: 70,
    };

    // Состояние для хранения данных о телефоне
    const [phoneData, setPhoneData] = useState(null);

    // Состояние для хранения данных о звонке
    const [callData, setCallData] = useState(null);

    // Состояние для хранения данных анализа разговора
    const [answerData, setAnswerData] = useState(null);

    // Получаем параметры из URL
    const { callId, currentId } = useParams();

    // Эффект для выполнения GET-запроса для телефона
    useEffect(() => {
        const fetchPhoneData = async () => {
            try {
                const response = await axios.get(`http://localhost:8080/phone/get-phone/${currentId}`);
                setPhoneData(response.data); // Сохраняем данные из ответа
            } catch (err) {
                console.error('Не удалось получить данные о телефоне:', err);
                // Игнорируем ошибку и оставляем phoneData равным null
            }
        };

        fetchPhoneData();
    }, [currentId]); // Зависимость от currentId

    // Эффект для выполнения GET-запроса для звонка
    useEffect(() => {
        const fetchCallData = async () => {
            try {
                const response = await axios.get(`http://localhost:8080/calls/get-call/${callId}`);
                setCallData(response.data); // Сохраняем данные из ответа
            } catch (err) {
                console.error('Не удалось получить данные о звонке:', err);
                // Игнорируем ошибку и оставляем callData равным null
            }
        };

        fetchCallData();
    }, [callId]); // Зависимость от callId

    // Эффект для выполнения GET-запроса для анализа разговора
    useEffect(() => {
        const fetchAnswerData = async () => {
            try {
                // Устанавливаем таймаут для запроса (например, 5 секунд)
                const controller = new AbortController(); // Для отмены запроса при таймауте
                const timeoutId = setTimeout(() => controller.abort(), 5000); // Таймаут 5 секунд

                const response = await axios.get(`http://localhost:8080/answer/get-by-call/${callId}`, {
                    signal: controller.signal, // Передаём сигнал для отмены
                });

                clearTimeout(timeoutId); // Очищаем таймаут, если запрос выполнен успешно
                setAnswerData(response.data); // Сохраняем данные из ответа
            } catch (err) {
                if (err.name === 'AbortError') {
                    console.error('Запрос превысил таймаут (5 секунд)');
                } else {
                    console.error('Не удалось получить данные анализа разговора:', err);
                }
                // Игнорируем ошибку и оставляем answerData равным null
            }
        };

        fetchAnswerData();
    }, [callId]); // Зависимость от callId

    // Используем переданные phoneData или значения по умолчанию
    const phoneInfo = phoneData || jsonData1;

    // Используем переданные callData или значения по умолчанию
    const callInfo = callData || jsonData2;

    // Используем переданные answerData или значения по умолчанию
    const analysisData = answerData || jsonData3;

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
            <GoBackButton path="/calls-by-phonenumber/:id" label="назад" />
            <div className="details-area">
                <p className="details-name">Иван Петров</p>
                <p className="details-info">
                    +{phoneInfo.phone} {formatDate(callInfo.date)}
                </p>
                <ProgressBar value={analysisData.probability} width={"100%"} />
                <p className="details-subtitle">Анализ разговора:</p>
                <p className="details-info">{analysisData.transcript}</p>
                <div className="answer-data-container">
                    <AnswerData
                        title="Ключевые слова" 
                        items={analysisData.keywords} 
                        width="49%" 
                        height="200px" 
                    />
                    <AnswerData
                        title="Эмоциональный тон" 
                        items={[analysisData.sentiment]} 
                        width="49%" 
                        height="200px" 
                    />
                </div>
                <p className="details-subtitle">Рекомендации:</p>
                <p className="details-info">{analysisData.recommendation}</p>
            </div>
        </>
    );
}