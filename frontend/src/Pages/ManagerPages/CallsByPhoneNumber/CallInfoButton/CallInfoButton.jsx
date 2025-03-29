import React from 'react';
import './CallInfoButton.css';

export default function CallInfoButton({ callData }) {
    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');

        return `${day}.${month}.${year} в ${hours}:${minutes}`;
    };

    const handleClick = () => {
        const currentPath = window.location.pathname; // Текущий путь
        const currentId = currentPath.split('/').pop(); // Извлекаем id из текущего URL
        window.location.href = `/call-details/${callData.id}/${currentId}`; // Формируем новый URL
    };

    // Массив доступных цветов
    const colors = ['#d82727', '#42a5f5', 'orange'];

    // Генерация случайного индекса
    const getRandomColor = () => {
        const randomIndex = Math.floor(Math.random() * colors.length);
        return colors[randomIndex];
    };

    const circleColor = getRandomColor();

    console.log('Rendering CallInfoButton:', { callData, circleColor });

    return (
        <button className="call-info-button" onClick={handleClick}>
            {/* Кружок */}
            <span className="circle" style={{ backgroundColor: circleColor }}></span>
            {/* Текст кнопки */}
            Звонок от {formatDate(callData.date)} от Менеджера {callData.manager}
        </button>
    );
}