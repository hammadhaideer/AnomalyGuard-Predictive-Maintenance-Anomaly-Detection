import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest

data = pd.read_csv('/content/dataset.csv')
non_numeric_cols = data.select_dtypes(exclude=['number']).columns.tolist()
data = pd.get_dummies(data, columns=non_numeric_cols)
X = data

X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

clf = IsolationForest(random_state=42)
clf.fit(X_train)

y_pred = clf.predict(X_test)

print("Predicted labels for anomalies (outliers):")
print(y_pred)

num_anomalies = (y_pred == -1).sum()
print(f"Number of anomalies: {num_anomalies}")
