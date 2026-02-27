# model.py

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset (hours studied vs score)
hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
scores = np.array([40, 50, 60, 65, 75, 85])

model = LinearRegression()
model.fit(hours, scores)

def predict_score(study_hours):
    study_hours = np.array([[study_hours]])
    prediction = model.predict(study_hours)
    return round(float(prediction[0]), 2)
