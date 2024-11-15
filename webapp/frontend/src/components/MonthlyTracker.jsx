import React, { useEffect, useState } from 'react'
import axios from 'axios'

const MonthlyTracker = () => {
  const [data, setData] = useState('')

  useEffect(() => {
    axios.get('http://localhost:5000/monthly-tracker')
      .then(response => setData(response.data))
      .catch(error => console.log(error))
  }, [])

  return (
    <div>
      <h1>Monthly Tracker Data</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}

export default MonthlyTracker
