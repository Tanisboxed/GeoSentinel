import React from 'react'
import { ReactTyped } from "react-typed"

const Hero = () => {
  return (
    <div className='text-white'>
        <div className='mx-w-[600px] mt-[-85px] w-full h-screen mx-auto px-10 text-center flex flex-col justify-center '>
            <p className='text-[#00df9a] text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-bold px-6 text-left font-custom'>GEOSENTINEL</p>
            <h1 className='md:text-5xl sm:text-4xl text-4xl font bold md:py-3 px-7 text-left'>Navigating Crisis with Precision.</h1>
            <div className='flex justify-left text-4xl items-center px-4'>
                <p className='md:text-4xl sm:text-3xl text-xl font-bold px-4 py-2'>Keep track of</p>
                <ReactTyped className='md:text-4xl sm:text-3xl text-xl font-bold md:pl-1'
                    strings={['Wars.','Military.','Civilians.']} 
                    typeSpeed={120} 
                    backSpeed={140} loop 
                    />
            </div>
            <div className="flex justify-start gap-4">
              <button className="bg-white w-[200px] rounded-md font-medium ml-8 my-6 py-3 text-black">
                See it in Action
              </button>
              <button className="w-[200px] rounded-md font-medium my-6 py-3 text-white border border-white bg-transparent">
                Learn More
              </button>
            </div>

        </div>
    </div>
  )
}

export default Hero