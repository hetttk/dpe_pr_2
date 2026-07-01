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

# Part A: Missing Value Handling

The following techniques were implemented:

### 1. Mean Imputation
Missing numerical values were replaced using the mean value.

### 2. Median Imputation
Missing numerical values were replaced using the median value.

### 3. Most Frequent Imputation
Missing categorical values were replaced using the most frequently occurring category.

### 4. Missing Indicator and Random Sample Imputation
A missing value indicator was created and missing values were filled using random sampling from existing observations.

### 5. KNN Imputation
Missing values were estimated using nearest neighboring records.

### 6. MICE (Iterative Imputer)
Missing values were predicted using relationships between multiple features.

---

# Part B: Outlier Detection and Treatment

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
