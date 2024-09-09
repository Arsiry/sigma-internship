__________________________________________________________________
__________________________________________________________________

### INTERNSHIP TASKS
__________________________________________________________________

#### TASK 1
##### Prepare a machine learning model

Predict the probability of user clicking the ad which is shown to them on the partner websites for the next 7 days on the basis of historical view log data, ad impression data and user data.

     (task_1_dataset/)
     (train.csv item_data.csv viewlog.csv | test.csv  sample_submission.csv)

The evaluated metric should be "area under the ROC curve" between the predicted probability and the observed target.

##### VS Code
##### Python (Numpy, Pandas, MatplotLib, Seaborn, Scikit-Learn, XGBoost)

Created data transformation pipeline

Pipeline produces final united dataset

EDA is conducted 

Feature Engineering is provided

Logistic Regression, Decision Trees, Random Forest, Gradient Boosting were applied

Best Model is selected (Gradient Boosting, the evaluated metric is "area under the ROC curve")

     task_1.ipynb 
__________________________________________________________________

#### TASK 2
#### Prepare a machine learning model

The dataset provided to you has data for several websites owned by the same company and they are asking for your help for what should be their approach to set reserve prices and what is the range for reserve prices they should be setting for July.

     (task_2_dataset/AD-Tech.csv)

##### VS Code
##### Python (Numpy, Pandas, MatplotLib, Seaborn, Scipy, Scikit-Learn, XGBoost)

EDA is conducted 

Feature Engineering is provided

Decision Trees, Random Forest, Gradient Boosting were applied

Best Model is selected (Random Forest and Gradient Boosting, the evaluated metric is mean absolute error)

     task_2.ipynb 
__________________________________________________________________

#### TASK 7
##### Prepare a machine learning model

The dataset provided to you has data for several websites owned by the same company and they are asking for your help for what should be their approach to set reserve prices and what is the range for reserve prices they should be setting for July.

     (task_7_dataset/Dataset.csv - dataset equal to dataset of Task 2)

##### VS Code
##### Python (Numpy, Pandas, MatplotLib, Seaborn, Scipy, Scikit-Learn, TensorFlow, Keras)

EDA is conducted 

Feature Engineering is provided

ANN were applied

     task_3.ipynb 
__________________________________________________________________

#### TASK 3
##### Collect data and Provide EDA

Created a database to ingest millions of simulated Ad Campaign events from a Kafka workspace.

##### SingleStore

Database is configured

     AdTechDatabase.pdf

Data are collected for 3 days

##### Metabase

Use a dashboard tool Metabase to connect to the database to visualize and analyze the event data.

EDA is conducted

     AdTechDashboard.pdf
__________________________________________________________________

#### TASK 4
#### Database Mongo 

Design the DB for a task in AdTech domain. Make queries for data ingestion, extraction, aggregation.

BD in AdTech domain from Task 1:

     train.csv     
     viewlog.csv    
     item_data.csv 


##### Lucidchart

Visual data model diagram

Data normalization

Indexes
     
     AdTechDatabaseModel-SimpleSchema.pdf
     AdTechDatabaseModel-DatabaseSchema.pdf

##### MongoDB

DB schema

Aggregation framework

     MongoDb-Database.pdf

Raw queries

     MongoDB-Mongosh.pdf
__________________________________________________________________

#### TASK 5
#### Database Postgres 

Design the DB for a task in AdTech domain. Make queries for data ingestion, extraction, aggregation.

BD in AdTech domain from Task 1:

     train.csv 
     viewlog.csv
     item_data.csv

##### Lucidchart

Visual data model diagram

Data normalization

Indexes
 
     AdTechDatabaseModel-SimpleSchema.pdf
     AdTechDatabaseModel-DatabaseSchema.pdf

##### Postres
##### Valentina Studio

DB schema

Aggregation framework

     PostgreSQLDatabase.pdf

Raw queries

     ad_tech_sql_collecting_data_1.sql
     ad_tech_sql_collecting_data_2.sql
     ad_tech_sql_collecting_data_3.sql
     ad_tech_sql_create_table_1.sql
     ad_tech_sql_create_table_2.sql
     ad_tech_sql_create_table_3.sql
__________________________________________________________________

#### TASK 6
##### Create a delta/csv spark table and build a data transformation pipeline with at least 3 aggregations and filtering.
     
     impressions.csv (train.csv)

BD in AdTech domain from Task 1:
     
##### VS Code
##### Python (PySpark, Delta)

Delta/csv spark table created

Data transformation pipeline with 3 aggregations and filtering built

Pipeline produces data 

Unit tests are done

Data Quality tests are done

     task_6.ipynb
     task_6.py
     unit_tests_task_6.py
     data_quality_tests_task_6.py
__________________________________________________________________
__________________________________________________________________

### PRACTICE AT KAGGLE
__________________________________________________________________

#### KAGGLE COMPETITIONS

##### Titanic - Machine Learning from Disaster

