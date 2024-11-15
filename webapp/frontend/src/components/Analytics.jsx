import React from 'react'
import Laptop from '../assets/laptop.jpg'

function Analytics() {
  return (
    <div className='w-full bg-white py-16 px-4'>
        <div className='max-w-[1240px] mx-auto grid md:grid-cols-2'>
            <img className='w-[500px] mx-auto my-4' src={Laptop} alt="/" />
            <div className='flex flex-col justify-center'>
                <h1 className='md:text-4xl sm:text-3xl text-3xl font-bold py-2'>Real-Time Crisis Mapping</h1>
                <p>GeoSentinel is a real-time crisis mapping platform that tracks global 
                    emergencies by aggregating data from various sources. It uses machine
                    learning to filter and process information on conflicts, military 
                    movements, and civilian gatherings, providing decision-makers with 
                    timely insights for quick action.</p>
                <button className='bg-black w-[200px] rounded-md font-medium mx-auto md:ml-0 my-6 py-3 text-white'>Get Started</button>
            </div>
        </div>
    </div>
  )
}

export default Analytics