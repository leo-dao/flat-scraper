import React, { useState } from 'react';
import styled from 'styled-components';
import Pets from './Pets';
import Date from './Date';
import Price from './Price';
import Location from './Location';
import Mail from './Mail';
import { PetPolicy } from './type';
import axios from 'axios';

const StyledForm = styled.form`
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 20px;
    padding: 20px;
    border: 0.5px solid black;
    border-radius: 5px;
    background-color: white;
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.2);
`;

const Button = styled.button`
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    &:hover {
        background-color: #45a049;
    }
`;

const Form: React.FC = () => {

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const data = {
            location,
            minPrice,
            maxPrice,
            pets,
            selectedDate
        };

        try {
            const response = await axios.post('http://localhost:8000/process-data/', data);
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const [location, setLocation] = useState<string>('');
    const onLocationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        setLocation(e.target.value);
    }

    const [minPrice, setMinPrice] = useState<number | null>(null);
    const [maxPrice, setMaxPrice] = useState<number | null>(null);
    const onMinPriceChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setMinPrice(parseInt(e.target.value));
    }

    const onMaxPriceChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setMaxPrice(parseInt(e.target.value));
    }

    const [pets, setPets] = useState<PetPolicy>('No pets allowed');
    const onPetsChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setPets(e.target.value as PetPolicy);
    }

    const [selectedDate, setSelectedDate] = useState<Date | null>(null);
    const handleDateChange = (date: Date | null) => {
        setSelectedDate(date);
    };

    const [email, setEmail] = useState('');
    const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setEmail(e.target.value);
    };


    return (
        <StyledForm onSubmit={handleSubmit}>
            <Location value={location} onChange={onLocationChange}/>
            <Price 
                minPrice={minPrice} 
                maxPrice={maxPrice} 
                onMinPriceChange={onMinPriceChange} 
                onMaxPriceChange={onMaxPriceChange}/>
            <Date selectedDate={selectedDate} onChange={handleDateChange}/>
            <Pets value={pets} onChange={onPetsChange}/>
            <Mail email={email} handleEmailChange={handleEmailChange}/>
            <Button type="submit">Submit</Button>
        </StyledForm>
    );
};

export default Form;