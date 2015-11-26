import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats.mstats as ms

from whiteWineData import WhiteWineData

def computePrincipalComponents(numpyArray):
	# Calculate covariance matrix
	covMatrix = np.cov(numpyArray.T)

	# Calculate eigenvectors and eigenvalues from the covariance matrix
	eigenValues, eigenVectors = np.linalg.eig(covMatrix)

	# Pair eigen values and eigen vectors
	eig_pairs = [(np.abs(eigenValues[i]), eigenVectors[:,i]) for i in range(len(eigenValues))]

	# Sort pairs to descending order
	eig_pairs.sort()
	eig_pairs.reverse()

	# Choose two eigenvectors with the highest eigen values
	firstEigenVector = eig_pairs[0][1].reshape(12,1)
	secondEigenVector = eig_pairs[1][1].reshape(12,1)

	# Horizontally stack the eigenvectors
	stackedMatrix = np.hstack((firstEigenVector, secondEigenVector))

	# Use the computed matrix to transform samples onto the new subspace
	transformed = stackedMatrix.T.dot(numpyArray.T)

	return transformed

def plotPrincipalComponents(data):
	plt.plot(data[0,:], data[1,:], 'o', markersize=7, color='red')
	#plt.xlim(0,300)
	#plt.ylim(-50,50)
	plt.show()

# Save data to numpy array
numpyArray = np.array(WhiteWineData().wholeData).astype(np.float)

# Zscore standardise numpy array
numpyArrayZscored = ms.zscore(numpyArray)

plotPrincipalComponents(computePrincipalComponents(numpyArray))

plotPrincipalComponents(computePrincipalComponents(numpyArrayZscored))