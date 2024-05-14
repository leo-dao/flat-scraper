import React, { useState } from 'react';
import styled from 'styled-components';
import Date from './Date';
import Location from './Location';
import Radio from './Radio';
import Text from './Text';


const Form: React.FC = () => {

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
    };
    return (
        <form onSubmit={handleSubmit}>
            <button type="submit">Submit</button>
        </form>
    );
};

export default Form;