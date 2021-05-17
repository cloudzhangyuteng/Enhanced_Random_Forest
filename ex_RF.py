
import sklearn
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from scipy.stats import beta
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
train_x[:,2] = beta(4,8).pdf(train_x[:,2])
print('max trainx;',max(train_x[:,2]))
train_y = func(train_x)

test_x = np.random.uniform(0,1,size=(dev_size,feature_size))
test_x[:,2] = beta(5,1).pdf(test_x[:,2])
print('max test_x;',max(test_x[:,2]))
test_y = func(test_x)


regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(train_x,train_y)

y_predict = regressor.predict(test_x)

err = np.sqrt(np.sum((y_predict-test_y)**2))

abs_err = np.abs(y_predict-test_y)
plt.scatter(test_x[:,2],abs_err,c='r')
plt.xlabel("test_x[3]")
plt.ylabel("error")
plt.title('RF')
plt.show()


plt.scatter(test_x[:,2],y_predict,c='r')
plt.scatter(train_x[:,2],train_y,c='b')
plt.xlabel("test_x[2]")
plt.ylabel("Y")
plt.title('RF')
plt.show()
print('err:',err)
