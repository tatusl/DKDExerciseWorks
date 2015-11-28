import numpy as np
import matplotlib.pyplot as plt
import math
import os
from whiteWineData import WhiteWineData

# Returns the number of bins with Sturges rule
def getBinsSturgesRule(numberOfSamples):
	bins = math.ceil(math.log(numberOfSamples, 2) + 1)
	print('Number of bins with Sturges rule: ' + str(bins))
	return bins

# Returns the number of bins with Square root choice
def getBinsSquareRootChoice(numberOfSamples):
	bins = math.ceil(math.sqrt(numberOfSamples))
	print('Number of bins with Square-root choice: ' + str(bins))
	return bins

# Returns interquartile range
def calcIQR(list):
	firstQuartile = np.percentile(list, 25)
	thirdQuartile = np.percentile(list, 75)
	return thirdQuartile - firstQuartile

# Returns the number of bins with Freedman-Diaconis choice
def getBinsFreedmanDiaconisChoice(numberOfSamples, list):
	binWidth = 2*(calcIQR(list)/(numberOfSamples**(1/3.0)))
	maximum = max(list)
	minimum = min(list)
	bins = math.ceil((maximum-minimum)/binWidth)
	print('Number of bins with Freedman-Diaconis rule ' + str(bins))
	return bins

# Plots and returns the histogram with given data and number of bins
def plotHistogram(attributeData, numberOfBins, attributeName, binSelectionMethod, plotColor):
	figure = plt.figure()
	plt.hist(attributeData, bins=numberOfBins, color=plotColor)
	plt.title(attributeName.capitalize() + '. Bins: ' + str(binSelectionMethod))
	return figure

# Saves the given figure
def saveFigure(figure, filename):
	currentPath = os.path.dirname(os.path.abspath(__file__))
	figuresPath = os.path.join(currentPath, 'figures')
	taskFigurePath = os.path.join(figuresPath, 'task1')
	_filename = os.path.join(taskFigurePath, filename)
	figure.savefig(_filename)
	print('Saved ' + filename)

data = WhiteWineData()

for i in range(0, len(data.attrList)):
	attribute = data.attrList[i]
	attributeName = data.attributeNames[i]

	# Plot and save histogram, bin selection used: Freedman Diaconis method
	binSelectionMethod = 'Freedman Diaconis method'
	figureFRM = plotHistogram(attribute, getBinsFreedmanDiaconisChoice(data.numberOfSamples, attribute), attributeName, binSelectionMethod, 'green')
	saveFigure(figureFRM, attributeName + '_' + binSelectionMethod + '.png')

	# Plot and save histogram, bin selection used: Sturges Rule
	binSelectionMethod = 'Sturges rule'
	figureSR = plotHistogram(attribute, getBinsSturgesRule(data.numberOfSamples), attributeName, binSelectionMethod, 'blue')
	saveFigure(figureSR, attributeName + '_' + binSelectionMethod + '.png')
	
	# Plot and save histogram, bin selection used: Square root choice
	binSelectionMethod = 'Square root choice'
	figureSRC = plotHistogram(attribute, getBinsSquareRootChoice(data.numberOfSamples), attributeName, binSelectionMethod, 'red')
	saveFigure(figureSRC, attributeName + '_' + binSelectionMethod + '.png')