
import tools.placeFigures as pf

import os
os.chdir('../')


### Begin

from kCells import Node, Edge, Face, Volume
from complex import PrimalComplex3D,DualComplex3D

# Nodes
n0 = Node(0,0,0)
n1 = Node(1,0,0)
n2 = Node(0,1,0)
n3 = Node(0,0,1)
nodes = [n0,n1,n2,n3]

# Edges
e0 = Edge(n0,n1)
e1 = Edge(n0,n2)
e2 = Edge(n0,n3)
e3 = Edge(n1,n2)
e4 = Edge(n1,n3)
e5 = Edge(n2,n3)
edges = [e0,e1,e2,e3,e4,e5]

# Faces
f0 = Face([e0,e4,-e2])
f1 = Face([e3,e5,-e4])
f2 = Face([e0,e3,-e1])
f3 = Face([e1,e5,-e2])
faces = [f0,f1,f2,f3]

# Volume
v0 = Volume([f0,f1,-f2,-f3])
volumes = [v0,]


pc = PrimalComplex3D(nodes,edges,faces,volumes)
dc = DualComplex3D(pc)

pic1 = pc.plotComplexTikZ()
pic1.scale=5
pic1.writeLaTeXFile('latex','Hirschberg2019-1')

pic2 = dc.plotComplexTikZ()
pic2.scale=5
pic2.writeLaTeXFile('latex','Hirschberg2019-2',True,True)

#pc.tikzScale = 3
#pc.writeTikZ('exampleHirschberg',color=True)
#print(dc.incidenceMatrix3)


### End


(figs,axes) = pf.getFigures()
pc.plotComplex(axes[0])
dc.plotComplex(axes[1],plotFaces=True)


