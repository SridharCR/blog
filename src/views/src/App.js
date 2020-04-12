import React from 'react';
import logo from './logo.svg';
import './App.css';
import SimplePost from './atoms/SimplePost';
import Header from './atoms/Header';

function App() {
  return (
    <div className="App">
        <Header />
        <SimplePost />
    </div>
  );
}

export default App;
