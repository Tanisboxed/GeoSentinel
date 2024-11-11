import React, {useRef} from 'react'
import NavBar from './components/NavBar';
import Hero from './components/Hero';
import Analytics from './components/Analytics';
import Heatmap from './components/Heatmap';
import Cards from './components/Cards';
import Footer from './components/Footer';

function App() {
  const heroRef = useRef(null);
  const analyticsRef = useRef(null);
  const heatmapRef = useRef(null);
  const cardsRef=useRef(null);
  const footerRef= useRef(null);

  const scrollToHome = () => heroRef.current?.scrollIntoView({ behavior: 'smooth'});
  const scrollToAbout = () => analyticsRef.current?.scrollIntoView({behavior: 'smooth'});
  const scrollToMap =() => heatmapRef.current?.scrollIntoView({behavior: 'smooth'});
  const scrollToFeatures = () => cardsRef.current?.scrollIntoView({ behavior: 'smooth'});
  const scrollToContact = () => footerRef.current?.scrollIntoView({ behavior: 'smooth'});
  return (
    <div>
      <NavBar 
        scrollToHome={scrollToHome}
        scrollToAbout={scrollToAbout}
        scrollToMap={scrollToMap}
        scrollToFeatures={scrollToFeatures}
        scrollToContact={scrollToContact}
      />
      <div ref={heroRef}>
        <Hero />
      </div>
      <div ref={analyticsRef}>
        <Analytics />
      </div>
      <div ref={heatmapRef}>
        <Heatmap />
      </div>
      <div ref={cardsRef}>
        <Cards />
      </div>
      <div ref={footerRef}>
        <Footer />
      </div>
    </div>
  );
}

export default App;
