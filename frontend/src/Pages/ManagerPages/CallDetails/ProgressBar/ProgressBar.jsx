import React from 'react';
import { useState, useEffect } from 'react';
import './ProgressBar.css';

export default function ProgressBar({ value, width }) {
    const progress = Math.min(Math.max(value, 0), 100);
    const [animatedProgress, setAnimatedProgress] = useState(0);

    useEffect(() => {
        const animationDuration = 800;
        const startTime = performance.now();
        
        const animate = (currentTime) => {
            const elapsedTime = currentTime - startTime;
            const progressFraction = Math.min(elapsedTime / animationDuration, 1);
            setAnimatedProgress(progress * progressFraction);
            
            if (progressFraction < 1) {
                requestAnimationFrame(animate);
            }
        };
        
        requestAnimationFrame(animate);
    }, [progress]);

    return (
        <div className="progress-bar-container" style={{ width: `${width}px` }}>
            <div className="progress-bar-track">
                <div
                    className="progress-bar-filled"
                    style={{ 
                        width: `${animatedProgress}%`,
                        borderRadius: '15px'
                    }}
                />
            </div>
            <p className="progress-bar-text">Вероятность: {Math.round(animatedProgress)}%</p>
        </div>
    );
}