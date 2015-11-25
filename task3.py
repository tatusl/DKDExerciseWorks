import numpy as np
import matplotlib.pyplot as plt
import math

from whiteWineData import WhiteWineData

# Save data to numpy array
numpyArray = np.array(WhiteWineData().wholeData).astype(np.float)

# Calculate covariance matrix
covMatrix = np.cov(numpyArray.T)

