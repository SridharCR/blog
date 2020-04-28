import React from 'react';
import './App.css';
import Routes from './atoms/Routes';
import Header from './atoms/Header';
import Button from './atoms/Button';

function App() {
  return (
    <div className="App" >
        <Header />
        <Routes/>
        <Button />
    </div>
  );
}

export default App;
