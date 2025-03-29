import React from 'react';
import PhoneButton from '../PhoneButton/PhoneButton';
import './Section.css';

export default function Section({ phoneList }) {
    return (
        <div className="section">
            {phoneList.map((phoneData) => (
                <PhoneButton key={phoneData.id} phoneData={phoneData} />
            ))}
        </div>
    );
}