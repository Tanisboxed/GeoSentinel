import React, { useState, useEffect } from 'react'
import axios from 'axios'
import calculator from '../assets/calculator.jpg'
import people from '../assets/people.jpg'
import worldcc from '../assets/worldcc.png'

const Cards = () => {
  const [monthlyTrackerData, setMonthlyTrackerData] = useState('')
  const [crisisIndexData, setCrisisIndexData] = useState('')
  const [civilianGatheringsData, setCivilianGatheringsData] = useState('')

  const fetchData = (endpoint, setter) => {
    axios
      .get(`http://localhost:5000/${endpoint}`, { responseType: 'blob' })
      .then((response) => {
        const file = new Blob([response.data], { type: response.headers['content-type'] })
        const fileURL = URL.createObjectURL(file)
        setter(fileURL)
      })
      .catch((error) => console.log(error))
  }

  useEffect(() => {
    fetchData('monthly-tracker', setMonthlyTrackerData)
    fetchData('crisis-index', setCrisisIndexData)
    fetchData('civilian-gathering', setCivilianGatheringsData)
  }, [])

  const downloadFile = (fileURL, filename) => {
    const link = document.createElement('a')
    link.href = fileURL
    link.download = filename
    link.click()
  }

  return (
    <div className='w-full py-[10rem] px-16 bg-white'>
      <div className='max-w-[1240px] mx-auto grid md:grid-cols-3 gap-8'>
        <div className='w-full shadow-xl flex flex-col p-4 my-4 rounded-lg hover:scale-105 duration-300'>
          <img className='w-20 mx-auto mt-[-3rem] bg-white' src={calculator} alt="/" />
          <h2 className='text-2xl font-bold text-center py-2'>Monthly Tracker</h2>
          <p className='text-center text-xl py-1'>No. of conflicts this month</p>
          <button
            onClick={() => downloadFile(monthlyTrackerData, 'monthly-tracker.csv')}
            className='bg-black text-white w-[200px] rounded-md font-medium my-6 mx-auto px-6 py-3 '
          >
            Download
          </button>
        </div>
        <div className='w-full shadow-xl bg-gray-50 flex flex-col p-4 md:my-0 my-8 rounded-lg hover:scale-105 duration-300'>
          <img className='w-20 mx-auto mt-[-3rem]' src={worldcc} alt="/" />
          <h2 className='text-2xl font-bold text-center py-2'>Crisis Index</h2>
          <p className='text-center text-xl py-1'>Ranking countries</p>
          <button
            onClick={() => downloadFile(crisisIndexData, 'crisis-index.csv')}
            className='w-[200px] rounded-md font-medium my-6 mx-auto px-6 py-3 text-black border-2 border-black bg-transparent '
          >
            Download
          </button>
        </div>
        <div className='w-full shadow-xl flex flex-col p-4 my-4 rounded-lg hover:scale-105 duration-300'>
          <img className='w-20 mx-auto mt-[-3rem] bg-white' src={people} alt="/" />
          <h2 className='text-2xl font-bold text-center py-2'>Civilian Gatherings</h2>
          <p className='text-center text-xl py-1'>Type of Gatherings</p>
          <button
            onClick={() => downloadFile(civilianGatheringsData, 'civilian-gatherings.csv')}
            className='bg-black text-white w-[200px] rounded-md font-medium my-6 mx-auto px-6 py-3 '
          >
            Download
          </button>
        </div>
      </div>
    </div>
  )
}

export default Cards
