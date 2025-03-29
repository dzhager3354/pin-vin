import React, { useEffect, useState } from 'react';
import axios from 'axios'; // Если хотите использовать fetch, замените на fetch
import './SuperviserStats.css';
import Header from '../../../CommonComponents/Header/Header';
import GoBackButton from '../../../CommonComponents/GoBackButton/GoBackButton';
import StatsBlock from './StatsBlock/StatsBlock';

export default function SuperviserStats() {
    // Состояние для хранения статистики
    const [stats, setStats] = useState(null);

    // Значения по умолчанию
    const defaultStats = {
        amount: 2171,
        hot: 121,
        warm: 179,
        cold: 41,
        conversion: 0.57,
    };

    // Эффект для выполнения GET-запроса при монтировании компонента
    useEffect(() => {
        const fetchStats = async () => {
            try {
                const response = await axios.get('http://localhost:8080/stats/get');
                setStats(response.data); // Сохраняем данные из ответа
            } catch (err) {
                console.error('Не удалось получить данные:', err);
                // Игнорируем ошибку и оставляем stats равным null
            }
        };

        fetchStats();
    }, []);

    // Используем переданные stats или значения по умолчанию
    const data = stats || defaultStats;

    // Маппинг данных из JSON в массив блоков
    const blocks = [
        { label: 'Всего звонков', value: data.amount },
        { label: 'Горячие', value: data.hot },
        { label: 'Тёплые', value: data.warm },
        { label: 'Холодные', value: data.cold },
        { label: 'Конверсия', value: `${data.conversion} %` },
    ];

    return (
        <>
            <Header />
            <GoBackButton path="/" label="назад" />
            <div className="statBlocksContainer">
                {blocks.map((block, index) => (
                    <StatsBlock
                        key={block.label} // Используем label как уникальный ключ
                        label={block.label}
                        value={block.value}
                        width="200px"
                        height="130px"
                    />
                ))}
            </div>
        </>
    );
}