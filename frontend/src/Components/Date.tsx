import React from 'react';

interface Props {
    name: string;
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Date: React.FC<Props> = ({ name, value, onChange }) => {
    return (
        <input
            type="date"
            name={name}
            value={value}
            onChange={onChange}
        />
    );
};

export default Date;