import './GoBackButton.css';

export default function GoBackButton({ path }) {
    const handleClick = () => {
        window.location.href = path;
    };

    return (
        <button className="go-back-button" onClick={handleClick} aria-label="Назад">
            <svg className="go-back-button__icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 18L9 12L15 6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
        </button>
    );
}