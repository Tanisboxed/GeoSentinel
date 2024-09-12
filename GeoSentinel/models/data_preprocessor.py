import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class DataPreprocessor:
    def __init__(self):
        self.preprocessor = None 
    
    def fit_transform(self, X):
        numeric_features = ['latitude','longitude','cloud_cover']
        categorical_features = ['event_type','actor1','actor2','location']
        text_features = ['notes']
        self.preprocessor = ColumnTransformer(
            transformer=[
                ('num', StandardScaler(), numeric_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
                ('text','passthrough', text_features)
            ]
        )
        return self.preprocessor.fit_transform(X)

    def transform(self, X):
        if self.preprocessor is None:
            raise ValueError("Preprocessor has not been fitted. Call fit_transform.")
        return self.preprocessor.transform(X)

def load_and_merge_data():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    satellite_data = pd.read_sql("SELECT * FROM satellite_data", conn)
    conflict_data = pd.read_sql("SELECT * FROM conflict_data",conn)

    conn.close()

    merged_Data = pd.merge_asof(
        satellite_data.sort_values('acquired'),
        conflict_data.sort_values('event_date'),
        left_on= 'acquired',
        right_on= 'event_date',
        tolerance= pd.Timedelta('1d'),
        direction='nearest'
    )
    
    merged_data= merged_data.dropna(subset=['event_id'])
    return merged_data 

if __name__ == "__main__":
    data = load_and_merge_data()
    preprocessor = DataPreprocessor()
    X = data[['latitude','longitude','cloud_cover','event_type','actor1','actor2','location', 'notes']]
    X_processed = preprocessor.fit_transform(X)
    print(f"Processed data shape: {X_processed.shape}")
