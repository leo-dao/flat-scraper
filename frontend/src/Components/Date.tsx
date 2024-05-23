import React from 'react';
import DatePicker from 'react-date-picker';
import { Value } from './type';

interface DateProps {
    selectedDate: Value;
    onChange: (date: Value) => void;
}

const DateInput: React.FC<DateProps> = ({ selectedDate, onChange }) => {

    const handleDateChange = (date: Value) => {
        onChange(date);
    };

    return (
        <DatePicker
            value={selectedDate}
            onChange={handleDateChange}
        />
    );
};

export default DateInput;
