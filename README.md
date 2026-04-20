## **Medical Insurance Cost Prediction using Support Vector Regression (SVR)**

### 

### Author: MANIKANDAPRABHU.S

### Project Type: Machine Learning – Regression



\---



#### **1) Project Overview**



##### This project predicts medical insurance costs using Support Vector Regression (SVR).

##### 

##### The model is trained on customer demographic and health-related data to understand how different factors influence insurance charges.



\---



#### **2) Dataset**



##### File used: `insurance\_pre.csv`

##### 

##### The dataset contains:

##### 

##### &#x20; \* Age

##### &#x20; \* BMI (Body Mass Index)

##### &#x20; \* Number of Children

##### &#x20; \* Gender

##### &#x20; \* Smoking Status

##### &#x20; \* Charges (Target Variable)

##### 

##### The goal is to predict insurance cost based on these features.



\---



#### **3) Workflow**



##### 1\. Import required libraries

##### 2\. Load dataset using pandas

##### 3\. Handle categorical variables using encoding

##### 4\. Prepare feature matrix (X) and target variable (y)

##### 5\. Split dataset into training and testing sets

##### 6\. Apply feature scaling (StandardScaler)

##### 7\. Train SVR model

##### 8\. Perform hyperparameter tuning using GridSearchCV

##### 9\. Make predictions

##### 10\. Evaluate model using:

##### &#x09;\* R² Score

##### &#x09;\* Mean Squared Error (MSE)

##### &#x09;\* Root Mean Squared Error (RMSE)

##### &#x09;\* Mean Absolute Error (MAE)

##### 

##### 11\. Visualize results

##### 12\. Save trained model and scaler

##### 

##### \---

##### 

#### **4) Model Evaluation**

##### 

##### \* The SVR model provides good prediction performance after tuning.

##### \* Feature scaling significantly improves accuracy.

##### \* Hyperparameter tuning helps find the optimal model configuration.

##### 

##### \---

##### 

#### **5) Project Files**

##### 

##### \* `01\_SVR\_Model.ipynb` 	 	– Model training and evaluation

##### \* `02\_Deployment\_SVR\_.ipynb` 	– Model deployment and prediction

##### \* `insurance\_pre.csv` 		– Dataset

##### \* `Finalized\_svr\_model.sav` 	– Trained SVR model

##### \* `scaler.pkl` 			– Saved StandardScaler

##### \* `requirements.txt` 		– Required Python libraries

##### 

##### \---

##### 

#### **6) Technologies Used**

##### 

##### \* Python

##### \* Pandas

##### \* NumPy

##### \* Matplotlib

##### \* Scikit-Learn

##### \* Pickle

##### 

##### \---

##### 

#### **7) Model Deployment**

##### 

##### \* Model and scaler are saved using pickle

##### \* Deployment implemented using Jupyter Notebook

##### \* User input is taken, scaled, and passed to the model for prediction

##### 

##### \---

##### 

#### **8) Conclusion**

##### 

##### \* Implemented SVR to predict insurance costs

##### \* Feature scaling improved model performance

##### \* GridSearchCV optimized hyperparameters

##### \* Model shows good accuracy with evaluation metrics

##### \* Demonstrates importance of preprocessing and tuning

##### 

##### \---

##### 

#### **9) Use Case**

##### 

##### This project helps insurance companies estimate customer charges based on personal and health-related factors, enabling better pricing strategies.

##### 

