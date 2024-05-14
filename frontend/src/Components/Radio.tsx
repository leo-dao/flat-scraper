import React from 'react';

interface Props {
    name: string;
    options: { label: string; value: string; }[];
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Radio: React.FC<Props> = ({ name, options, value, onChange }) => {
    return (
        <div>
            {options.map(option => (
                <label key={option.value}>
                    <input
                        type="radio"
                        name={name}
                        value={option.value}
                        checked={value === option.value}
                        onChange={onChange}
                    />
                    {option.label}
                </label>
            ))}
        </div>
    );
};

export default Radio;
