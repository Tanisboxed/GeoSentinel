import React, { useState } from 'react';
import axios from 'axios';

function FormComponent() {
  const initialData = {
    event_id_cnty: '', event_date: '', year: '', time_precision: '',
    disorder_type: '', event_type: '', sub_event_type: '', actor1: '',
    assoc_actor_1: '', inter1: '', actor2: '', assoc_actor_2: '', inter2: '',
    interaction: '', civilian_targeting: '', iso: '', region: '', country: '',
    admin1: '', admin2: '', admin3: '', location: '', latitude: '', longitude: '',
    geo_precision: '', source: '', source_scale: '', notes: '', fatalities: '',
    tags: '', timestamp: ''
  };
  
  const requiredFields = [
    'year', 'disorder_type', 'event_type', 'actor1', 'actor2', 
    'region', 'location', 'latitude', 'longitude', 'geo_precision', 
    'source', 'timestamp'
  ];

  const [formData, setFormData] = useState(initialData);
  const [popupMessage, setPopupMessage] = useState('');
  const [showPopup, setShowPopup] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/submit-form', formData);
      setPopupMessage(response.data.message || 'Data submitted successfully');
      setShowPopup(true);
    } catch (error) {
      setPopupMessage('Error submitting data');
      setShowPopup(true);
    }
  };

  const closePopup = () => setShowPopup(false);

  return (
    <div className="bg-gray-100 p-6 rounded-lg shadow-md mt-3">
      <form onSubmit={handleSubmit} className="space-y-4">
        <h2 className="text-2xl font-bold text-center text-gray-700 mb-6">Submit Data to Us</h2>
        {Object.keys(initialData).map((key) => (
          key === 'event_date' ? (
            <div key={key} className="flex flex-col">
              <label className="text-gray-600 font-semibold mb-1">
                {key.replace('_', ' ')}{requiredFields.includes(key) && <span className="text-red-500">*</span>}:
              </label>
              <input
                type="datetime-local"
                name={key}
                value={formData[key]}
                onChange={handleChange}
                className="border rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                required={requiredFields.includes(key)}
              />
            </div>
          ) : (
            <div key={key} className="flex flex-col">
              <label className="text-gray-600 font-semibold mb-1">
                {key.replace('_', ' ')}{requiredFields.includes(key) && <span className="text-red-500">*</span>}:
              </label>
              <input
                type="text"
                name={key}
                value={formData[key]}
                onChange={handleChange}
                className="border rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                required={requiredFields.includes(key)}
              />
            </div>
          )
        ))}
        <button type="submit" className="w-full bg-blue-500 text-white font-semibold p-2 rounded-md hover:bg-blue-600">
          Submit data to predict
        </button>
      </form>

      {showPopup && (
        <div className="fixed inset-0 flex justify-center items-center bg-gray-800 bg-opacity-50 z-50">
          <div className="bg-white p-6 rounded-lg shadow-md w-96">
            <h3 className="text-xl font-semibold text-gray-700 mb-4">Submission Status</h3>
            <p className="text-gray-600 mb-4">{popupMessage}</p>
            <div className="flex justify-end">
              <button 
                className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600" 
                onClick={closePopup}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default FormComponent;
