import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const Heatmap = () => {
  const [heatmapData, setHeatmapData] = useState(null);

  useEffect(() => {
    // Fetch heatmap data from backend
    const fetchData = async () => {
      // Simulate fetching data
      // const response = await fetch('/your-backend-api-endpoint');
      // const data = await response.json();
      // setHeatmapData(data);  // Example data: [[lat, lng, intensity], ...]

      // For now, we'll simulate no data, and the map will load with no heatmap layer
      // setHeatmapData([]);
    };

    fetchData();

    // Optionally, set up an interval for real-time updates
    const interval = setInterval(fetchData, 5000); // Update every 5 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="w-full h-full bg-[#000300] py-4 px-4">
      <h1 className='text-white font-bold justify-center text-center p-6 text-4xl'>Crisis Heatmap</h1> 
      <div className="w-full h-96 bg-gray-100 rounded-lg shadow-md mx-auto relative mt-6">
        <MapContainer center={[0, 0]} zoom={2} scrollWheelZoom={false} className="w-full h-full z-10">
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {/* If you have data, you can add a heatmap layer */}
          {/* {heatmapData && <L.heatLayer data={heatmapData} radius={25} blur={15} />} */}
        </MapContainer>

        {/* Legend Box */}
        <div className="absolute top-4 right-4 bg-white bg-opacity-75 p-3 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold">Category Legend</h3>
          <div className="flex flex-col space-y-2 mt-2">
            <div className="flex items-center space-x-2">
              <div className="w-6 h-6 bg-red-500 rounded-full"></div>
              <span>War Conflict</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-6 h-6 bg-orange-500 rounded-full"></div>
              <span>Military Movement</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-6 h-6 bg-yellow-500 rounded-full"></div>
              <span>Civilian Gathering</span>
            </div>
          </div>
        </div>
      </div>
      <div className='w-full py-8 text-white px-4'>
        <div className='max-w-[1240px] mx-auto grid lg:grid-cols-3'>
          <div className='lg:col-span-2'>
            <h1 className='md:text-2xl sm:text-xl text-xl font-bold py-1'>Want to search by Country?</h1>
            <p className='text-gray-500 py-2'>Please enter country name.</p>
          </div>
          <div className='flex flex-col sm:flex-row items-center justify-between w-full'>
            <input className='p-3 flex w-full rounded-md text-black px-4' type="text" placeholder='Enter country name' />
            <button className='bg-[#00df9a] w-[100px] rounded-md font-medium ml-4 my-6 px-6 py-3 text-black '>Search</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Heatmap;
