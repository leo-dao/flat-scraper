import React from 'react';

interface Props {
    name: string;
    type: string;
    placeholder: string;
    value: string | number;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Text: React.FC<Props> = ({ name, type, placeholder, value, onChange }) => {
    return (
        <input
            type={type}
            name={name}
            placeholder={placeholder}
            value={value}
            onChange={onChange}
        />
    );
};

export default Text;
