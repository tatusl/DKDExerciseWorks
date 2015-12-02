import csv
import numpy as np
import matplotlib.pyplot as plt
import math

class WhiteWineData:

	def __init__(self):
		self.csvPath = "winequality-white.csv"

		# Input attribute values
		self.fixedAcidity, self.volatileAcidity, self.citricAcid = [], [], []
		self.residualSugar, self.chlorides, self.freeSulfurDioxide = [], [], []
		self.totalSulfurDioxide, self.density, self.pH = [], [], []
		self.sulphates, self.alcohol = [], []

		# Output attribute value
		self.quality = []

		# List of attributes
		self.attrList = [self.fixedAcidity, self.volatileAcidity, self.citricAcid, self.residualSugar, self.chlorides, self.freeSulfurDioxide, self.totalSulfurDioxide, self.density, self.pH, self.sulphates, self.alcohol, self.quality]

		self.numberOfSamples = self.calcNumberOfSamples()
		self.attributeNames = self.readAttributeNamesFromCsv()
		self.readDataFromCsv()
		self.wholeData = self.constructWholeData()
	
	# Calculates number of samples in data from the csv file
	def calcNumberOfSamples(self):
		numberOfLines = len(list(csv.reader(open(self.csvPath))))
		return numberOfLines-1

	# Reads data to the corresponding attribute variables from the csv file
	def readDataFromCsv(self):
		with open(self.csvPath) as csvfile:
			data = csv.reader(csvfile, delimiter=';')
			# Dirty hack to skip the first line (line with attribute names)
			firstLine = True
			for row in data:
				if firstLine:
					firstLine = False
					continue
				for i in range(0, len(self.attrList)):
					self.attrList[i].append(float(row[i]))
			csvfile.close()

	def constructWholeData(self):
		with open(self.csvPath) as csvfile:
			csvfile.readline()
			data = csv.reader(csvfile, delimiter=';')
			wholeData = []
			for row in data:
				wholeData.append(row)
		return wholeData

	# Read attribute names from the csv
	def readAttributeNamesFromCsv(self):
		csvReader = csv.reader(open(self.csvPath), delimiter=';')
		attributeNames = next(csvReader)
		return attributeNames
