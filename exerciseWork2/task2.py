import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
import scipy.stats.mstats as ms

# Read data to pandas dataframe
data = pd.read_csv('winequality-white.csv', sep=';')

# Select input variables as x and typecast to numpy array
x = np.array(data.iloc[0:,0:11])

# Select output variable (quality) as y and typecast to numpy array
y = np.array(data.quality)

'''
# Zscore normalize
x = ms.zscore(x)
y = ms.zscore(y)
'''

# Use scikit learn method
neighbors = KNeighborsRegressor(n_neighbors=8)
neighbors.fit(x, y)

# Compared predicted and actual quality values for first 100 samples
for i in range(0,100):
	predicted = float(neighbors.predict(x[i].reshape(1, -1)))
	actual = y[i]
	print('Predicted: ' + str(predicted) + ' actual: ' + str(actual))



