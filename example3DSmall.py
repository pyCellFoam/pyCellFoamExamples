# -*- coding: utf-8 -*-
#==============================================================================
# SIMPLE EXAMPLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Thu Dec  7 14:16:21 2017

'''

'''

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
from complex import Complex3D
#import matplotlib.pyplot as plt
import tools.exportLaTeX as tex


#==============================================================================
#    PREPARE PLOT
#==============================================================================
with MyLogging ('simpleExample'):
    (figs,ax) = pf.getFigures(numTotal=8)
#    for a in ax:
#        pf.setAxesEqual(a)

#==============================================================================
#    NODES
#==============================================================================
    # Create nodes at [0,0,0], [1,0,0], [0,1,0] and [0,0,1]
    a = 3
    n0 = Node(0,0,0)
    n1 = Node(a,0,0)
    n2 = Node(0,a,0)
    n3 = Node(0,0,a)
    
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
    
    # Create reversed edge
    me0 = -e0
    me0.plotEdge(ax[1])
    

    
    
#==============================================================================
#    FACES
#==============================================================================
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
    
    #create reversed face
    mf0 = -f0
    mf0.plotFace(ax[1])

#==============================================================================
#    VOLUME
#============================================================================== 
    #Create a volume by defining the border faces
    v0 = Volume([f0,f1,-f2,-f3])
    
    # plot the volume
    v0.plotVolume(ax[2])
    
    volumes = [v0,]
    
    
#==============================================================================
#    FIGURES FOR PRESENTATION
#==============================================================================     
    
    for n in nodes:
        n.plotNode(ax[5])
    for e in edges:
        e.plotEdge(ax[5])
    pf.setAxesEqual(ax[5])
    pf.exportPNG(figs[5],'2018-09-18_tetrahedron_incidenc1')
        
    

#    plt.figure(figs[0].number)
#    fig = plt.gcf()
#    fig.set_size_inches(5,4)
#    plt.savefig('2018-09-18_tetrahedron_nodes_edges',dpi=300,transparent=True)        
    
    for e in edges:
        e.plotEdge(ax[6])
    for f in faces:
        f.plotFace(ax[6])
        
    pf.setAxesEqual(ax[6])
    pf.exportPNG(figs[6],'2018-09-18_tetrahedron_incidenc2')
        
    for f in faces:
        f.plotFace(ax[7])
#    for v in volumes:
#        v.plotVolume(ax[7])
        
    pf.copylimits(ax[6],ax[7])
    pf.exportPNG(figs[7],'2018-09-18_tetrahedron_incidenc3')
    
    
    c1 = Complex3D(nodes,edges,faces,volumes)
#    print(tex.array2bmatrix(c1.incidenceMatrix1))
#    print(tex.array2bmatrix(c1.incidenceMatrix2))
#    print(tex.array2bmatrix(c1.incidenceMatrix3))
#    
#    print(np.dot(c1.incidenceMatrix1,c1.incidenceMatrix2))
#    cc.printBlue('Incidence matrix')
#    print(c1.incidenceMatrix1)
#    c1.plotIncidence1(figs[3])
#    
#    c1.plotComplex(ax[4])
#    
#    
#    
#    plt.figure(figs[0].number)
#    fig = plt.gcf()
#    plt.savefig('2018-09-18_tetrahedron_faces',dpi=300,transparent=True)
#    print(tex.array2Tabular(c1.incidenceMatrix1))
#    
#    
#    plt.figure(figs[0].number)
#    fig = plt.gcf()
#    fig.set_size_inches(5,4)
#    plt.savefig('2018-09-18_tetrahedron_nodes_edges',dpi=300,transparent=True)
    
    
    
    
    
