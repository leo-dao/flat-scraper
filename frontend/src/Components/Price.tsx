import React from "react";
import styled from "styled-components";

interface PriceProps {
    minPrice?: number;
    maxPrice?: number;
    onMinPriceChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    onMaxPriceChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Container = styled.div`
    display: flex;
    gap: 5px;
    align-items: center;
`;

const PriceInput = styled.input`
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 5px;
`;

const Price: React.FC<PriceProps> = ({minPrice, maxPrice, onMaxPriceChange, onMinPriceChange}) => {
    return (
        <Container>
            From:
            <PriceInput
                type="number"
                placeholder="Min price"
                value={minPrice}
                onChange={onMinPriceChange}
            />
            To:
            <PriceInput
                type="number"
                placeholder="Max price"
                value={maxPrice}
                onChange={onMaxPriceChange}
            />
        </Container>
    );
};

export default Price;