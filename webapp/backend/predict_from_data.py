import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf

base_path = os.getcwd()
print(base_path)

model_path = os.path.abspath( os.path.join(base_path,'..','..', 'models',"geosentinel_cnn_model.h5" ))
print(model_path)
model = tf.keras.models.load_model(model_path)


import numpy as np

def preprocess_data(input_data):

  processed_data = []

  numerical_features = [
      'year', 'latitude', 'longitude', 'geo_precision', 'fatalities'
  ]

  for feature in numerical_features:
    processed_data.append(input_data[feature] / 100)

  categorical_features = [
      'disorder_type', 'event_type', 'actor1', 'actor2', 'region',
      'sub_event_type', 'interaction', 'source_scale'
  ]

  def one_hot_encode(value, categories):

    encoding = [0] * len(categories)
    if value in categories:
      encoding[categories.index(value)] = 1
    return encoding

  categories = {
      'disorder_type': ['Strategic developments', 'Civil Unrest', 'Protest'],
      'event_type': ['Strategic developments', 'Protest', 'Riot'],
      'actor1': ['Settlers (Israel)', 'Protesters', 'Police', 'Citizens'],
      'actor2': ['Civilians (Palestine)', 'Protesters', 'Police'],
      'region': ['Middle East', 'North America', 'Europe', 'Asia'],
      'sub_event_type': ['Looting/property destruction', 'Military action', 'Armed clashes'],
      'interaction': ['Political militia-Civilians', 'Protesters-Police'],
      'source_scale': ['Other', 'Government', 'NGO', 'UN']
  }

  for feature in categorical_features:
    processed_data.extend(one_hot_encode(input_data[feature], categories[feature]))

  if len(processed_data) > 768:
    processed_data = processed_data[:768]  

  return np.array(processed_data).reshape(1, -1)

input_data = {
  "event_id_cnty": "PSE62716",
  "event_date": "01 November 2024",
  "year": 2024,
  "time_precision": 1,
  "disorder_type": "Strategic developments",
  "event_type": "Strategic developments",
  "sub_event_type": "Looting/property destruction",
  "actor1": "Settlers (Israel)",
  "assoc_actor_1": None,
  "inter1": "Political militia",
  "actor2": "Civilians (Palestine)",
  "assoc_actor_2": None,
  "inter2": "Civilians",
  "interaction": "Political militia-Civilians",
  "civilian_targeting": None,
  "iso": 275,
  "region": "Middle East",
  "country": "Palestine",
  "admin1": "West Bank",
  "admin2": "Hebron",
  "admin3": None,
  "location": "Shi'b Al Batim",
  "latitude": 31.3942,
  "longitude": 35.1365,
  "geo_precision": 1,
  "source": "PLO Negotiations Affairs Department",
  "source_scale": "Other",
  "notes": "Land seizure: On 1 November 2024, Israeli sett...",
  "fatalities": 0,
  "tags": None,
  "timestamp": 1730758098
}

