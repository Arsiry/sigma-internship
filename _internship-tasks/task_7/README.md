# TASK 7
## Prepare a machine learning model
The dataset has data for several websites owned by the same company and they are asking for your help for what should be their approach to set reserve prices and what is the range for reserve prices they should be setting for July. 

Explore data, find corelation between fields, and predict total revenue in order to know the Impact of Digital Advertisement for Business

Build a python app which makes prediction with the model via JSON

## Content
* `/task_7_dataset/Dataset.csv`, given dataset 
* `task_7.ipynb`, jupiter notebook: EDA, feature engineering, ANN model application
* `task_7_model.py`, This script loads a dataset, splits it into training and validation sets, builds and trains a neural network using TensorFlow, evaluates the model, makes predictions, and saves both the validation data in JSON format and the trained model to disk.
* `app.py`, This script creates a Flask API that loads a pre-trained model to receive input data in JSON format, make predictions using the model, and return the results as a JSON response.
* `/task_7_dataset/Dataset_X.csv`, given dataset without target variable
* `/task_7_dataset/Dataset_y.csv`, target variable
* `test_data.json`, validation dataset in JSON format
* `predictions.json`, resulting prediction in JSON format
* `test-7.postman_collection.json`, Postman collection used for testing
* `postman_screen.png`, screenshot from Postman
* `tests.py`, tests for app.py
* `requirements.txt`, file with prod dependencies
* `Makefile`, make file to run tests


EDA was done. The dataset was checked for missing values and outliers. Correlation Analysis with statistical tests was performed.

The Neural Network was applied. Used Feature Scaling.

The python app which makes prediction with the model via JSON was builded.

Link to Kaggle:
`https://www.kaggle.com/code/annatrofy/real-time-advertiser-s-auction-deep-learning`
