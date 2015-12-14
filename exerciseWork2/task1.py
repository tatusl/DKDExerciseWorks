import numpy as np
import pandas as pd
import itertools
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

# Returns in-sample error vectors
def calculateInSampleErrorVectors(dataIn):
	# Split data to 5 parts
	splittedData = np.array_split(dataIn, 5)
	
	# Get index combinations
	indexCombinations = list(itertools.combinations(range(0, len(splittedData)), 4))

	# Create in-sample data
	inSampleDataList = []
	for combination in indexCombinations:
		inSampleData = []
		for index in combination:
				dataInIndex = list(np.array(splittedData[index]))
				inSampleData += dataInIndex
		inSampleData = np.array(inSampleData)
		inSampleDataList.append(inSampleData)

	inSampleErrorVectors = []

	for dataPart in inSampleDataList:
		# Split input variables and output variable out of the data part. Typecast to numpy array
		splittedX = dataPart[0:,0:11]
		splittedY = dataPart[:,11]

		# List containing errors for the data part
		errors = []

		for i in range(0, len(splittedY)):
			sampleReshaped = splittedX[i].reshape(1, -1)
			# Subtract the predicted quality from actual quality
			error = float(splittedY[i] - lm.predict(sampleReshaped))
			errors.append(error)

		inSampleErrorVectors.append(errors)

	return inSampleErrorVectors

# Returns concatenated vectors
def concatenateVectors(vectors):
	vectorsConcatenated = []
	for vector in vectors:
		vectorsConcatenated += vector
	return vectorsConcatenated

# Plot histogram
def plotHistogram(concatVector, title):
	figure = plt.figure()
	plt.hist(concatVector, bins=50, color='b')
	plt.title(title), plt.xlabel("Error"), plt.ylabel("Frequency")
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
np.set_printoptions(suppress=True)
np.set_printoptions(precision=5)

print(weightVector)

'''
print('Coeffients are: ')

for i in zip(x, coefs):
	print(i)
'''

outOfSampleErrorVectors = calculateOutOfSampleErrorVectors(data)
concatenatedOut = concatenateVectors(outOfSampleErrorVectors)
plotHistogram(concatenatedOut, 'Out-of-Sample Error Histogram')

inSampleErrorVectors = calculateInSampleErrorVectors(data)
concatenatedIn = concatenateVectors(inSampleErrorVectors)
plotHistogram(concatenatedIn, 'In-Sample Error Histogram')

numpyOut = np.array(concatenatedOut)
meanOut = np.mean(numpyOut)
varOut = np.var(numpyOut)

numpyIn = np.array(concatenatedIn)
meanIn = np.mean(numpyIn)
varIn = np.var(numpyIn)

print("Average error for out-of-sample: ")
print(meanOut)
print("Average error for in-sample: ")
print(meanIn)
print("Variance for out-of-sample")
print(varOut)
print("Variance for in-sample")
print(varIn)