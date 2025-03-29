import './CallsByPhoneNumber.css'
import Header from '../../../CommonComponents/Header/Header'
import GoBackButton from '../../../CommonComponents/GoBackButton/GoBackButton'
import EmptyArea from '../../../CommonComponents/EmptyArea/EmptyArea'
import './CallButtonsArea/CallButtonsArea'
import CallButtonsArea from './CallButtonsArea/CallButtonsArea'

export default function CallsByPhoneNumber() {

    const callList = [
        {
            id: 1,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 2,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 3,
            manager: 789,
            date: "2023-10-07T16:45:00"
        },
        {
            id: 4,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 5,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 6,
            manager: 789,
            date: "2023-10-07T16:45:00"
        },
        {
            id: 7,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 8,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 9,
            manager: 789,
            date: "2023-10-07T16:45:00"
        },
        {
            id: 10,
            manager: 123,
            date: "2023-10-05T14:30:00"
        },
        {
            id: 11,
            manager: 456,
            date: "2023-10-06T09:15:00"
        },
        {
            id: 12,
            manager: 789,
            date: "2023-10-07T16:45:00"
        }
    ];

    return(
        <>
            <Header/>
            <GoBackButton path="/manager-phone-numbers" label="к номерам" />
            <CallButtonsArea callList={callList}/>
        </>
    );
}