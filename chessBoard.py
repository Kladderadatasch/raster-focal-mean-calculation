import numpy as np
import matplotlib.pyplot as mp

rows = 8
cols = 8

ChessArray = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        ChessArray[i,j]=i+j
        if ChessArray[i,j] % 2 == 0:
            ChessArray[i,j] = 0
        else:
            ChessArray[i,j] = 1
            
mp.imshow(ChessArray, cmap='Greys', interpolation='none')
mp.xticks(1)