Predict survival on the Titanic 

     (titanic_train.csv titanic_test.csv titanic_gender_submission.csv)
     titanic.ipynb 

##### House Prices - Advanced Regression Techniques

Predict sales prices 
     
     (housing_prices_test.csv housing_prices_train.csv housing_prices_submission.csv housing_prices_sample_submission.csv)

     housing_prices_v1.ipynb
     housing_prices_v2.ipynb
     housing_prices_v3.ipynb
     housing_prices_v4.ipynb
     housing_prices_v5.ipynb
     housing_prices_v6.ipynb

__________________________________________________________________

#### EDA 
#### EXPLORATORY DATA ANALYSIS

Intro to Exploratory data analysis (EDA) in Python
     
     intro-to-eda.ipynb (data.csv)

Detailed exploratory data analysis (EDA) with python
     
     detailed-eda.ipynb (train.csv  data_description.txt)

Advanced Visualisation for Exploratory data analysis (EDA)
     
     advanced-visualization-for-eda.ipynb (penguins.csv)

Advanced Functional Exploratory Data Analysis (EDA)
     
     advanced-functional-eda.ipynb (titanic.csv) 

Univariate statistics
     
     eda-univariate-statistics.ipynb (insurance.csv heart_attack_prediction_dataset.csv)

Zomato Dataset EDA
     
     eda-zomato.ipynb (zomatodataset)

Black Friday Sales EDA
     
     eda-black-friday.ipynb (blackFriday_train.csv  blackFriday_test.csv)

Flight Price Prediction EDA 
     
     eda-flight-price-prediction.ipynb (Data_Train.xlsx Test_set.xlsx)
__________________________________________________________________

#### FEATURE ENGINEERING

Feature Engineering Kaggle Course
     
     fe-course-1-intro.ipynb (Concrete_Data.xls)
     fe-course-2-mutual-info.ipynb (Aumobile_data.csv)
     fe-course-2-mutual-info-ex.ipynb (ames.csv)
     fe-course-3-creating-features.ipynb (autos.csv accidents.csv concrete.csv customer.csv)
     fe-course-3-creating-features-ex.ipynb (ames.csv)
     fe-course-4-clustering-with-k-means.ipynb (housing.csv)
     fe-course-4-clustering-with-k-means-ex.ipynb (ames.csv)
     fe-course-5-principal-component-analysis.ipynb (autos.csv)
     fe-course-5-principal-component-analysis-ex.ipynb (ames.csv)
     fe-course-6-target-encoding.ipynb (movielens1m.csv)
     fe-course-6-target-encoding-ex.ipynb (ames.csv)

Advanced Feature Engineering
     
     advanced-feature-engineering.ipynb (DSB_Day1_Titanic_train.csv diamonds.csv application_train.csv)

Feature Engineering Reference Guide
     
     feature-engineering/feature-engineering-reference-guide.ipynb (titanic_train.csv)
__________________________________________________________________

#### MACHINE LEARNING KAGGLE COURSES

Course "Intro to Machine Learning"
     
     melbourne-housing-beginner.ipynb

Course "Intermediate Machine Learning"
     
     melbourne-housing-intermediate_missing_values.ipynb
     melbourne-housing-intermediate_categorical_variables.ipynb
     melbourne-housing-intermediate_pipelines.ipynb
     melbourne-housing-intermediate_cross_validation.ipynb
     melbourne-housing-intermediate_XGBoost.ipynb
     melbourne-housing-intermediate_data_leakage.ipynb

     (melb_data.csv AER_credit_card_data.csv)
__________________________________________________________________

#### DEEP LEARNING KAGGLE COURSE

     a-single-neuron.ipynb
     a-single-neuron-ex.ipynb
     deep-neural-networks.ipynb
     deep-neural-networks-ex.ipynb
     stochastic-gradient-descent.ipynb
     stochastic-gradient-descent-ex.ipynb
     overfitting-and-underfitting.ipynb
     overfitting-and-underfitting-ex.ipynb
     dropout-and-batch-normalization.ipynb
     dropout-and-batch-normalization-ex.ipynb
     binary-classification.ipynb
     binary-classification-ex.ipynb

     (concrete.csv fuel.csv hotel.csv ion.csv red-wine.csv spotify.csv)

__________________________________________________________________
__________________________________________________________________

### COURSES
__________________________________________________________________

Udemy

Complete SQL and Databases Bootcamp
__________________________________________________________________

Udemy

100 Days of Code: The Complete Python Pro Bootcamp
__________________________________________________________________

Udemy

Python Data Structures & Algorithms + LEETCODE Exercises
__________________________________________________________________

Prometheus (Київський Політехнічний Інститут)

Розробка та аналіз алгоритмів
__________________________________________________________________

Coursera (Princeton University)

Algorithms
__________________________________________________________________

Udemy

Intermediate to Advanced Python with 10 OOP Projects
__________________________________________________________________

Udemy

Digital Marketing & Advertising Masterclass - 87+ Lectures
__________________________________________________________________


