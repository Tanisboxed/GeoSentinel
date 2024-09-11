# GeoSentinel: Real-Time Conflict Surveillance and Crisis Mapping

GeoSentinel is an advanced system for real-time conflict surveillance and crisis mapping using satellite imagery and conflict event data.

## Features

- Real-time data collection from satellite imagery APIs and conflict databases
- Machine learning-based classification of conflict events
- Interactive global heatmap for visualizing conflict intensity
- Continuous updates based on incoming data

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/GeoSentinel.git
   cd GeoSentinel
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database (PostgreSQL):
   ```
   createdb geosentinel
   ```

4. Set up environment variables (API keys, database URL, etc.) in a `.env` file.

5. Run the data collection scripts:
   ```
   python scripts/fetch_satellite_data.py
   python scripts/fetch_conflict_data.py
   ```

6. Train the model:
   ```
   python models/conflict_classifier.py
   ```

7. Start the Flask backend:
   ```
   python webapp/backend/server.py
   ```

8. Start the React frontend:
   ```
   cd webapp/frontend
   npm install
   npm start
   ```

## Usage

Navigate to `http://localhost:3000` in your web browser to view the GeoSentinel dashboard.

## Contributing
We welcome contributions from the community. 

## Acknowledgements
Thanks to the contributors and researchers whose work has paved the way for advancements in transfer learning and event classification. Special thanks to the open-source communities for their tools and libraries that make this project possible.
