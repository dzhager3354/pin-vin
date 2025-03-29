import './EmptyArea.css';

export default function EmptyArea({ children }) {
    return (
        <div className="empty-area">
            {children}
        </div>
    );
}