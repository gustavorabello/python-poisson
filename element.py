## =================================================================== ##
#  this is file model.py, created at 18-Feb-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##


import numpy as np

class linElement:

 def __init__(self):

  self.kxxc = np.zeros( [3,3],dtype=float )
  self.kyyc = np.zeros( [3,3],dtype=float )

  self.gqPoints = np.array([ 
               [0.33333333333333,0.33333333333333,0.33333333333333],
               [0.60000000000000,0.20000000000000,0.20000000000000],
               [0.20000000000000,0.60000000000000,0.20000000000000],
               [0.20000000000000,0.20000000000000,0.60000000000000] ])
                       
  self.gqWeights = np.array( [-0.562500000000000,
                               0.520833333333333,
                               0.520833333333333,
                               0.520833333333333] )

  self.phiJ = np.array([ [0.33333333333333,0.33333333333333,0.33333333333333],
                         [0.60000000000000,0.20000000000000,0.20000000000000],
                         [0.20000000000000,0.60000000000000,0.20000000000000],
                         [0.20000000000000,0.20000000000000,0.60000000000000] ])
                       
  self.dphiJdl1 = np.array([ [1.0, 0.0,-1.0],
                             [1.0, 0.0,-1.0],
                             [1.0, 0.0,-1.0],
                             [1.0, 0.0,-1.0] ])

  self.dphiJdl2 = np.array([ [0.0,1.0,-1.0],
                             [0.0,1.0,-1.0],
                             [0.0,1.0,-1.0],
                             [0.0,1.0,-1.0] ])


 def getK(self,m,v1,v2,v3 ):

  v = np.array( [v1,v2,v3] )
  jacobian = m.X[v3]*( m.Y[v1]-m.Y[v2] )+m.X[v1]*( m.Y[v2]-m.Y[v3] )+m.X[v2]*( -m.Y[v1]+m.Y[v3] )

  localx = np.zeros([4,1])
  localy = np.zeros([4,1])
  for k in range(0,4):
   valx = 0.0
   valy = 0.0
   for i in range(0,3):
    valx += m.X[v[i]] * self.phiJ[k,i]
    valy += m.Y[v[i]] * self.phiJ[k,i]
   localx[k] = valx
   localy[k] = valy

  dxdl1 = np.zeros([4,1])
  dxdl2 = np.zeros([4,1])
  dydl1 = np.zeros([4,1])
  dydl2 = np.zeros([4,1])
  for k in range(0,4):
   valxl1 = 0.0
   valxl2 = 0.0
   valyl1 = 0.0
   valyl2 = 0.0
   for i in range(0,3):
    valxl1 += m.X[v[i]]*self.dphiJdl1[k,i]
    valxl2 += m.X[v[i]]*self.dphiJdl2[k,i]
    valyl1 += m.Y[v[i]]*self.dphiJdl1[k,i]
    valyl2 += m.Y[v[i]]*self.dphiJdl2[k,i]
   dxdl1[k] = valxl1
   dxdl2[k] = valxl2
   dydl1[k] = valyl1
   dydl2[k] = valyl2

  dphiJdx = np.zeros([4,3])
  dphiJdy = np.zeros([4,3])
  for k in range(0,4):
   for i in range(0,3):
    dphiJdx[k,i] = (self.dphiJdl1[k,i]*dydl2[k]-self.dphiJdl2[k,i]*dydl1[k])/jacobian
    dphiJdy[k,i] = (-self.dphiJdl1[k,i]*dxdl2[k]+self.dphiJdl2[k,i]*dxdl1[k])/jacobian

  self.kxxc = np.zeros([3,3])
  self.kyyc = np.zeros([3,3])
  for k in range(0,4):
   for i in range(0,3):
    for j in range(0,3):
     self.kxxc[i,j] += dphiJdx[k,i]*dphiJdx[k,j]*jacobian*self.gqWeights[k];
     self.kyyc[i,j] += dphiJdy[k,i]*dphiJdy[k,j]*jacobian*self.gqWeights[k];

