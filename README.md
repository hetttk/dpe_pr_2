# Data Cleanser Project

## Data Preprocessing and Feature Engineering for Healthcare Dataset

---

# Project Overview

This project focuses on cleaning and preparing healthcare data for Machine Learning applications. The dataset contains missing values and outliers that can negatively affect data analysis and model performance.

Various preprocessing techniques were applied to improve data quality and create a reliable dataset suitable for predictive modeling.

---

# Project Objectives

- Identify missing values in the dataset.
- Apply different missing value imputation techniques.
- Detect outliers using statistical methods.
- Treat outliers using appropriate techniques.
- Compare preprocessing methods.
- Prepare a clean dataset for Machine Learning.

---

# Dataset Description

The dataset consists of synthetic healthcare records containing patient information and health indicators.

## Features

| Feature | Description |
|----------|-------------|
| patient_id | Unique patient identifier |
| age | Age of patient |
| gender | Gender of patient |
| region | Geographic region |
| bmi | Body Mass Index |
| blood_pressure | Blood pressure reading |
| cholesterol | Cholesterol level |
| glucose | Blood glucose level |
| disease_risk | Disease risk indicator |

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- SciPy
- Jupyter Notebook

---
<img width="826" height="403" alt="Screenshot 2026-07-01 142327" src="https://github.com/user-attachments/assets/337c4ade-6f15-4b22-8467-1c8dc964a3ae" />

# Part A: Missing Value Handling

The following techniques were implemented:

### 1. Mean Imputation
Missing numerical values were replaced using the mean value.
<img width="546" height="162" alt="image" src="https://github.com/user-attachments/assets/3a9284a9-e696-46c0-9ccd-c94c07c66b81" />

### 2. Median Imputation
Missing numerical values were replaced using the median value.
median = SimpleImputer(strategy="median")
<img width="586" height="122" alt="image" src="https://github.com/user-attachments/assets/37ee3413-1fa5-4680-b621-de480f5b56f1" />

### 3. Most Frequent Imputation
Missing categorical values were replaced using the most frequently occurring category.
<img width="750" height="255" alt="image" src="https://github.com/user-attachments/assets/cd674caf-3b0d-4b56-8501-7d3f6a8f1041" />

<img width="647" height="215" alt="image" src="https://github.com/user-attachments/assets/d49ab2a3-dd41-4428-a384-540a00de16ff" />


### 4. Missing Indicator and Random Sample Imputation
A missing value indicator was created and missing values were filled using random sampling from existing observations.

### 5. KNN Imputation
Missing values were estimated using nearest neighboring records.
<img width="697" height="391" alt="image" src="https://github.com/user-attachments/assets/a54184ac-7e50-4894-885a-89215e71b90b" />

### 6. MICE (Iterative Imputer)
Missing values were predicted using relationships between multiple features.
<img width="490" height="137" alt="image" src="https://github.com/user-attachments/assets/bb4e51b8-3f35-4b87-9cda-0ab9bd980b2e" />

---

# Part B: Outlier Detection and Treatment
before:
<img width="520" height="432" alt="cd1f1083-534f-4512-a85e-6dc4df81d210" src="https://github.com/user-attachments/assets/0cb0e7ca-f803-404d-be3a-3eaac4479e0f" />

after:
<img width="520" height="432" alt="a5f19eeb-6b97-460b-89cb-c20810baf627" src="https://github.com/user-attachments/assets/2a1c7cf1-4875-469b-8fa2-4f84dd0f7dd2" />


The following outlier handling techniques were implemented:

### IQR Method
Used to identify and remove BMI outliers.

### Z-Score Method
Used to detect extreme cholesterol values.

### Percentile Method
Used to cap extreme blood pressure values.

### Winsorization
Used to reduce the effect of extreme glucose values while preserving records.

---

# Project Workflow

1. Dataset Loading
2. Data Exploration
3. Missing Value Analysis
4. Missing Value Treatment
5. Outlier Detection
6. Outlier Treatment
7. Dataset Verification
8. Export Clean Dataset

---

# Libraries Used

```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

from scipy import stats
from scipy.stats.mstats import winsorize
```

---

# Results

- Missing values successfully identified and treated.
- Multiple imputation techniques implemented.
- Outliers detected using statistical approaches.
- Extreme values treated using capping and removal techniques.
- Final dataset prepared for Machine Learning applications.

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Statistical Analysis
- Outlier Detection
- Data Preparation
- Machine Learning Preprocessing

---

# Conclusion

The healthcare dataset was successfully cleaned using multiple preprocessing techniques. Missing values were handled using various imputation methods, and outliers were detected and treated using statistical approaches. The final dataset is consistent, reliable, and ready for Machine Learning and Data Analytics tasks.
