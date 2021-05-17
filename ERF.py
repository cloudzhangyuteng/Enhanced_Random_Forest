
import sklearn
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt

def func(X):
    res = np.sin(np.pi*X[:,0])
    res = res + 4/(1+np.exp(-20*X[:,1]+10))
    res += 2*X[:,2]+2*X[:,3]
    return res

np.random.seed(123)
train_size = 1000
dev_size = 100
feature_size = 10
train_x = np.random.uniform(0,1,size=(train_size,feature_size))
train_y = func(train_x)

test_x = np.random.uniform(0,1,size=(dev_size,feature_size))
test_y = func(test_x)

from sklearn import linear_model
reg=linear_model.Lasso(alpha=0.5,fit_intercept=True)
reg.fit(train_x,train_y)
y_predict=reg.predict(train_x)

epsilon = train_y-y_predict
regressor = RandomForestRegressor(n_estimators=100,random_state=0)
regressor.fit(train_x,epsilon)

y_predict = regressor.predict(test_x) + reg.predict(test_x)

err = np.sqrt(np.sum((y_predict-test_y)**2))
err = np.sqrt(np.sum((y_predict-test_y)**2))
abs_err = np.abs(y_predict-test_y)
plt.scatter(test_x[:,2],abs_err,c='r')
plt.xlabel("test_x[2]")
plt.ylabel("error")
plt.title('Enhanced-RF')
plt.show()
print('err:',err)
