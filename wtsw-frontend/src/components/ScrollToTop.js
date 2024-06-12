import React from 'react';
import './ScrollToTop.css';

const ScrollToTop = () => {
    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };

    return (
        <div className="scroll-to-top" onClick={scrollToTop}>
            <img src="/wtsw.png" alt="Scroll to top" />
        </div>
    );
};

export default ScrollToTop;