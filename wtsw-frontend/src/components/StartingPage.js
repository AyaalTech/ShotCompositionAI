function StartingPage() {
    return (
        <div className="starting-page" style={{height: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center', marginLeft: '12vw'}}>
            <div style={{background: `radial-gradient(circle, rgb(20,99,243) 0%, rgb(204,208,216) 77%)`}}>    
                <h1 style={{fontFamily: "'Obrazec 2.0'", fontSize: '4em'}}>Why This Shot <span style={{textDecoration: 'underline'}}>Works?</span></h1>
                <p style={{fontFamily: "'Covid19'", fontSize: '2em'}}>Discover the secrets behind great cinematography with WTSW</p>
            </div>
            <p style={{fontFamily: "'Raleway'", fontSize: '1.2em', marginTop: '2em', width: '75vw'}}>Upload the shot you are interested in and AI will reveal its secrets. Explore the impact of various cinematographic elements such as Focal Length, Lighting Temperature, Aperture, Focus Distance, Shot Type, ISO, INT/EXT settings, Camera Model, Composition Techniques, Filter Used, and Lens on achieving the perfect shot.</p>
        </div>
    );
}

export default StartingPage;