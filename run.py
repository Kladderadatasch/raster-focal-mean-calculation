import RasterHandler as RH 
import matplotlib.pyplot as mp
import numpy as np
import argparse

#mp.imshow(RH.readRaster('./data/RasterExample1.txt').getData())

def readCommands():
  '''
  Get commandline arguments
  '''
  
  #Sets a default Path if nothing else is specified
  p = argparse.ArgumentParser(description=("Computing and Plotting the focal Mean of a given Raster"), formatter_class=argparse.RawTextHelpFormatter)
  p.add_argument("--path", dest ="PathRastArray", type=str, default='./data/RasterExample1.txt', help=("Specify the Path to your Raster in txt format"))
  cmdargs = p.parse_args()
  return cmdargs

def focalMean_fun(PathRastArray):
    
#    calls the RasterHandler Module
    raster = RH.readRaster(PathRastArray)
    data = raster.getData()
    rows = raster.getRows()
    cols = raster.getCols()
    
    #creates a second array. which is is of the size of the original one
    #and filled with zeros which will be overwritten
    focalMean = np.zeros((rows,cols))
    
    for i in range(rows):
        for j in range(cols):
    
            focalSum = 0
            cellsVisited = 0
            
            #Creates a window, which covers 5x5 Pixels
            #The window is moved along the Raster and inside the mean of the window
            #is created
            for ii in range(i-2, i+3):
                for jj in range(j-2, j+3):
                    
                    #The window moves as long as it does not cross the outlines
                    #of the original Array. Without the condition it would move
                    #infinitely. Every movement is counted as cellsVisited
                    
                    if (ii>-1 and ii<cols and jj>-1 and jj<cols):
                        focalSum = focalSum+data[ii,jj]
                        cellsVisited=cellsVisited+1
            
            #Finally, the mean is calculated by the total Sums of the values in the windows
            #divided by the number of cells used for the calculation
            
            if cellsVisited >0:
                focalMean[i,j]=focalSum/cellsVisited
                
    return(data, focalMean)

def plotMean(data, focalMean):
    mp.imshow(data)
    mp.show()
    mp.imshow(focalMean)
    mp.show()

if __name__ == 'main':
    cmdArgs = readCommands()
    data,focalMean = focalMean_fun(cmdArgs.PathRastArray)
    plotMean(data,focalMean)
    