import React, { useEffect, useState } from 'react'
import axios from 'axios'

const CrisisIndex = () => {
  const [data, setData] = useState('')

  useEffect(() => {
    axios.get('http://localhost:5000/crisis-index')
      .then(response => setData(response.data))
      .catch(error => console.log(error))
  }, [])

  return (
    <div>
      <h1>Crisis Index Data</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  )
}

export default CrisisIndex
