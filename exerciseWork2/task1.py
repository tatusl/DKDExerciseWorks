import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Read data to pandas dataframe
data = pd.read_csv('winequality-white.csv', sep=';')

# Select input variables as x
x = data.iloc[0:,0:11]

# Select output variable (quality) as y
y = data.quality

# Use linear regression from scikit
lm = LinearRegression()

lm.fit(x,y)

# Get intercept and coefficients
coefs = lm.coef_
intercept = lm.intercept_

# Combine them to get the weight vector
weightVector = np.hstack((np.array(intercept), np.array(coefs)))

print('Coeffients are: ')

for i in zip(x, coefs):
	print(i)

splittedData = np.array_split(data, 5)

# Calculate out sample error


outOfSampleErrorVectors = []

for part in splittedData:
	splittedX = part.iloc[0:,0:11]
	splittedY = part.quality
	predictedQualityList = []

	for sample in splittedX.iterrows():
		numpySample = np.array(sample[1])
		#print(numpySample)
		predictedQualityList.append(lm.predict(numpySample))
	
	outOfSampleVector = []
 
	for i in range(0, len(splittedY)):
		print(splittedY[i][0] - predictedQualityList[i])
		#outOfSampleVector.append(splittedY[i] - predictedQualityList[i])
	