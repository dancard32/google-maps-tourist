import logo from './logo.svg';
import React, {useState, useEffect} from 'react';
import './App.css';


function App() {

  const [data, setData] = useState([{}])
  
  useEffect(() => {
    fetch("/api").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>

      <div>
        {(typeof data.members === 'undefined') ? (
            <p>Loading...</p>
        ) :(
          data.members.map((member, i) => (
            <p key={i}>{member}</p>
          ))
        )}
      </div>
    </div>
  );
}

export default App;
