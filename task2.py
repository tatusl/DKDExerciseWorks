import numpy as np
import matplotlib.pyplot as plt
import math
import os
import pandas
from pandas.tools.plotting import parallel_coordinates
from whiteWineData import WhiteWineData

data1 = WhiteWineData()
data2 = pandas.read_csv('winequality-white.csv', sep=';')

def drawScatterPlot(attr1, attr2, attr1Name, attr2Name):
	#attr1 = np.random.choice(attr1, 200)
	#attr2 = np.random.choice(attr2, 200)
	plt.scatter(attr1, attr2)
	plt.xlabel(attr1Name)
	plt.ylabel(attr2Name)
	plt.show()

def drawParallelCoordinates(data, columnString):
	plt.figure()
	parallel_coordinates(data, columnString)
	plt.show()

def drawParallelCoordinatesWithLimit(data, columnString):
	plt.figure()
	parallel_coordinates(data, columnString)
	plt.ylim(0, 10)
	plt.show()

#drawParallelCoordinates(data2, 'quality')
drawParallelCoordinatesWithLimit(data2, 'quality')

#drawScatterPlot(data.density, data.fixedAcidity, 'Density', 'Fixed Acidity')
