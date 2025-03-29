import React from 'react';
import './PhoneButton.css';

export default function PhoneButton({ phoneData }) {
    const handleClick = () => {
        // При клике переходим на страницу с использованием id
        window.location.href = `/calls-by-phonenumber/${phoneData.id}`;
        // alert(phoneData.id);
    };

    return (
        <button className="phone-button" onClick={handleClick}>
            {phoneData.phone}
        </button>
    );
}