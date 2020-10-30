from sklearn import svm, datasets
from joblib import dump
from sklearn.model_selection import train_test_split


X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42,
)
model = svm.SVC(
    class_weight='balanced',
    probability=True,
    random_state=42,
)
model.fit(X_train, y_train)
dump(model, 'application/model.joblib')

print(f"Training Accuracy: {100 * model.score(X_train, y_train):.2f}%")
print(f"Validation Accuracy: {100 * model.score(X_test, y_test):.2f}%")
