import csv
import numpy as np
import matplotlib.pyplot as plt
import math

csvPath = "winequality-white.csv"

#Init input attribute values
fixedAcidity, volatileAcidity, citricAcid = [], [], []
residualSugar, chlorides, freeSulfurDioxide = [], [], []
totalSulfurDioxide, Density, pH = [], [], []
sulphates, alcohol = [], [], 

#Init outout attribute value
quality = []

#Calculate number of lines in csv file
numberOfLines = len(list(csv.reader(open('winequality-white.csv'))))

#Number of samples, subtract the attribute name line
n = numberOfLines-1

#Add attributes to attributes list
attrList = [fixedAcidity, volatileAcidity, citricAcid, residualSugar, chlorides, freeSulfurDioxide, totalSulfurDioxide, Density, pH, sulphates, alcohol, quality]

#Read attributes values to corresponding attribute variable from the csv file
with open(csvPath) as csvfile:
	data = csv.reader(csvfile, delimiter=';')
	firstLine = True
	for row in data:
		if firstLine:
			firstLine = False
			continue
		for i in range(0, len(attrList)):
			attrList[i].append(float(row[i]))
	csvfile.close()

#Returns the number of bins with Sturges rule
def getBinsSturgesRule(numberOfSamples):
	return math.ceil(math.log(numberOfSamples, 2) + 1)

#Returns the number of bins with Square root choice
def getBinsSquareRootChoice(numberOfSamples):
	return math.ceil(math.sqrt(numberOfSamples))

#Returns interquartile range
def calcIQR(list):
	firstQuartile = np.percentile(list, 25)
	thirdQuartile = np.percentile(list, 75)
	return thirdQuartile - firstQuartile

#Returns the number of bins with Freedman-Diaconis choice
def getBinsFreedmanDiaconisChoice(numberOfSamples, list):
	return 2*(calcIQR(list)/(numberOfSamples**(1/3.0)))

def plotHistogram(attributeData, numberOfBins):
	plt.figure()
	plt.hist(attributeData, bins=numberOfBins, color="green")
	plt.title("lol")
	plt.show()

print(calcIQR(fixedAcidity))
print(getBinsFreedmanDiaconisChoice(n, fixedAcidity))
plotHistogram(fixedAcidity, getBinsSturgesRule(n))