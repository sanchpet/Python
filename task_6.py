import pandas as pd
DATA = pd.read_csv("candy-data.csv", delimiter=',', index_col='competitorname')
train_data = DATA.drop(['Mike & Ike', 'Root Beer Barrels', 'Starburst'])
X = pd.DataFrame(train_data.drop(['winpercent', 'Y'],axis=1))
y = pd.DataFrame(train_data['Y'])
from sklearn.linear_model import LogisticRegression
reg = LogisticRegression(random_state=2019, solver='lbfgs').fit(X, y.values.ravel())
reg.predict_proba([[0,1,0,0,0,0,0,0,0,0.162,0.116]])
test_data = pd.read_csv("candy-test.csv", delimiter=',', index_col='competitorname')
X_test = pd.DataFrame(test_data.drop(['Y'], axis=1))
Y_pred = reg.predict(X_test)
Y_pred
Y_pred_probs = reg.predict_proba(X_test)
Y_pred_probs
Y_pred_probs_class_1 = Y_pred_probs[:, 1]
Y_true = (test_data['Y'].to_frame().T).values.ravel()
Y_true
from sklearn import metrics
fpr, tpr, _ = metrics.roc_curve(Y_true, Y_pred)
metrics.roc_auc_score(Y_true, Y_pred_probs_class_1)
metrics.recall_score(Y_true, Y_pred)
metrics.precision_score(Y_true, Y_pred)
