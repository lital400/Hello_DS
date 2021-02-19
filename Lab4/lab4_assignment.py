# Author: Lital Israel
# Course: CAP 4784
# 2/11/21
# Lab 4 - Analyzing BRFSS Data

import numpy as np

my_data = np.genfromtxt('brfss-cdc.csv', dtype=int, delimiter=',', skip_header=1)

print("First Five Rows of the Data:\n", my_data[:5, :])
print("Shape of the data: ", my_data.shape)

currentWeight = my_data[:, 2:3]
weightYrAgo = my_data[:, 3:4]
weightChange = currentWeight - weightYrAgo

print("\nDescriptive Statistics for Weight Change Data:")
print("Mean: {:.2f}".format(np.mean(weightChange)))
print("Median:", np.median(weightChange))
print("Standard Deviation: {:.2f}".format(np.std(weightChange)))
q75, q25 = np.percentile(weightChange, [75, 25])
print("Interquartile Range:", q75 - q25)

concatArray = np.column_stack((my_data, weightChange))
print("\nFirst Five Rows of the Data with Weight Changes:\n", concatArray[:5, :])
print("Shape of the data: ", concatArray.shape)

maleFemaleSplit = [concatArray[concatArray[:, 5] == k] for k in np.unique(concatArray[:, 5])]

print("\nFirst Five Rows of the Data relevant to Males:\n", maleFemaleSplit[0][:5, :])
print("Shape of the data: ", maleFemaleSplit[0].shape)

print("\nDescriptive Statistics for Data relevant to Males:")
print("Mean: {:.2f}".format(np.mean(maleFemaleSplit[0])))
print("Median:", np.median(maleFemaleSplit[0]))
print("Standard Deviation: {:.2f}".format(np.std(maleFemaleSplit[0])))
q75, q25 = np.percentile(maleFemaleSplit[0], [75, 25])
print("Interquartile Range:", q75 - q25)

print("\nFirst Five Rows of the Data relevant to Females:\n", maleFemaleSplit[1][:5, :])
print("Shape of the data: ", maleFemaleSplit[1].shape)

print("\nDescriptive Statistics for Data relevant to Females:")
print("Mean: {:.2f}".format(np.mean(maleFemaleSplit[1])))
print("Median:", np.median(maleFemaleSplit[1]))
print("Standard Deviation: {:.2f}".format(np.std(maleFemaleSplit[1])))
q75, q25 = np.percentile(maleFemaleSplit[1], [75, 25])
print("Interquartile Range:", q75 - q25)
