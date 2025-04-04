import './Gate.css';
import Header from '../../CommonComponents/Header/Header';
import Button from '../../CommonComponents/Button/Button';

export default function Gate() {
    return (
        <>
            <Header />
            <div className="gate-buttons">
                <Button
                    backgroundColor="#d82727"
                    label="менеджер"
                    width="200px"
                    onClick={() => window.location.href = '/manager-phone-numbers'}
                />
                <Button
                    backgroundColor="#d82727"
                    label="директор"
                    width="200px"
                    onClick={() => window.location.href = '/superviser-stats'}
                />
            </div>
        </>
    );
}