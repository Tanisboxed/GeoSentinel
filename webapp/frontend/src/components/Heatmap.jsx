import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import 'leaflet.heat';

const HeatmapLayer = ({ points, color }) => {
  const map = useMap();

  useEffect(() => {
    if (points.length > 0) {
      const heatLayer = L.heatLayer(points, {
        radius: 25,
        blur: 15,
        maxZoom: 10,
        gradient: { 0.4: color, 0.65: color, 1.0: color }
      }).addTo(map);

      return () => map.removeLayer(heatLayer);
    }
  }, [map, points, color]);

  return null;
};

const Heatmap = () => {
  const [data, setData] = useState({ politicalMilitia: [], stateForces: [], externalForces: [] });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/predict', { method: 'POST' });
        
        if (response.ok) {
          const result = await response.json();
          setData({
            politicalMilitia: result.politicalMilitia.map(item => [item[0], item[1], 0.5]),
            stateForces: result.stateForces.map(item => [item[0], item[1], 0.5]),
            externalForces: result.externalForces.map(item => [item[0], item[1], 0.5])
          });
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="w-full h-full bg-[#000300] py-4 px-4">
      <h1 className="text-white font-bold justify-center text-center p-6 text-4xl">Crisis Heatmap</h1>
      <div className="w-full h-96 bg-gray-100 rounded-lg shadow-md mx-auto relative mt-6">
        <MapContainer center={[0, 0]} zoom={2} scrollWheelZoom={false} className="w-full h-full z-10">
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
          <HeatmapLayer points={data.politicalMilitia} color="yellow" />
          <HeatmapLayer points={data.stateForces} color="orange" />
          <HeatmapLayer points={data.externalForces} color="red" />
        </MapContainer>

        {/* Legend */}
        <div className="absolute top-4 right-4 bg-white bg-opacity-75 p-3 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold">Category Legend</h3>
          <div className="flex flex-col space-y-2 mt-2">
            <div className="flex items-center space-x-2">
              <div className="w-6 h-6 bg-yellow-500 rounded-full"></div>
              <span>Political Militia</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-6 h-6 bg-orange-500 rounded-full"></div>
              <span>State Forces</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-6 h-6 bg-red-500 rounded-full"></div>
              <span>External Forces</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Heatmap;
