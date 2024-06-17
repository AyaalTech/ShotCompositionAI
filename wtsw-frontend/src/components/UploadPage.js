import React, { useState } from 'react';
import axios from 'axios';

function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);

    const handleImageChange = event => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = async event => {
        event.preventDefault();
        if (!selectedFile) {
            alert("Please select an image");
            return;
        }
        try {
            const formData = new FormData();
            formData.append('file', selectedFile);
            const response = await axios.post('http://localhost:5000/predict', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
  };

  return (
    <div className="upload-page" style={{ height: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', gap: '2vh', background: `radial-gradient(circle, rgb(20,99,243) 0%, rgb(204,208,216) 20%)`}}>
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
