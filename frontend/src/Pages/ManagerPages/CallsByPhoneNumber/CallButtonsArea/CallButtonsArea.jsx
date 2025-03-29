import React from 'react';
import CallInfoButton from '../CallInfoButton/CallInfoButton'; // Импортируем кнопку
import './CallButtonsArea.css'; // Импортируем стили

export default function CallButtonsArea({ callList }) {
    return (
        <div className="call-buttons-area">
            {callList.map((callData) => (
                <CallInfoButton key={callData.id} callData={callData} />
            ))}
        </div>
    );
}