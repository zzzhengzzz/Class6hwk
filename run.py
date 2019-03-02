#!/usr/bin/env python

import os
import os.path as op
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from argparse import ArgumentParser

parser = ArgumentParser(description='A CSV reader + stats maker')
parser.add_argument('csvfile',
                    type=str,
                    help='Path to the input csv file.')

parsed_args = parser.parse_args()
my_csv_file = parsed_args.csvfile

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None)
print(data.head())

print(data.shape)

print(np.mean(data))
print(np.std(data))
print(np.average(data))

# Add headers to the table
header_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 
'MEDV']
headerdata = pd.read_csv(my_csv_file, sep='\s+|,', header=None, names=header_names)

print(headerdata)

#VISUALIZE DATA:

# Visulaize Histogram of each feature
# - histogram AGE colum

plt.figure(figsize=(10, 10))
plt.hist(data.iloc[:, 6], bins=10, rwidth=0.9)
plt.savefig("histo_age.png", dpi=100)
plt.show()

# - Scatter Age&MEDV
plt.scatter(data.iloc[:, 6], data.iloc[:, -1])
plt.savefig("scatter_age_medv", dpi=100)
plt.show()


