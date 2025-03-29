import './Header.css';
import { useNavigate } from 'react-router-dom';

export default function Header() {
    const navigate = useNavigate();

    const handleLogoClick = () => {
        navigate('/'); // Переход на главную страницу
    };

    return (
        <header className="header">
            <div 
                className="header__logo"
                onClick={handleLogoClick}
                style={{ cursor: 'pointer' }} // Добавляем указатель при наведении
            >
                VINPIN
            </div>
        </header>
    );
}