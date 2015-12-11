import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Returns out-of-sample error vectors
def calculateOutOfSampleErrorVectors(dataIn):
	# Split data to 5 parts
	splittedData = np.array_split(dataIn, 5)

	# List containing out-of-sample error vectors for each data part
	outOfSampleErrorVectors = []

	for dataPart in splittedData:
		# Split input variables and output variable out of the data part. Typecast to numpy array
		splittedX = np.array(dataPart.iloc[0:,0:11])
		splittedY = np.array(dataPart.quality)
		# List containing errors for the data part
		errors = []

		for i in range(0, len(splittedY)):
			sampleReshaped = splittedX[i].reshape(1, -1)
			# Subtract the predicted quality from actual quality
			error = float(splittedY[i] - lm.predict(sampleReshaped))
			errors.append(error)

		outOfSampleErrorVectors.append(errors)

	return outOfSampleErrorVectors

# Returns concatenated vectors
def concatenateVectors(vectors):
	vectorsConcatenated = []
	for vector in vectors:
		vectorsConcatenated += vector
	return vectorsConcatenated

# Plot histogram
def plotHistogram(concatVector):
	figure = plt.figure()
	plt.hist(concatVector, bins=50, color='b')
	plt.show()

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

outOfSampleErrorVectors = calculateOutOfSampleErrorVectors(data)

concatenated = concatenateVectors(outOfSampleErrorVectors)

plotHistogram(concatenated)

