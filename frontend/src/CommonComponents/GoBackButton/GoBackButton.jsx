import './GoBackButton.css';

export default function GoBackButton({ path, label }) {
    const handleClick = () => {
        window.location.href = path;
    };

    return (
        <button className="go-back-button" onClick={handleClick}>
            <img src="/icons/arrow.png" alt="Arrow" className="go-back-button__icon" />
            <span className="go-back-button__text">{label}</span>
        </button>
    );
}