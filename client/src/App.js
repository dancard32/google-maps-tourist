import logo from './logo.svg';
import React, {useState, useEffect} from 'react';
import './App.css';


function App() {

 

  return (
    <div className="App">
      <header className="App-header">
        <p>Google Maps - Tourist Routes</p>
      </header>

      <div className='form'>
        <form action='/' method='post'>
          <div>
            <label>Starting Location:</label>
            <input type='text' name='starting_location' required/>
          </div>
    
          <div>
            <label>Ending Location:</label>
            <input type='text' name='ending_location' required/>
          </div>

          <br/>
          <input type='submit'/>
        </form>
      </div>

      
      <iframe src="../map.html" width="75%" height="500vh" allowFullScreen="" loading="lazy"></iframe>

      <br/>
      <div>
        <a>Made with ❤️ by Dan</a>
        <br></br>
        <a href='https://github.com/dancard32' target="_blank" rel="noopener noreferrer">
        Check me out on github!</a>
      </div>
      
    </div>
  );
}

export default App;
