import Navbar from './components/NavBar';
import UploadPage from './components/UploadPage';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div style={{ height: '100vh', overflowY: 'scroll' }}>
        <UploadPage />
        <UploadPage />
      </div>
      <img src="/tarkovsky.png" alt="director" style={{ position: 'sticky', bottom: '0', left: '100vw', width: '15rem', zIndex: 10 }} />
    </div>
  );
}

export default App;
