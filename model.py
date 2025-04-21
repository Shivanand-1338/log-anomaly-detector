from sklearn.ensemble import IsolationForest

def train_anomaly_detector(X):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    return model