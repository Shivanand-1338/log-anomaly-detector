from sklearn.feature_extraction.text import TfidfVectorizer

def load_logs(file_path="logs.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return [line.strip().split(" ", 2)[-1] for line in lines]  # remove timestamp

def vectorize_logs(log_lines):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(log_lines)
    return X, vectorizer