import React from 'react';
import './ProgressBar.css';

export default function ProgressBar({ value, width }) {
    // Ограничиваем значение от 0 до 100
    const progress = Math.min(Math.max(value, 0), 100);

    return (
        <div className="progress-bar-container" style={{ width: `${width}px` }}>
            {/* Заполненная часть */}
            <div
                className="progress-bar-filled"
                style={{ width: `${progress}%` }}
            ></div>
            {/* Текст прогресса */}
            <p className="progress-bar-text">Вероятность: {progress}%</p>
        </div>
    );
}