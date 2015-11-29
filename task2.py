import numpy as np
import matplotlib.pyplot as plt
import math
import os
import pandas
import itertools
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import scatter_matrix
from whiteWineData import WhiteWineData

data1 = WhiteWineData()
data2 = pandas.read_csv('winequality-white.csv', sep=';')

def drawScatterPlot(attr1, attr2, attr1Name, attr2Name):
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
	plt.show()

def drawParallelCoordinatesWithLimit(data, columnString):
	# Reduce number of samples
	#sampledData = data.loc[np.random.choice(data.index, 500, replace=False)]
	#print(len(sampledData))
	normData = data/data.max().astype(np.float64)
	plt.figure()
	parallel_coordinates(normData, columnString)
	#plt.ylim(0, 15)
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
	
saveAllScatterPlots(data1.attrList, data1.attributeNames)
