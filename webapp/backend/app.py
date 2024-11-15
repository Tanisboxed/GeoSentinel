import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
from predict_from_data import predict_output
import data_reader

app = Flask(__name__)

CORS(app) 



@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        data = request.json
        
        result = predict_output(data)
        return jsonify({"message": "Data submitted successfully", "prediction": result}), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500
    
@app.route("/", methods=["GET"])
def homePage():
    data= {
        "success":True,
        "message": 'welcome to the homepage'
    }
    return jsonify(data) , 200


@app.route("/predict", methods=["POST"])
def predict():
     
    from data_reader import political_militia_data,state_forces_data,external_forces_data
    return jsonify({
        "politicalMilitia": political_militia_data,
        "stateForces": state_forces_data,
        "externalForces": external_forces_data
    }), 200
    

from flask import send_file
import pandas as pd

@app.route('/monthly-tracker', methods=["GET"])
def monthly_tracker():
    # Call the number_conflict function
    result_df = data_reader.number_conflict()

    # Save the result DataFrame to a CSV file
    result_df.to_csv('monthly_tracker.csv', index=False)

    # Send the CSV file for download
    return send_file('monthly_tracker.csv', as_attachment=True)


@app.route('/crisis-index', methods=["GET"])
def crisis_index():
    crisis_count_by_country, ranked_countries = data_reader.rank_countries()

    # Save the data to a CSV file
    crisis_count_df = pd.DataFrame(crisis_count_by_country).reset_index()
    ranked_countries_df = pd.DataFrame(ranked_countries).reset_index()

    crisis_count_df.to_csv('crisis_count_by_country.csv', index=False)
    ranked_countries_df.to_csv('ranked_countries.csv', index=False)

    # Send the CSV for download
    return send_file('crisis_count_by_country.csv', as_attachment=True)

@app.route('/civilian-gathering', methods=["GET"])
def civilian_tracking():
    ranked_countries_by_total, ranked_countries_by_protests = data_reader.rank_by_civilian_gatherings()

    # Save the data to a CSV file
    total_gatherings_df = pd.DataFrame(ranked_countries_by_total).reset_index()
    protests_df = pd.DataFrame(ranked_countries_by_protests).reset_index()

    total_gatherings_df.to_csv('ranked_by_total_gatherings.csv', index=False)
    protests_df.to_csv('ranked_by_protests.csv', index=False)

    # Send the CSV for download
    return send_file('ranked_by_total_gatherings.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    
# 1. rank countries based on montly events, 
# 2. calculates total civialian gatherings,
# 3. tracker: monthly events tracker sorts.