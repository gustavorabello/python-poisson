## =================================================================== ##
#  this is file mesh.py, created at 10-Apr-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

import numpy as np

class Mesh:
 "definition of mesh"
 
 def __init__(self,nx,ny):
  numVerts = nx*nx;
  numElems = 18;

  self.numVerts = numVerts
  self.numElems = numElems
  self.X = np.zeros([numVerts],dtype=float)
  self.Y = np.zeros([numVerts],dtype=float)
  self.IEN = np.zeros([numElems,3],dtype=int)
  self.cc = np.zeros([numVerts],dtype=float)
  self.idbcc = np.zeros([0],dtype=int)

  count=0
  for i in range( 0,4 ):
   for j in range( 0,4 ):
    self.X[count] = i * 1.0/(nx-1)
    self.Y[count] = j * 1.0/(ny-1)
    count=count+1

  self.IEN[0] = [0,1,5]
  self.IEN[1] = [0,5,4]
  self.IEN[2] = [1,2,6]
  self.IEN[3] = [1,6,5]
  self.IEN[4] = [2,3,7]
  self.IEN[5] = [2,7,6]
  self.IEN[6] = [4,5,9]
  self.IEN[7] = [4,9,8]
  self.IEN[8] = [5,6,10]
  self.IEN[9] = [5,10,9]
  self.IEN[10] = [6,7,11]
  self.IEN[11] = [6,11,10]
  self.IEN[12] = [8,9,13]
  self.IEN[13] = [8,13,12]
  self.IEN[14] = [9,10,14]
  self.IEN[15] = [9,14,13]
  self.IEN[16] = [10,11,15]
  self.IEN[17] = [10,15,14]

 def boundaryConditions(self):
  for i in range(0,self.numVerts):
   if( self.X[i] == self.X.min() ):
    self.cc[i] = 0
    self.idbcc = np.append(self.idbcc,i)
   if( self.X[i] == self.X.max() ):
    self.cc[i] = 1
    self.idbcc = np.append(self.idbcc,i)
   if( self.Y[i] == self.Y.min() and self.X[i] > self.X.min() and self.X[i] < self.X.max() ):
    self.cc[i] = 4
    self.idbcc = np.append(self.idbcc,i)
   if( self.Y[i] == self.Y.max() and self.X[i] > self.X.min() and self.X[i] < self.X.max() ):
    self.cc[i] = 6
    self.idbcc = np.append(self.idbcc,i)

