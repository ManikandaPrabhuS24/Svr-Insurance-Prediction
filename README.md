# Medical Insurance Cost Prediction Using Support Vector Regression

## Project Overview

This project is a Machine Learning application developed to predict medical insurance charges using the Support Vector Regression (SVR) algorithm. The project demonstrates the complete Machine Learning pipeline, including:

- Data preprocessing
- Feature engineering
- Model training
- Feature scaling
- Model serialization
- Deployment using Streamlit

The application predicts insurance costs based on customer details such as age, BMI, smoking status, gender, and number of children.

---

## Project Structure

```text
Medical-Insurance-Cost-Prediction/
│
├── 01_SVR_Model.ipynb
├── 02_Deployment_SVR.ipynb
├── app.py
├── insurance_pre.csv
├── Finalized_svr_model.sav
├── requirements.txt
└── README.md
```

---

## Technologies Used

| Category | Tools / Libraries |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Data Visualization | Matplotlib |
| Model Deployment | Streamlit |
| Feature Scaling | StandardScaler |
| Model Serialization | Pickle |

---

## Dataset Information

The dataset contains customer information used to predict medical insurance charges.

### Features Used

| Feature Name | Description |
|---|---|
| age | Customer age |
| bmi | Body Mass Index |
| children | Number of dependent children |
| sex | Gender |
| smoker | Smoking status |
| charges | Insurance cost (target variable) |

---

## Machine Learning Workflow

### 1. Import Required Libraries

Libraries are imported for:

- Data handling
- Data preprocessing
- Visualization
- Feature scaling
- Model training
- Deployment

---

### 2. Load Dataset

The dataset is loaded and analyzed using Pandas.

The preprocessing workflow includes:

- Checking missing values
- Data inspection
- Feature analysis
- Data cleaning

---

### 3. Data Preprocessing

Categorical variables are converted into numerical format.

Examples:

- Male → 1
- Female → 0
- Smoker → 1
- Non-Smoker → 0

Feature scaling is applied using:

```python
StandardScaler
```

---

### 4. Feature Selection

### Input Features

```text
Age
BMI
Children
Gender
Smoking Status
```

### Target Variable

```text
Insurance Charges
```

---

### 5. Model Training

The project uses:

```python
Support Vector Regression (SVR)
```

SVR is used to learn complex relationships between customer health-related attributes and insurance costs.

---

### 6. Model Saving

The trained model is saved using Pickle serialization.

```text
Finalized_svr_model.sav
```

---

### 7. Model Deployment

The trained SVR model is deployed using Streamlit.

Users can enter customer information and receive instant insurance cost predictions.

---

## Streamlit Application

The Streamlit application provides an interactive interface for insurance cost prediction.

### User Inputs

| Input | Description |
|---|---|
| Age | Customer age |
| BMI | Body Mass Index |
| Number of Children | Dependents count |
| Gender | Male / Female |
| Smoker | Smoking status |

---

### Application Output

```text
Predicted Medical Insurance Cost
```

---


## Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Example Prediction Workflow

### Sample Inputs

| Feature | Example Value |
|---|---|
| Age | 30 |
| BMI | 28.5 |
| Children | 2 |
| Gender | Male |
| Smoker | Yes |

### Predicted Output

```text
8138.28
```

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Support Vector Regression
- Feature scaling
- Data preprocessing
- Model deployment
- Streamlit integration
- Building ML applications
- Machine Learning workflow
- Model serialization using Pickle

---

## Future Improvements

Potential enhancements for this project:

- Add hyperparameter tuning
- Improve prediction accuracy
- Add model evaluation metrics
- Add advanced visualizations
- Deploy on cloud platforms
- Build responsive UI design
- Add API integration

---

## Author

**MANIKANDAPRABHU.S**

Machine Learning and Artificial Intelligence Enthusiast

