# TASK 1
## Prepare a machine learning model
Predict the probability of user clicking the ad which is shown to them on the partner websites for the next 7 days on the basis of historical view log data, ad impression data and user data.

We are provided with the view log of users (2018/10/15 - 2018/12/11) and the product description collected from the owner website. We also provide the training data containing details for ad impressions at the partner websites. Train data contains the impression logs during 2018/11/15 – 2018/12/13 along with the label which specifies whether the ad is clicked or not. 

The evaluated metric could be "area under the ROC curve" between the predicted probability and the observed target.


## Content
* `/task_1_dataset/train.csv`, train data contains the impression logs during 2018/11/15 – 2018/12/13 along with the label which specifies whether the ad is clicked or not 
* `/task_1_dataset/view_log.csv`, view log of users (2018/10/15 - 2018/12/11)
* `/task_1_dataset/item_data.csv`, products descriptions
* `task_1.ipynb`, jupiter notebook: collecting data, EDA, feature engineering, classical ML models application

The final dataset was created like this: 

- First, we look at the impression log (train.csv) and add a column with information about the number of ad impressions a user saw in the 7 days before the ad impression time. 
- Then, we add data from the user view log, where we check how many times the user visited the website in the 7 days before the ad impression time, what product was viewed most often, and the type of device used. 
- Lastly, we add product details.

EDA was done. The dataset was checked for missing values and outliers. Categorical Encoding, Feature Scaling, and Correlation Analysis were performed.

The following ML models were used: Logistic Regression, Decision Trees, Random Forest, and XGBoost. The XGBoost model gave the best result.

Link to Kaggle:
`https://www.kaggle.com/code/annatrofy/context-ad-clicks-machine-learning-algorithms`
