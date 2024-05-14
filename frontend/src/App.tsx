import React from 'react';
import './App.css';
import styled from 'styled-components';


const Background = styled.div`
  background-color: #f0f0f0;
  height: 100vh;
  display: flex;
  justify-content: center;
`;

const App: React.FC = () => {
  return (
    <Background>
      <h1>App</h1>
    </Background>
  );
}

export default App;
