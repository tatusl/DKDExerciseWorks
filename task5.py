import numpy as np
import matplotlib.pyplot as plt
import pandas
from whiteWineData import WhiteWineData

dataframe = pandas.read_csv('winequality-white.csv', sep=';')

pearsonCorrTable = dataframe.corr(method='pearson')

kendallCorrTable = dataframe.corr(method='kendall')

with open('pearson.html', 'w') as writer:
	writer.write(pearsonCorrTable.to_html())

with open('kendallTau.html', 'w') as writer:
	writer.write(kendallCorrTable.to_html())

#print(asHtml)


#print(kendallCorrTable)