import ScrollToTop from './ScrollToTop';
import './NavBar.css';

const Navbar = () => {
  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <nav className="navbar">
      <ScrollToTop />
      <div className="nav-items">
        <span onClick={() => scrollToSection('section1')}>Lorem</span>
        <span onClick={() => scrollToSection('section2')}>Ipsum</span>
        <span onClick={() => scrollToSection('section3')}>Dorem</span>
      </div>
    </nav>
  );
};

export default Navbar;