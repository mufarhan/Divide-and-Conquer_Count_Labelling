import math
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x_axis_labels = [1, 2, 3, 4, 5, 6, 7, 8]
x_tick_labels = ['1', '2', '3', '4', '5', '6', '7', '8']

x_axis_values = [1, 2,	3,	4,	5,	6,	7,	8]

y_axis_values = [[0.604466, 0.371356, 0.272045, 0.221366, 0.192957, 0.167887, 0.153239, 0.147795],
[0.691418, 0.428351, 0.320645, 0.26603, 0.234299, 0.214504, 0.198843, 0.190801],
[2.0035, 1.21796, 0.877157, 0.702703, 0.6017, 0.538009, 0.489509, 0.453528],
[2.08651, 1.24419, 0.899062, 0.701846, 0.62135, 0.540773, 0.495412, 0.463137],
[5.67051, 3.2345, 2.30023, 1.80482, 1.52757, 1.35223, 1.22502, 1.16635],
[5.3916, 3.09275, 2.2011, 1.74318, 1.45474, 1.27396, 1.16387, 1.11221],
[14.8329, 8.47961, 6.07779, 4.83563, 4.14574, 3.70976, 3.44777, 3.26989],
[15.597, 8.90882, 6.36457, 5.06627, 4.32045, 3.86428, 3.57184, 3.38406],
[26.3142, 14.7796, 10.538, 8.28445, 7.08683, 6.26667, 5.78172, 5.49151],
[105.693, 58.5118, 41.8089, 32.9925, 28.1826, 25.0663, 23.5531, 22.7712],
[169.727, 95.419, 69.1548, 54.9942, 47.9982, 43.4825, 40.6506, 39.9403],
[149.85, 84.6224, 61.3668, 49.28, 43.5005, 40.3666, 37.9087, 37.277]]


label_list = [r'NY', r'COL', r'FLA', r'NW', r'NE', r'CAL', r'LKS', r'EUS', r'WUS', r'CUS', r'USA', r'EUR']
color_list = ['r', 'cyan', 'b', 'g', 'yellow', 'magenta', 'grey', 'LightGreen', 'grey', 'm', 'c', 'orange']
line_style = ['o-', 's--', 'v:', '<-', '*--', '^:', 'h-.', '>-', '+--', 'x:', 'p-.', 'd--']

plt.figure(figsize=(3.5,3))

handles = []

plt.xlabel("# of Cores", fontsize=11)
plt.ylabel("Construction Time (sec.)", fontsize=11)

locs, labels = plt.xticks(x_axis_labels, x_tick_labels)
plt.setp(labels)

for i in range(len(y_axis_values)):
  a, = plt.plot(x_axis_values, y_axis_values[i], line_style[i], markersize = 6, label = label_list[i], color = color_list[i], linewidth = 1)
  handles.append(a)
  plt.yscale('log')

plt.figlegend(handles, label_list, bbox_to_anchor=(1.2, 0.98), prop={'size':8}, ncol=1)
locs, labels = plt.xticks(fontsize=9)
locs, labels = plt.yticks(fontsize=9)

plt.tight_layout()
plt.savefig('parallel.pdf', format='pdf', bbox_inches='tight')
plt.savefig('parallel.eps', bbox_inches='tight')
plt.clf()
