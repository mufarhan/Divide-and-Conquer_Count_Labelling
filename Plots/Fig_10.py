#!/usr/bin/python

import math
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x_axis_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_tick_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

x_axis_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y_axis_values_1 = [[0.715992, 0.795294, 0.828832, 0.826338, 0.761321, 0.704886, 0.616627, 0.48182, 0.376908, 0.315895],
[1.751156, 1.758708, 1.745176, 1.727220, 1.660010, 1.446586, 1.310104, 1.141747, 0.987574, 0.946308]]

y_axis_values_3 = [[0.735393, 0.824023, 0.81756, 0.755751, 0.765541, 0.851117, 0.771198, 0.604875, 0.50512, 0.449319],
[1.608356, 1.621827, 1.632712, 1.708633, 1.717539, 1.355979, 1.070859, 1.086458, 1.163436, 1.153413]]

y_axis_values_4 = [[0.710241, 0.817793, 0.832738, 0.814098, 0.784447, 0.752033, 0.675826, 0.598629, 0.513125, 0.476069],
[1.924166, 1.995519, 2.044724, 2.093843, 2.019099, 1.611735, 1.510709, 1.384427, 1.292834, 1.241825]]

y_axis_values_5 = [[0.597172, 0.707802, 0.806091, 0.816746, 0.830329, 0.840744, 0.711366, 0.608188, 0.526432, 0.493273],
[1.870472, 2.015562, 2.119942, 2.116403, 2.050422, 1.917076, 1.624689, 1.517069, 1.247746, 1.069435]]

y_axis_values_6 = [[0.900586, 1.0151, 1.11434, 1.15163, 1.14218, 1.0994, 0.903652, 0.782894, 0.636065, 0.531778],
[2.189429, 2.278316, 2.381500, 2.397522, 2.331535, 2.208472, 1.822311, 1.604682, 1.351171, 1.203640]]

y_axis_values_7 = [[0.895268, 1.00091, 1.02353, 0.99381, 1.01002, 0.925217, 0.775505, 0.690845, 0.642902, 0.572589],
[2.298558, 2.402059, 2.425752, 2.415789, 2.343469, 1.962896, 1.696986, 1.635058, 1.548349, 1.462679]]

y_axis_values_8 = [[1.13638, 1.31521, 1.43396, 1.44615, 1.47118, 1.47563, 1.23879, 0.998097, 0.728024, 0.570331],
[2.872178, 2.939679, 3.027164, 3.077591, 3.095478, 2.907769, 2.374376, 2.111457, 1.817975, 1.596784]]

y_axis_values_9 = [[1.1517, 1.29522, 1.33759, 1.36048, 1.34136, 1.18318, 1.06163, 0.87577, 0.732832, 0.624647],
[2.716815, 2.821660, 2.841466, 2.809282, 2.806601, 2.367564, 2.088058, 1.826775, 1.619061, 1.477657]]

y_axis_values_10 = [[1.13145, 1.26094, 1.27921, 1.32446, 1.36516, 1.20225, 1.0688, 0.983603, 0.828102, 0.710968],
[2.859822, 2.923972, 2.924540, 2.853819, 2.827056, 2.676410, 2.502084, 2.195363, 1.855405, 1.710937]]

y_axis_values_11 = [[1.50316, 1.70062, 1.75296, 1.84336, 1.88106, 1.66906, 1.52119, 1.25832, 0.997449, 0.875655],
[4.5888666, 4.4577478, 4.6127696, 4.483046, 4.369844, 4.1798206, 3.8023374, 3.490711, 2.6964096, 2.2535916]]

y_axis_values_12 = [[1.5616, 1.75414, 1.82863, 1.89426, 1.89825, 1.70581, 1.58509, 1.3379, 1.05371, 0.841491],
[4.8637362, 4.9689076, 4.8906654, 4.5142728, 4.516604, 4.5619636, 4.2055768, 3.4748918, 2.8049356, 2.441128]]

y_axis_values_13 = [[2.01478, 2.03641, 2.07799, 2.03012, 1.91336, 1.7999, 1.64392, 1.51258, 1.43875, 1.3896],
[5.5373806, 5.4303806, 5.5660398, 5.3558022, 4.5566042, 4.2105756, 3.7419816, 3.2522988, 3.1946052, 2.8961554]]


label_list = [r'DCL', r'TL']

color_list = ['b', 'r']
line_style = ['o-', '<-']

#color_list = ['g', 'b']
#line_style = ['o-', 's--']


plt.figure(figsize=(20,6))

#----------------------------------------------------------

plt.subplot(2,6,1)

plt.title('(NY)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)
plt.ylabel("Query Time ($\mu$s)", fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)

for i in range( len(y_axis_values_1) ):
  plt.plot(x_axis_values, y_axis_values_1[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,2)

plt.title('(COL)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)

for i in range( len(y_axis_values_3) ):
  plt.plot(x_axis_values, y_axis_values_3[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,3)

plt.title('(FLA)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)

for i in range( len(y_axis_values_4) ):
  plt.plot(x_axis_values, y_axis_values_4[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,4)

plt.title('(NW)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_5) ):
  plt.plot(x_axis_values, y_axis_values_5[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,5)

plt.title('(NE)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_6) ):
  plt.plot(x_axis_values, y_axis_values_6[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,6)

plt.title('(CAL)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_7) ):
  plt.plot(x_axis_values, y_axis_values_7[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,7)

plt.title('(LKS)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)
plt.ylabel("Query Time ($\mu$s)", fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_8) ):
  plt.plot(x_axis_values, y_axis_values_8[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,8)

plt.title('(EUS)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_9) ):
  plt.plot(x_axis_values, y_axis_values_9[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,9)

plt.title('(WUS)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_10) ):
  plt.plot(x_axis_values, y_axis_values_10[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,10)

plt.title('(CUS)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_11) ):
  plt.plot(x_axis_values, y_axis_values_11[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,11)

plt.title('(USA)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_12) ):
  plt.plot(x_axis_values, y_axis_values_12[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

#----------------------------------------------------------

plt.subplot(2,6,12)

plt.title('(EUR)', fontsize=25)
plt.xlabel('Query Sets', fontsize=21)

locs, labels = plt.xticks(x_axis_labels,x_tick_labels)
plt.setp(labels)


for i in range( len(y_axis_values_13) ):
  plt.plot(x_axis_values, y_axis_values_13[i], line_style[i], markersize = 9, color = color_list[i], label=label_list[i], linewidth = 1)

locs, labels = plt.xticks(fontsize=14)
locs, labels = plt.yticks(fontsize=14)

plt.legend(loc= 'upper right', prop={'size':14})

plt.tight_layout()
plt.savefig('query_with_varyingdistance_traveltimes.pdf', bbox_inches='tight')
plt.savefig('query_with_varyingdistance_traveltimes.eps', bbox_inches='tight')
plt.clf()
