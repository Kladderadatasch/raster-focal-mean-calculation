# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 00:44:33 2013

@author: nrjh
"""
import numpy as np
import RasterHandler 
import matplotlib.pyplot as mp

class Raster(object):
    
    '''A class to represent 2-D Rasters'''

# Basic constuctor method
    def __init__(self,data,xorg,yorg,cellsize,nodata=-999.999):
        self._data=np.array(data)
        self._orgs=(xorg,yorg)
        self._cellsize=cellsize
        self._nodata=nodata
        
    def getData(self):
        return self._data
        
#return the shape of the data array      
    def getShape(self):
        return self._data.shape    
    
    def getRows(self):
        return self._data.shape[0]
        
    def getCols(self):
        return self._data.shape[1]
        
    def getOrgs(self):
        return self._orgs
        
    def getCellsize(self):
        return self._cellsize
    
    def getNoData(self):
        return self._nodata
        

