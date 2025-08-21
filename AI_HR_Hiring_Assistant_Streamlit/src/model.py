import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

# -----------------------------
# Build absolute path to CSV
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Goes up from /src/
hiring_history_path = os.path.join(BASE_DIR, "data", "hiring_history.csv")

# Debug: check if file exists
if not os.path.exists(hiring_history_path):
    raise FileNotFoundError(f"hiring_history.csv not found at {hiring_history_path}")

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv(hiring_history_path)

X = df.drop("hired", axis=1)
y = df["hired"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train logistic regression
clf = LogisticRegression().fit(X_scaled, y)

# -----------------------------
# Prediction function
# -----------------------------
def predict_hire_score(features):
    """Return probability of being hired given a features dict"""
    if not features:
        return 0.5
    # Example feature vector: length of name and email
    vec = np.array([[len(str(features.get("name", ""))), len(str(features.get("email", "")))]])
    vec = scaler.transform(vec)
    return float(clf.predict_proba(vec)[0][1])

