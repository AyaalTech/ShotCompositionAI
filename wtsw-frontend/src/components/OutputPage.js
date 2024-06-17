import React, { useEffect, useState } from 'react';

function OutputPage({ hasUploaded, responseData }) {
  const [isLoading, setIsLoading] = useState(hasUploaded);

  useEffect(() => {
    if (hasUploaded &&!responseData) {
      setIsLoading(true);
    } else {
      setIsLoading(false);
    }
  }, [hasUploaded, responseData]);

  if (isLoading) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        Loading...
      </div>
    );
  }

  if (!responseData) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        No data available. Upload it.
      </div>
    );
  }

  const roundUpNumber = (num) => typeof num === 'number'? Math.round(num) : num;

  return (
    <div className="output-page" style={{ height: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', gap: '2vh'}}>
      <div style={{ background: 'linear-gradient(180deg, rgba(20,99,243,1) 0%, rgba(204,208,216,1) 100%)', padding: '0.5em'}}>
        <h1 style={{ fontFamily: "'Obrazec 2.0'", fontSize: '3em' }}>Analysis Results</h1>
        <p style={{ fontFamily: "'Covid19'", fontSize: '2em' }}>Here are the details of the analyzed shot:</p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', maxWidth: '800px', margin: 'auto' }}>
          {Object.entries(responseData).map(([key, value], index) => (
            <div key={index} style={{ backgroundColor: '#f9f9f9', borderRadius: '10px', padding: '1em', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
              <strong>{key}</strong>:{roundUpNumber(value)}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default OutputPage;
