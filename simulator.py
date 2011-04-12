## =================================================================== ##
#  this is file Simulator.py, created at 11-Apr-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

import element as el
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

class Simulator:

 def __init__(self,m):

  self.m = m
  self.IEN = m.IEN
  self.X = m.X
  self.Y = m.Y
  self.numVerts = m.numVerts
  self.numElems = m.numElems
  self.cc = m.cc
  self.idbcc = m.idbcc
  self.linElem = el.linElement()
  self.K = lil_matrix( (self.numVerts,self.numVerts),dtype=float )

 def matrixAssemble(self):
  
  v = np.zeros([3],dtype=int)

  for self.elem in range(0,self.numElems):
   v[0] = self.IEN[self.elem,0]
   v[1] = self.IEN[self.elem,1]
   v[2] = self.IEN[self.elem,2]

   self.linElem.getK(self.m,v[0],v[1],v[2])

   for i in range(0,3):
    ii=v[i]
    for j in range(0,3):
     jj=v[j]
     self.K[ii,jj] += self.linElem.kxxc[i,j]+self.linElem.kyyc[i,j]


