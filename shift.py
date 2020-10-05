# -*- coding: utf-8 -*-
"""
@author: Anna Galsanova
"""
import numpy as np
 
def read(filename):
    t = []
    file = open(filename)
    lines = file.readlines()
    file.close()
    for line in lines[2:]:
        l = line.split()
        t.append(l)
 
    image = np.array(t, dtype='int32')
    return image
 
 
def coord(image):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y, x] == 1:
                return y, x
 
 
y1, x1 = coord(read('img1.txt'))
y2, x2 = coord(read('img2.txt'))
 
_y = y2-y1
_x = x2-x1
print('сдвиг по у:',_y, '\nсдвиг по х:',_x)
