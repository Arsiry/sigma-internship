import unittest
from unittest.mock import patch
from flask import json
import pandas as pd
from app import app


class TestPredictFunction(unittest.TestCase):

    def setUp(self):
        # Set up test client and application context
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Tear down the application context
        self.app_context.pop()

    @patch('app.model')  # Mocking the model object
    def test_predict(self, mock_model):
        # Arrange: prepare the input data
        test_data = {
          "site_id": {"54672": 1.3282373934, "109738": 1.3282373934},
          "ad_type_id": {"54672": -0.1803785606, "109738": -0.1803785606},
          "geo_id": {"54672": 0.2836884608, "109738": 0.6916805002},
          "device_category_id": {"54672": -1.1359721998, "109738": -1.1359721998},
          "advertiser_id": {"54672": -0.2775025908, "109738": -0.1962050096},
          "order_id": {"54672": -1.0918156967, "109738": -1.1535387037},
          "line_item_type_id": {"54672": 0.9347314186, "109738": -1.2670823628},
          "os_id": {"54672": -0.6222839746, "109738": -0.6222839746},
          "monetization_channel_id": {"54672": -1.4621509984, "109738": 0.6399059922},
          "ad_unit_id": {"54672": 0.6329273921, "109738": 0.6649230304},
          "total_impressions": {"54672": -0.0731608368, "109738": -0.2564441896},
          "viewable_impressions": {"54672": 0.1089480653, "109738": -0.229004725},
          "day": {"54672": 1.3310240681, "109738": 0.9777512715}
        }
        
        # Mocking the model's predict method to return the expected predictions
        mock_model.predict.return_value = pd.Series([
            [0.006275742780417204], [1.1706428267643787e-05]
        ])  # Return predefined predictions
        
        # Act: simulate a POST request to the predict function
        response = self.app.post('/predict', json=test_data)

        # Convert the response to JSON format
        response_data = json.loads(response.get_data(as_text=True))

        # Assert: check if the response contains the expected predictions
        self.assertIn('predictions', response_data)
        self.assertEqual(response_data['predictions'], [
            [0.006275742780417204], [1.1706428267643787e-05]
        ])

    @patch('app.model')  # Mocking the model object
    def test_predict_with_empty_data(self, mock_model):
    # Arrange: simulate empty JSON data
        test_data = {}
        
        # Mocking the model's predict method to return the expected predictions
        mock_model.predict.return_value = pd.Series([])  # Return predefined predictions
        
        # Act: simulate a POST request with empty data
        response = self.app.post('/predict', json=test_data)

        # Convert the response to JSON format
        response_data = json.loads(response.get_data(as_text=True))

        # Assert: check if the response contains the expected predictions
        self.assertIn('predictions', response_data)
        self.assertEqual(response_data['predictions'], [])
                
