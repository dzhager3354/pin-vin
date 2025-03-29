import React from 'react';
import './StatsBlock.css';

export default function StatsBlock({ label, value, width = '150px', height = '100px' }) {
    const containerStyle = {
        width: width,
        height: height,
    };

    return (
        <div className="stats-block" style={containerStyle}>
            <div className="stats-block__content">
                <div className="stats-block__label">{label}</div>
                <div className="stats-block__value">{value}</div>
            </div>
        </div>
    );
}