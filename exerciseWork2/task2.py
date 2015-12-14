import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import NearestNeighbors
from decimal import *

# Returns out-of-sample error vectors after nearest neighbour regression
def calculateOutOfSampleErrorVectors(dataIn, neighbors):
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
			error = float(splittedY[i] - neighbors.predict(sampleReshaped))
			#print(error)
			errors.append(error)

		outOfSampleErrorVectors.append(errors)

	return outOfSampleErrorVectors

# Returns in-sample error vectors
def calculateInSampleErrorVectors(dataIn, neighbors):
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
			error = float(splittedY[i] - neighbors.predict(sampleReshaped))
			errors.append(error)

		inSampleErrorVectors.append(errors)

	return inSampleErrorVectors

# Calculates model with K nearest neighbors, returns the model
def calculateKNearestNeighborsModel(data, numberOfNeighbors):
	# Select input variables as x and typecast to numpy array
	x = np.array(data.iloc[0:,0:11])
	# Select output variable (quality) as y and typecast to numpy array
	y = np.array(data.quality)
	neighbors = KNeighborsRegressor(n_neighbors=numberOfNeighbors)
	neighbors.fit(x, y)
	return neighbors

# Returns concatenated vectors
def concatenateVectors(vectors):
	vectorsConcatenated = []
	for vector in vectors:
		vectorsConcatenated += vector
	return vectorsConcatenated

def calculateErrorVectorMean(errorVector):
	return(np.mean(errorVector))

# Plot histogram
def plotHistogram(concatVector, title):
	figure = plt.figure()
	plt.hist(concatVector, bins=50, color='b')
	plt.title(title)
	plt.show()

# Read data to pandas dataframe
data = pd.read_csv('winequality-white.csv', sep=';')

'''
# Predict with k=1 and plot absolute error histograms
model = calculateKNearestNeighborsModel(data, 1)
outOfSampleErrorVectors = calculateOutOfSampleErrorVectors(data, model)
inSampleErrorVectors = calculateInSampleErrorVectors(data, model)
plotHistogram(concatenateVectors(outOfSampleErrorVectors), 'Out-of-Sample error vector, k-NN regression, k=1')
plotHistogram(concatenateVectors(inSampleErrorVectors), 'In-sample error vector, k-NN regression, k=1')
'''

'''
for k in range(1,9):
	model = calculateKNearestNeighborsModel(data, k)
	outOfSampleErrorVectors = calculateOutOfSampleErrorVectors(data, model)
	concatenatedErrorVectors = concatenateVectors(outOfSampleErrorVectors)
	meanError = calculateErrorVectorMean(concatenatedErrorVectors)
	print('Out-of-sample mean error when neighbors ' + str(k) + ' : ' + str(meanError))
'''

# Predict with k=3 and plot absolute error histograms
model = calculateKNearestNeighborsModel(data, 3)
outOfSampleErrorVectors = calculateOutOfSampleErrorVectors(data, model)
inSampleErrorVectors = calculateInSampleErrorVectors(data, model)
plotHistogram(concatenateVectors(outOfSampleErrorVectors), 'Out-of-Sample error vector, k-NN regression, k=3')
plotHistogram(concatenateVectors(inSampleErrorVectors), 'In-sample error vector, k-NN regression, k=3')

# Experimentation with NearestNeighbor method
'''
x = np.array(data.iloc[0:,0:11])
# Select output variable (quality) as y and typecast to numpy array
y = np.array(data.quality)

nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(data)

distances, indices = nbrs.kneighbors(data)

for i in range(0, len(y)):
	print('Actual quality: ' + str(y[i]) + ' predicted quality: ' + str(y[indices[i][0]]))
	print(y[i] == y[indices[i][0]])
'''