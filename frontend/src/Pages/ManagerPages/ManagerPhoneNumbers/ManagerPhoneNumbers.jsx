import React, { useEffect, useState } from 'react';
import axios from 'axios'; // Если хотите использовать fetch, замените на fetch
import Header from '../../../CommonComponents/Header/Header';
import Section from '../../../CommonComponents/PhoneNumbersSection/Section/Section';
import GoBackButton from '../../../CommonComponents/GoBackButton/GoBackButton';
import EmptyArea from '../../../CommonComponents/EmptyArea/EmptyArea';

export default function ManagerPhoneNumbers() {
    // Состояние для хранения списка телефонов
    const [phoneList, setPhoneList] = useState(null);

    // Заглушка (используется, если данные не получены)
    const defaultPhoneList = [
        { id: 1, phone: "12345678909" },
        { id: 2, phone: "98765432101" },
        { id: 3, phone: "33333333333" },
        { id: 4, phone: "77777777777" },
        { id: 5, phone: "77777777777" },
        { id: 6, phone: "12345678909" },
        { id: 7, phone: "98765432101" },
        { id: 8, phone: "33333333333" },
        { id: 9, phone: "77777777777" },
        { id: 10, phone: "77777777777" },
        { id: 11, phone: "98765432101" },
        { id: 12, phone: "33333333333" },
        { id: 13, phone: "77777777777" },
        { id: 14, phone: "77777777777" },
    ];

    // Эффект для выполнения GET-запроса при монтировании компонента
    useEffect(() => {
        const fetchPhones = async () => {
            try {
                const response = await axios.get('http://localhost:8080/phone/get');
                setPhoneList(response.data); // Сохраняем данные из ответа
            } catch (err) {
                console.error('Не удалось получить данные:', err);
                // Игнорируем ошибку и оставляем phoneList равным null
            }
        };

        fetchPhones();
    }, []);

    // Используем переданные phoneList или значения по умолчанию
    const data = phoneList || defaultPhoneList;

    return (
        <>
            <Header />
            <GoBackButton path="/" label="назад" />
            <div style={{ display: 'flex', gap: '20px' }}>
                {/* Секция с телефонами */}
                <Section phoneList={data} onClick={() => alert("!!!")} />
                {/* Пустая зона с красивой надписью */}
                <EmptyArea>
                    <div style={{
                        display: 'flex',
                        justifyContent: 'center',
                        alignItems: 'center',
                        height: '100%',
                        color: '#666',
                        fontSize: '1.5rem',
                        fontWeight: '300',
                        textAlign: 'center',
                        padding: '2rem',
                        font: 'Poppins',
                        opacity: 0.7,
                        background: 'linear-gradient(135deg, #f5f5f5 0%, #e9e9e9 100%)',
                        borderRadius: '12px',
                        boxShadow: 'inset 0 0 10px rgba(0,0,0,0.05)'
                    }}>
                        Выберите номер из списка<br />для просмотра звонков
                    </div>
                </EmptyArea>
            </div>
        </>
    );
}