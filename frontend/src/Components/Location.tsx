import React from 'react';

interface Props {
    name: string;
    options: string[];
    value: string;
    onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
}

const Location: React.FC<Props> = ({ name, options, value, onChange }) => {
    return (
        <select name={name} value={value} onChange={onChange}>
            {options.map(option => (
                <option key={option} value={option}>{option}</option>
            ))}
        </select>
    );
};

export default Location;
