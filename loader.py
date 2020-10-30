from joblib import load
from sklearn import datasets


model = load('application/model.joblib')
X, y = datasets.load_iris(return_X_y=True)

for i in range(len(X)):
    row = X[i]
    y_true = y[i]
    y_pred, *_ = model.predict([row])
    y_prob, *_ = model.predict_proba([row])
    print(f'#{i} {list(row)}: {y_pred}/{y_true} @ {100 * y_prob[y_pred]:.2f}%')
