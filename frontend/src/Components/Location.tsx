import React from 'react';

interface Props {
    value: string;
    onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
}

const options = [
    'Montreal',
    'Toronto',
    'Vancouver',
];

const Location: React.FC<Props> = ({value, onChange }) => {
    return (
        <select name={'Pick a location'} value={value} onChange={onChange}>
            {options.map(option => (
                <option key={option} value={option}>{option}</option>
            ))}
        </select>
    );
};

export default Location;
