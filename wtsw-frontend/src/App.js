import Navbar from './components/NavBar';

function App() {
  return (
    <div className="App">
      <Navbar />
      <img src="/tarkovsky.png" alt="director" style={{ position: 'absolute', right: 0, bottom: 0, height: '15rem' }} />
    </div>
  );
}

export default App;
