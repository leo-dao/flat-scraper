import React from 'react';
import './App.css';
import styled from 'styled-components';
import Form from './Components/Form';

const Background = styled.div`
  background-color: #f0f0f0;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const App: React.FC = () => {
  return (
    <Background>
      <h1>Flat Scraper</h1>
      <Form />
    </Background>
  );
}

export default App;
