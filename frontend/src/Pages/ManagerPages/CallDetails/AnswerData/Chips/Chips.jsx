import './Chips.css';

export default function Chips({ label }) {
    const getBackgroundColor = () => {
        if (label === 'позитивный' || label === 'positive') {
            label = 'позитивный'
            return '#4CAF50';
        } 
        if (label === 'нейтральный' || label === 'neutral') {
            label = 'нейтральный'
            return '#2196F3';
        } 
        if (label === 'негативный' || label === 'negative') {
            label = 'негативный'
            return '#FF9800';
        }
        return 'white';
    };

    const backgroundColor = getBackgroundColor();

    return (
        <div 
            className="chips" 
            style={{ backgroundColor }} 
        >
            {label}
        </div>
    );
}