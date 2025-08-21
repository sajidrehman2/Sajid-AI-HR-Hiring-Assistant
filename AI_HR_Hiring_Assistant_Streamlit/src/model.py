import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv("data/hiring_history.csv")
X = df.drop("hired", axis=1)
y = df["hired"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
clf = LogisticRegression().fit(X_scaled, y)

def predict_hire_score(features):
    if not features:
        return 0.5
    vec = np.array([[len(str(features.get("name", ""))), len(str(features.get("email", "")))]])
    vec = scaler.transform(vec)
    return float(clf.predict_proba(vec)[0][1])
