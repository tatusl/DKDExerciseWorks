import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import manifold
from sklearn.metrics import euclidean_distances
import scipy.stats.mstats as ms

from whiteWineData import WhiteWineData

data = WhiteWineData().wholeData

def plot2DMDSScatterPlot(data):
	
	# Limit sample. Maybe add random choice.
	#data = data[0: 2000]

	# Calcluate Euclidean distances
	#distances = euclidean_distances(data)

	# Multi Dimensional Scaling
	mds = manifold.MDS(n_components=2, dissimilarity="euclidean", n_jobs=1)

	# Calculate coordinates for new (2D) space
	coordinates = mds.fit(data).embedding_

	# Plot
	plt.plot(coordinates[:,0], coordinates[:,1], 'o', markersize=7, color='red')
	plt.show()

plot2DMDSScatterPlot(data)
