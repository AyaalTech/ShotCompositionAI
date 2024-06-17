import React, { useState } from 'react';
import axios from 'axios';

function UploadPage() {
  const [image, setImage] = useState(null);

  const handleImageChange = (event) => {
    setImage(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('Predictions:', response.data);

    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  return (
    <div className="upload-page" style={{ height: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', gap: '2vh'}}>
      <h1 style={{fontFamily: "'Obrazec 2.0'", fontSize: '3em'}}>Upload An Image</h1>
      <p style={{fontFamily: "'Covid19'", fontSize: '2em'}}>for ai to think about</p>
      <form onSubmit={handleSubmit} style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center'}}>
        <label htmlFor="file-upload" style={{cursor: 'pointer', marginBottom: '1vh', fontFamily: "'Raleway'", padding: '10px 20px', backgroundColor: '#1463F3', color: '#CCD0D8', border: 'none', borderRadius: '5px'}}>
            📂 Browse Files
        </label>
        <input id="file-upload" type="file" accept="image/*" onChange={handleImageChange} style={{display: 'none'}} />
        <button type="submit" style={{fontFamily: "'Raleway'", width: '12vw', padding: '10px 20px', fontSize: '1em', backgroundColor: '#1D2023', color: '#CCD0D8', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>🦾 Upload</button>
      </form>
    </div>
  );
}

export default UploadPage;
