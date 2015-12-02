import numpy as np
import matplotlib.pyplot as plt
import pandas
from whiteWineData import WhiteWineData

dataframe = pandas.read_csv('winequality-white.csv', sep=';')

pearsonCorrTable = dataframe.corr(method='pearson')

kendallCorrTable = dataframe.corr(method='kendall')

# Write HTML docs

with open('pearson.html', 'w') as writer:
	writer.write(pearsonCorrTable.to_html())

with open('kendallTau.html', 'w') as writer:
	writer.write(kendallCorrTable.to_html())

# Write LaTeX docs
with open('pearson.tex', 'w') as writer:
	writer.write(pearsonCorrTable.to_latex())

with open('kendallTau.tex', 'w') as writer:
	writer.write(kendallCorrTable.to_latex())

#print(asHtml)


#print(kendallCorrTable)