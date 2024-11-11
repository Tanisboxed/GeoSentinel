import React, {useState} from 'react'
import {AiOutlineClose, AiOutlineMenu} from 'react-icons/ai'
const NavBar = ({ scrollToHome, scrollToAbout, scrollToMap, scrollToFeatures, scrollToContact}) => {
    const [nav, setNav] = useState(false)

    const handleNav = () =>{
        setNav(!nav)
    }
  return (
    <div className="bg-[#000300] sticky top-0 z-1000">
    <div className='flex justify-between items-center h-24 max-w-[1240px] mx-auto px-4 text-white'>
        <h1 className='w-full text-3xl font-bold mx-auto text-[#00df9a] p-3'>GeoSentinel.</h1>
        <ul className='hidden md:flex'>
            <li className='p-4 cursor-pointer' onClick={scrollToHome}>Home</li>
            <li className='p-4 cursor-pointer' onClick={scrollToAbout}>About</li>
            <li className='p-4 cursor-pointer' onClick={scrollToMap}>Map</li>
            <li className='p-4 cursor-pointer' onClick={scrollToFeatures}>Features</li>
            <li className='p-4 cursor-pointer' onClick={scrollToContact}>Contact</li>
        </ul>
        <div onClick={handleNav} className='block md:hidden'>
            {nav ? <AiOutlineClose size={20}/>: <AiOutlineMenu size={20} /> }
        </div>
        <div className={nav? 'fixed left-0 top-0 w-[60%] h-full border-r border-r-gray-900 bg-[#000300] ease-in-out duration-500' : 'fixed left-[-100%] ease-out duration-500'}>
            <h1 className='w-full text-3xl font-bold text-[#00df9a] m-4'>GeoSentinel.</h1>
            <ul className=' uppercase p-4'>
                <li className='p-4 border-b border-gray-700 cursor-pointer' onClick={() =>{ handleNav(); scrollToHome();}}>Home</li>
                <li className='p-4 border-b border-gray-700 cursor-pointer' onClick={() =>{ handleNav(); scrollToAbout(); }}>About</li>
                <li className='p-4 border-b border-gray-700 cursor-pointer' onClick={() =>{ handleNav(); scrollToMap();}}>Maps</li>
                <li className='p-4 border-b border-gray-700 cursor-pointer' onClick={() =>{ handleNav(); scrollToFeatures();}}>Features</li>
                <li className='p-4 cursor-pointer' onClick={() =>{ handleNav(); scrollToContact();}}>Contact</li>
            </ul>
        </div>
    </div>
    </div>
  )
}

export default NavBar