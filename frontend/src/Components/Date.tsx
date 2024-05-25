import React from 'react';
import styled from 'styled-components';

interface DateProps {
    selectedDate: Date | null;
    onChange: (date: Date | null) => void;
}

const Select = styled.select`
    width: 100%;
    padding: 10px 15px;
    border-radius: 8px;
    border: 2px solid #ccc;
    font-size: 16px;
    cursor: pointer;
    transition: border-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;

    &:hover {
        border-color: #555;
    }
`;

const months = [
    { value: "01", label: "January" },
    { value: "02", label: "February" },
    { value: "03", label: "March" },
    { value: "04", label: "April" },
    { value: "05", label: "May" },
    { value: "06", label: "June" },
    { value: "07", label: "July" },
    { value: "08", label: "August" },
    { value: "09", label: "September" },
    { value: "10", label: "October" },
    { value: "11", label: "November" },
    { value: "12", label: "December" }
];

const DateInput: React.FC<DateProps> = ({ selectedDate, onChange }) => {

    const handleMonthChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const newDate = selectedDate ? new Date(selectedDate) : new Date();
        newDate.setMonth(parseInt(e.target.value) - 1);
        onChange(newDate);
    };

    return (
        <Select
            value={selectedDate ? (selectedDate.getMonth() + 1).toString().padStart(2, '0') : ''}
            onChange={handleMonthChange}
        >
            <option value="">Select a start month</option>
            {months.map(month => (
                <option key={month.value} value={month.value}>{month.label}</option>
            ))}
        </Select>
    );
};

export default DateInput;
