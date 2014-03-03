# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 01:06:28 2014

@author: doyung
"""
import matplotlib.pyplot as plt

plt.plot([10,11,12,13], [14,13,7,6], 'b')
plt.plot([10,11,12], [14,13,7], 'bo')
plt.text(13.2, 10, 'dont', color='b')

plt.plot([10,11,12,13], [10,5,6,7], 'r')
plt.plot([13], [7], 'ro')
plt.text(13.2, 9, 'can', color='r')

plt.plot([10,11,12,13], [7,2,9,7], 'g')
plt.plot([12,13], [9,7], 'go')
plt.text(13.2, 8, 'never', color='g')

plt.plot([10,11,12,13], [12,9,8,4], 'k')
plt.plot([10,11,12], [12,9,8], 'ko')
plt.text(13.2, 7, 'know', color='k')

plt.plot([10,11,12,13], [10,9,7,4], 'y')
plt.plot([11,12], [9,7], 'yo')
plt.text(13.2, 6, 'love', color='y')

plt.plot([10,11,12,13], [11,7,7,7], 'm')
plt.plot([10,11,12,13], [11,7,7,7], 'mo')
plt.text(13.2, 5, 'now', color='m')

plt.plot([10,11,12,13], [12,8,3,6], 'c')
plt.plot([10,11,12,13], [12,8,3,6], 'co')
plt.text(13.2, 4, 'make', color='c')

plt.axis([10, 15, 0, 20])
plt.xlabel('Years (20--)')
plt.ylabel('Number of Times Mentioned')
plt.title('Most Common Words in Top Singles')
plt.show()