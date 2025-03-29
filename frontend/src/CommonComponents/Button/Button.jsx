import './Button.css'

export default function Button({ backgroundColor, label, onClick, width, height }) {
    const buttonStyle = {
        backgroundColor,
        width: width || 'auto', // Если ширина не указана, используется auto
        height: height || 'auto', // Если высота не указана, используется auto
    };

    return (
        <button
            className="custom-button"
            style={buttonStyle}
            onClick={onClick}
        >
            {label}
        </button>
    );
}