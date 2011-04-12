## =================================================================== ##
#  this is file main.py, created at 11-Apr-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

import mesh as mes
import simulator as sim

mesh=mes.Mesh(4,4)
mesh.boundaryConditions()

s1=sim.Simulator(mesh)
s1.matrixAssemble()
print s1.K




