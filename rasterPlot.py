

'''
A simple example of plotting
a raster dataset to screen
'''

#########################################
import numpy as np
import matplotlib.pyplot as plt


#########################################

if __name__=="__main__":
  # make a nonesense dataset as a numpy array
  cols=100   # number of x dimensions
  rows=100   # number of y dimensions
  dataset=np.random.rand(cols,rows)

  # plot that datset to screen with matplotlib
  plt.imshow(dataset)
  plt.show()

