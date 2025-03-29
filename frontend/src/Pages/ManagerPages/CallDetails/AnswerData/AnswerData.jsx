import './AnswerData.css';
import Chips from './Chips/Chips';

export default function AnswerData({ title, items, width, height }) {
    return (
        <div className="answer-data" style={{ width, height }}>
            <div className="answer-data__title">{title}</div>
            <div className="answer-data__chips">
                {items.map((item, index) => (
                    <Chips key={index} label={item} />
                ))}
            </div>
        </div>
    );
}