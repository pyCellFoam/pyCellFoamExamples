# -*- coding: utf-8 -*-
#==============================================================================
# EXAMPLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Fri Mar 29 16:16:41 2019



import os
os.chdir('../')

#==============================================================================
#    IMPORTS
#==============================================================================
from kCells import Node
from kCells import Edge
from kCells import Face
from kCells import Volume
from tools import MyLogging
import tools.placeFigures as pf
import tools.colorConsole as cc
from complex import DualComplex3D
import grids.grid3DKelvin as kelvin 
import tools.incidenceMatrix as iM

    

#==============================================================================
#    PREPARE PLOT
#==============================================================================
with MyLogging ('Presentation'):
    (figs,ax) = pf.getFigures(numTotal=9)

#==============================================================================
#    NODES
#==============================================================================
    # Create nodes at [0,0,0], [1,0,0], [0,1,0] and [0,0,1]
    n0 = Node(0,0,0)
    n1 = Node(1,0,0)
    n2 = Node(0,1,0)
    n3 = Node(0,0,1)
    
    # put all nodes in a list to simplify handling:
    nodes = [n0,n1,n2,n3]
    
    # plot all nodes
    for n in nodes:
        n.plotNode(ax[0])
            
        
        
#==============================================================================
#    EDGES
#==============================================================================
    # Create some edges by defining their endpoints
    e0 = Edge(n0,n1)
    e1 = Edge(n0,n2)
    e2 = Edge(n0,n3)
    e3 = Edge(n1,n2)
    e4 = Edge(n1,n3)
    e5 = Edge(n2,n3)
    
    
    # Put them in a list, too
    edges = [e0,e1,e2,e3,e4,e5]
    
    # plot all edges
    for e in edges:
        e.plotEdge(ax[0])
        
    # check the node
    cc.printBlue('Edges that are connectd to node',n0)
    cc.printWhite(n0.edges)
    
    
    # Calculate incidence matrix
    print(iM.calcIncidence1(nodes,edges))
    
    # Create reversed edge
    me0 = -e0
    me0.plotEdge(ax[1])
    

    
    
#==============================================================================
#    FACES
#==============================================================================
    
    # Choose some edges that can define a face
    tempEdges = [e0,e4,e2] 
    for e in tempEdges:
        e.plotEdge(ax[2])
    
    
    # Create faces by defining the border edges
    f0 = Face([e0,e4,-e2])
    f1 = Face([e3,e5,-e4])
    f2 = Face([e0,e3,-e1])
    f3 = Face([e1,e5,-e2])
    
    # Put faces in a list, we've seen that before ;)
    faces = [f0,f1,f2,f3]
    
    # Plot the faces
    for f in faces:
        f.plotFace(ax[0])
        
    # Check the edge
    cc.printBlue('Faces that are connectd to edge',e1)
    cc.printWhite(e1.faces)
 
    
    # Calculate incidence matrix
    print(iM.calcIncidence2(edges,faces))
    
    #create reversed face
    mf0 = -f0
    mf0.plotFace(ax[1])

#==============================================================================
#    VOLUME
#============================================================================== 
    # Create a volume by defining the border faces
    v0 = Volume([f0,f1,-f2,-f3])
    
    volumes = [v0,]
    
    # plot the volume
    v0.plotVolume(ax[3])

    # Calculate incidence matrix
    print(iM.calcIncidence3(faces,volumes))    
    
#==============================================================================
#    DUAL COMPLEX
#==============================================================================     
    (c,_,_) = kelvin.getComplex(0,0,0)
    c.plotComplex(ax[4],showLabel=False)
    dc = DualComplex3D(c)
    
#==============================================================================
#    DUAL  NODES
#==============================================================================  
        
    
    c.plotComplex(ax[5],plotNodes=False,plotEdges=False,plotFaces=False,plotVolumes=True,showLabel=False,showBarycenter=False)
    dc.innerNodes[0].plotNode(ax[5])
    dc.plotComplex(ax[5],plotNodes=True,plotEdges=False,plotFaces=False,plotVolumes=False,showLabel=False)


#==============================================================================
#    DUAL  EDGES
#============================================================================== 
    
    c.plotComplex(ax[6],plotNodes=False,plotEdges=False,plotFaces=False,plotVolumes=True,showLabel=False,showBarycenter=False)
    dc.innerEdges[0].plotEdge(ax[6])
    dc.innerEdges[0].dualCell3D.plotFace(ax[6])
    dc.plotComplex(ax[6],plotNodes=False,plotEdges=True,plotFaces=False,plotVolumes=False,showLabel=False)
    
#==============================================================================
#    DUAL  FACES
#==============================================================================    
    

    c.plotComplex(ax[7],plotNodes=False,plotEdges=False,plotFaces=False,plotVolumes=True,showLabel=False,showBarycenter=False)
    dc.innerFaces[0].plotFace(ax[7])
    dc.innerFaces[0].dualCell3D.plotEdge(ax[7])
    dc.plotComplex(ax[7],plotNodes=False,plotEdges=False,plotFaces=True,plotVolumes=False,showLabel=False,showNormalVec=False,showBarycenter=False)
     
#==============================================================================
#    DUAL  VOLUMES
#==============================================================================    
    c.plotComplex(ax[8],plotNodes=True,plotEdges=False,plotFaces=False,plotVolumes=False,showLabel=False,showBarycenter=False)
    dc.volumes[0].plotVolume(ax[8])
    dc.plotComplex(ax[8],plotNodes=False,plotEdges=False,plotFaces=True,plotVolumes=True,showLabel=False,showNormalVec=False,showBarycenter=False)

    
    

