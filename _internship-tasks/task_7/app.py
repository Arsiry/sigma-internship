from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanAbsoluteError


# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model
model = load_model('trained_model.h5', custom_objects={'mae': MeanAbsoluteError()})


# Define the route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON data from the request
        json_data = request.get_json()

        # Convert the JSON data to a pandas DataFrame
        input_data = pd.DataFrame(json_data)

        # Make predictions using the model
        predictions = model.predict(input_data)

        # Convert the predictions to a list and return them as a JSON response
        return jsonify({'predictions': predictions.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5001)