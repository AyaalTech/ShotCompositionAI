import './NavBar.css';

const Navbar = () => {
  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ block: 'end',  behavior: 'smooth' });
    }
  };

  return (
    <nav className="navbar">
      <img src="/wtsw.png" alt="WT Logo" style={{ width: '3rem' }} />
      <span onClick={() => scrollToSection('section1')}>Starting</span>
      <span onClick={() => scrollToSection('section2')}>Upload</span>
      <span onClick={() => scrollToSection('section3')}>Analysis</span>
      <span onClick={() => scrollToSection('section4')}>Guides</span>
    </nav>
  );
};

export default Navbar;