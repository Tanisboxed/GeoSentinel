
# **WarLens: Real-Time Conflict Surveillance System** 🗺️

## **Overview**
**WarLens** is a real-time conflict surveillance and crisis analysis platform that provides actionable insights into global conflict zones. By integrating data from sources like the **ACLED conflict event database** , WarLens offers a comprehensive view of ongoing crises. The project automates data collection, classification, and visualization, aiming to assist decision-makers in understanding and responding to conflict scenarios effectively.

## **Key Features**
### 1. **Interactive Heatmap**
   - Visualizes global conflict hotspots using **Leaflet.js**.
   - Displays real-time data on military movements, war conflicts, and civilian gatherings.
   - Provides interactive navigation and zoom capabilities for detailed region analysis.

### 2. **Monthly Tracker**
   - Summarizes conflict data for the current month, showcasing:
     - **Total Number of Conflicts**
     - **Crisis Index**: A ranking of countries based on conflict intensity.
   - Offers insights into emerging crisis zones by analyzing recent conflict trends.

### 3. **Country Ranking System**
   - Ranks countries based on the **Crisis Index**, reflecting the severity of conflict events.
   - Highlights high-risk areas, aiding in quick decision-making and prioritization.

### 4. **Civilian Gatherings Analysis**
   - Categorizes civilian gatherings into different types (e.g., protests, rallies).
   - Provides a detailed analysis of gatherings to identify potential areas of unrest.
   - Users can filter events based on type, helping to understand the social dynamics of specific regions.

### 5. **Automated Data Collection and Processing**
   - Integrates with the **ACLED API** for real-time conflict data fetching.
   - Features an automated ETL (Extract, Transform, Load) pipeline for data preprocessing and cleaning.

## **Technology Stack**
### **Frontend**
- **ReactJS**: For building a dynamic, responsive user interface.
- **Tailwind CSS**: For efficient, utility-first styling.
- **Leaflet.js**: For interactive map visualization.

### **Backend**
- **Flask**: For API handling, data processing, and serving the frontend.
- **Python**: For data processing, feature extraction, and ML model integration.

### **Database**
- **SQLite**: Lightweight database for storing preprocessed data and ML model outputs.

### **Machine Learning**
- **Convolutional Neural Networks (CNN)** for conflict event classification. 

## **Installation and Setup**

### **Prerequisites**
- Node.js and npm
- Python 3.8+
- Flask
- SQLite

### **Clone the Repository**
```bash
git clone https://github.com/TanishaJauhari/WarLens.git
cd WarLens/webapp
