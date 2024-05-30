import React, { useState } from 'react';
import styled from 'styled-components';

interface MailProps {
    email: string;
    handleEmailChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Input = styled.input`
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    font-size: 16px;
    outline: none;
    &:focus {
        transition: 0.2s;
        border-color: blue;
    }
`;

const Mail = (props: MailProps) => {

    return (
        <Input
            type="email"
            id="email"
            value={props.email}
            onChange={props.handleEmailChange}
            placeholder='Email Address'
        />
    );
};

export default Mail;