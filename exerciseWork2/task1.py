import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Read data to pandas dataframe
data = pd.read_csv('winequality-white.csv', sep=';')


# Select input variables as x
x = data.iloc[0:,0:11]

# Select output variable (quality) as y
y = data.quality

print(x)

'''
lm = LinearRegression()

lm.fit(x,y)

print(lm.intercept_)
'''