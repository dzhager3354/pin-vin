import React, { useEffect, useState } from 'react';
import axios from 'axios'; // Если хотите использовать fetch, замените на fetch
import { useParams } from 'react-router-dom'; // Для получения параметров из URL
import './CallsByPhoneNumber.css';
import Header from '../../../CommonComponents/Header/Header';
import GoBackButton from '../../../CommonComponents/GoBackButton/GoBackButton';
import CallButtonsArea from './CallButtonsArea/CallButtonsArea';

export default function CallsByPhoneNumber() {
    // Получаем id из URL
    const { id } = useParams();

    // Состояние для хранения списка звонков
    const [callList, setCallList] = useState(null);

    // Заглушка (используется, если данные не получены)
    const defaultCallList = [
        {
            id: 1,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 2,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 3,
            manager: 789,
            date: "2023-10-07T16:45:00"
        },
        {
            id: 4,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 5,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 6,
            manager: 789,
            date: "2023-10-07T16:45:00"
        },
        {
            id: 7,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 8,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 9,
            manager: 789,
            date: "2023-10-07T16:45:00"
        },
        {
            id: 10,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 11,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 12,
            manager: 789,
            date: "2023-10-07T16:45:00"
        }
    ];

    // Эффект для выполнения GET-запроса при монтировании компонента
    useEffect(() => {
        const fetchCalls = async () => {
            try {
                const response = await axios.get(`http://localhost:8080/calls/get/${id}`);
                setCallList(response.data); // Сохраняем данные из ответа
            } catch (err) {
                console.error('Не удалось получить данные:', err);
                // Игнорируем ошибку и оставляем callList равным null
            }
        };

        fetchCalls();
    }, [id]); // Зависимость от id

    // Используем переданные callList или значения по умолчанию
    const data = callList || defaultCallList;

    return (
        <>
            <Header />
            <GoBackButton path="/manager-phone-numbers" label="к номерам" />
            <CallButtonsArea callList={data} />
        </>
    );
}