class_labels = [
    'Strategic developments', 'Protests', 'Riots',
       'Violence against civilians', 'Battles',
       'Explosions/Remote violence','Looting', 'Property Destruction', 
       'Protest', 'Military Action', 'Armed Clashes',
       'Political militia-Civilians', 'Protesters only',
       'State forces only', 'State forces-Rioters',
       'State forces-Political militia',
       'Political militia-Political militia', 'State forces-Rebel group',
       'Rioters only', 'Rebel group-Civilians', 'Civilians only',
       'Rebel group-Political militia', 'External/Other forces-Civilians',
       'External/Other forces only', 'Identity militia-Identity militia',
       'Political militia-External/Other forces',
       'Political militia only', 'Rioters-Civilians',
       'State forces-Civilians', 'State forces-Identity militia',
       'Identity militia-Civilians', 'Rioters-External/Other forces',
       'Rebel group-Rebel group', 'State forces-Protesters',
       'State forces-State forces', 'State forces-External/Other forces',
       'Identity militia only', 'Rioters-Rioters',
       'Rebel group-Identity militia',
       'External/Other forces-External/Other forces',
       'Political militia-Identity militia',
       'Rebel group-External/Other forces', 'Protesters-Protesters',
       'Protesters-External/Other forces', 'Rebel group only',
       'Rioters-Protesters', 'Political militia-Rioters',
       'Political militia-Protesters', 'Civilians-Civilians',
       'Rebel group-Protesters', 'Rebel group-Rioters',
       'Identity militia-External/Other forces',
       'Identity militia-Rioters', 'Identity militia-Protesters',
       'Political militia', 'Protesters', 'State forces', 'Rioters',
       'Rebel group', 'Civilians', 'External/Other forces',
       'Identity militia',
    'Strategic developments', 'Protests', 'Riots',
       'Violence against civilians', 'Battles',
       'Explosions/Remote violence','Looting', 'Property Destruction', 
       'Protest', 'Military Action', 'Armed Clashes',
       'Political militia-Civilians', 'Protesters only',
       'State forces only', 'State forces-Rioters',
       'State forces-Political militia',
       'Political militia-Political militia', 'State forces-Rebel group',
       'Rioters only', 'Rebel group-Civilians', 'Civilians only',
       'Rebel group-Political militia', 'External/Other forces-Civilians',
       'External/Other forces only', 'Identity militia-Identity militia',
       'Political militia-External/Other forces',
       'Political militia only', 'Rioters-Civilians',
       'State forces-Civilians', 'State forces-Identity militia',
       'Identity militia-Civilians', 'Rioters-External/Other forces',
       'Rebel group-Rebel group', 'State forces-Protesters',
       'State forces-State forces', 'State forces-External/Other forces',
       'Identity militia only', 'Rioters-Rioters',
       'Rebel group-Identity militia',
       'External/Other forces-External/Other forces',
       'Political militia-Identity militia',
       'Rebel group-External/Other forces', 'Protesters-Protesters',
       'Protesters-External/Other forces', 'Rebel group only',
       'Rioters-Protesters', 'Political militia-Rioters',
       'Political militia-Protesters', 'Civilians-Civilians',
       'Rebel group-Protesters', 'Rebel group-Rioters',
       'Identity militia-External/Other forces',
       'Identity militia-Rioters', 'Identity militia-Protesters',
       'Political militia', 'Protesters', 'State forces', 'Rioters',
       'Rebel group', 'Civilians', 'External/Other forces',
       'Identity militia',
    'Strategic developments', 'Protests', 'Riots',
       'Violence against civilians', 'Battles',
       'Explosions/Remote violence','Looting', 'Property Destruction', 
       'Protest', 'Military Action', 'Armed Clashes',
       'Political militia-Civilians', 'Protesters only',
       'State forces only', 'State forces-Rioters',
       'State forces-Political militia',
       'Political militia-Political militia', 'State forces-Rebel group',
       'Rioters only', 'Rebel group-Civilians', 'Civilians only',
       'Rebel group-Political militia', 'External/Other forces-Civilians',
       'External/Other forces only', 'Identity militia-Identity militia',
       'Political militia-External/Other forces',
       'Political militia only', 'Rioters-Civilians',
       'State forces-Civilians', 'State forces-Identity militia',
       'Identity militia-Civilians', 'Rioters-External/Other forces',
       'Rebel group-Rebel group', 'State forces-Protesters',
       'State forces-State forces', 'State forces-External/Other forces',
       'Identity militia only', 'Rioters-Rioters',
       'Rebel group-Identity militia',
       'External/Other forces-External/Other forces',
       'Political militia-Identity militia',
       'Rebel group-External/Other forces', 'Protesters-Protesters',
       'Protesters-External/Other forces', 'Rebel group only',
       'Rioters-Protesters', 'Political militia-Rioters',
       'Political militia-Protesters', 'Civilians-Civilians',
       'Rebel group-Protesters', 'Rebel group-Rioters',
       'Identity militia-External/Other forces',
       'Identity militia-Rioters', 'Identity militia-Protesters',
       'Political militia', 'Protesters', 'State forces', 'Rioters',
       'Rebel group', 'Civilians', 'External/Other forces',
       'Identity militia',
    'Strategic developments', 'Protests', 'Riots',
       'Violence against civilians', 'Battles',
       'Explosions/Remote violence','Looting', 'Property Destruction', 
       'Protest', 'Military Action', 'Armed Clashes',
       'Political militia-Civilians', 'Protesters only',
       'State forces only', 'State forces-Rioters',
       'State forces-Political militia',
       'Political militia-Political militia', 'State forces-Rebel group',
       'Rioters only', 'Rebel group-Civilians', 'Civilians only',
       'Rebel group-Political militia', 'External/Other forces-Civilians',
       'External/Other forces only', 'Identity militia-Identity militia',
       'Political militia-External/Other forces',
       'Political militia only', 'Rioters-Civilians',
       'State forces-Civilians', 'State forces-Identity militia',
       'Identity militia-Civilians', 'Rioters-External/Other forces',
       'Rebel group-Rebel group', 'State forces-Protesters',
       'State forces-State forces', 'State forces-External/Other forces',
       'Identity militia only', 'Rioters-Rioters',
       'Rebel group-Identity militia',
       'External/Other forces-External/Other forces',
       'Political militia-Identity militia',
       'Rebel group-External/Other forces', 'Protesters-Protesters',
       'Protesters-External/Other forces', 'Rebel group only',
       'Rioters-Protesters', 'Political militia-Rioters',
       'Political militia-Protesters', 'Civilians-Civilians',
       'Rebel group-Protesters', 'Rebel group-Rioters',
       'Identity militia-External/Other forces',
       'Identity militia-Rioters', 'Identity militia-Protesters',
       'Political militia', 'Protesters', 'State forces', 'Rioters',
       'Rebel group', 'Civilians', 'External/Other forces',
       'Identity militia',
       ]  # Adjust if needed


def predict_output(input_data:dict):
    processed_input = preprocess_data(input_data)

    prediction = model.predict(processed_input)

    print(f"Prediction shape: {prediction.shape}")

    predicted_class_index = np.argmax(prediction)

    if predicted_class_index < len(class_labels):
        print(f"Predicted event type: {class_labels[predicted_class_index]}")
        return class_labels[predicted_class_index]
    else:
        print(f"Predicted class index {predicted_class_index} is out of bounds.")
