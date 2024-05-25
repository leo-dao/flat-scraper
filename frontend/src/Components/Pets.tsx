import React from 'react';
import styled from 'styled-components';

interface Props {
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Container = styled.div`
    display: flex;
    flex-direction: column;
    gap: 5px;
`;

const petOptions = [
    { value: 'No pets allowed', label: 'No pets allowed' },
    { value: 'Dogs allowed', label: 'Dogs allowed' },
    { value: 'Cats allowed', label: 'Cats allowed' },
];

const Pets: React.FC<Props> = ({ value, onChange }) => {
    return (
        <Container>
            {petOptions.map(option => (
                <label key={option.value}>
                    <input
                        type="radio"
                        name='Pets'
                        value={option.value}
                        checked={value === option.value}
                        onChange={onChange}
                    />
                    {option.label}
                </label>
            ))}
        </Container>
    );
};

export default Pets;