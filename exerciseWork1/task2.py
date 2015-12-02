import numpy as np
import matplotlib.pyplot as plt
import math
import os
import pandas
import itertools
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import scatter_matrix
from whiteWineData import WhiteWineData
from sklearn import preprocessing
import random

data1 = WhiteWineData()
data2 = pandas.read_csv('winequality-white.csv', sep=';')

def drawScatterPlot(attr1, attr2, attr1Name, attr2Name):
	# Limit number of samples if either of the attributes is density
	if (attr1Name == 'density' or attr2Name == 'density'):
		attr1 = np.random.choice(attr1, 1000)
		attr2 = np.random.choice(attr2, 1000)
	scatter = plt.figure()
	plt.scatter(attr1, attr2)
	plt.title('n = ' + str(len(attr1)))
	plt.xlabel(attr1Name)
	plt.ylabel(attr2Name)
	return scatter

def drawParallelCoordinates(data, columnString):
	plt.figure()
	parallel_coordinates(data, columnString)
	plt.title('Parallel coordinates, raw data')
	plt.show()

def drawParallelCoordinatesWithScaledValues(data, columnNames):
	# Construct dataframe without quality attribute (don't want to scale that)
	dataWoQuality = pandas.DataFrame(data.iloc[:,0:11])
	# Scale values
	scaled = pandas.DataFrame(preprocessing.scale(dataWoQuality))

	# Construct dataframe with quality attribute values
	quality = pandas.DataFrame(data.iloc[:,11])

	# Concatenate dataframes
	allAttributes = pandas.concat([scaled, quality], axis=1)

	# Add column names
	allAttributes.columns = columnNames

	# Select random samples
	num = 1500
	allAttributes = allAttributes.loc[random.sample(list(allAttributes.index), num)]

	# Plot figure
	plt.figure()
	parallel_coordinates(allAttributes, 'quality')
	plt.title('Parallel coordinates, scaled values ' + 'n: ' + str(len(allAttributes)))
	plt.ylim(-2, 4)
	plt.show()

def saveAllScatterPlots(data, attributeNames):
	# Calculate index combinations
	combinations = list(itertools.combinations(range(0, len(data1.attrList)), 2))
	for comb in combinations:
		filename = 'scatter_plot_' + attributeNames[comb[0]] + '_' + attributeNames[comb[1]]
		scatterPlot = drawScatterPlot(data[comb[0]], data[comb[1]], attributeNames[comb[0]], attributeNames[comb[1]])
		saveFigure(scatterPlot, filename)

# Saves the given figure
def saveFigure(figure, filename):
	currentPath = os.path.dirname(os.path.abspath(__file__))
	figuresPath = os.path.join(currentPath, 'figures')
	taskFigurePath = os.path.join(figuresPath, 'task2')
	_filename = os.path.join(taskFigurePath, filename)
	figure.savefig(_filename)
	print('Saved ' + filename)
	
#saveAllScatterPlots(data1.attrList, data1.attributeNames)

#drawParallelCoordinates(data2, 'quality')
drawParallelCoordinatesWithScaledValues(data2, data1.attributeNames)



