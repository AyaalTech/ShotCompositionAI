import React, { useState } from 'react';
import Navbar from './components/NavBar';
import StartingPage from './components/StartingPage';
import UploadPage from './components/UploadPage';
import OutputPage from './components/OutputPage';

function App() {
  const [hasUploaded, setHasUploaded] = useState(false);
  const [responseData, setResponseData] = useState(null);

  return (
    <div className="App">
      <div style={{ display: 'flex', flexDirection: 'column', height: 'fitContent', scrollBehavior: 'smooth'}}>
        <Navbar />
        <div id="section1"><StartingPage /></div>
        <div id="section2">
          <UploadPage setHasUploaded={setHasUploaded} setResponseData={setResponseData} />
        </div>
        <div id="section3">
          <OutputPage hasUploaded={hasUploaded} responseData={responseData} />
        </div>
        <img src="/tarkovsky.png" alt="director" style={{ position: 'sticky', bottom: '0', left: '100vw', width: '15vw', zIndex: 10 }} />
      </div>
    </div>
  );
}

export default App;
