import './Chips.css';

export default function Chips({ label }) {
    // Определяем цвет фона в зависимости от значения label
    const getBackgroundColor = () => {
        if (label === 'позитивный') return '#4CAF50'; // Зелёный
        if (label === 'нейтральный') return '#2196F3'; // Синий
        if (label === 'негативный') return '#FF9800'; // Оранжевый
        return 'white'; // По умолчанию белый
    };

    const backgroundColor = getBackgroundColor();

    return (
        <div 
            className="chips" 
            style={{ backgroundColor }} // Динамически задаём цвет фона
        >
            {label}
        </div>
    );
}