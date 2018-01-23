#!/usr/local/bin/python

#Brooke Davis
#Prog1

import matplotlib.pyplot as plt
import csv
x = []
y = []

with open('cars04.csv','r') as csvfile:
	plots = csv.DictReader(csvfile)
	for row in plots:
		if row['City MPG'] != '*':
			x.append(int(row['City MPG']))
			y.append(int(row['HP']))

plt.plotfile(x,y)
plt.axis([0, 6, 0, 20])
plt.savefig('foo.png', bbox_inches='tight')
