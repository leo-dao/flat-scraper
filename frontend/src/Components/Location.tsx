import React from 'react';
import styled from 'styled-components';

interface Props {
    value: string;
    onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
}

const Select = styled.select`
    width: 100%;
    padding: 10px 15px;
    border-radius: 8px;
    border: 2px solid #ccc;
    font-size: 16px;
    cursor: pointer;
`;

// Hardcoding for now
const options = [
    'Montreal',
    'Toronto',
    'Vancouver',
];

const Location: React.FC<Props> = ({value, onChange }) => {
    return (
        <Select name={'Pick a location'} value={value} onChange={onChange}>
            {options.map(option => (
                <option key={option} value={option}>{option}</option>
            ))}
        </Select>
    );
};

export default Location;
