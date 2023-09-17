# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Wed Apr 18 16:14:47 2018




#==============================================================================
#    IMPORTS
#==============================================================================
import os
os.chdir('../')

from kCells import Node
from kCells import Edge
from kCells import Face
from kCells import Volume
import tools.placeFigures as pf
from complex import PrimalComplex3D, DualComplex3D
from tools import MyLogging
import matplotlib.pyplot as plt
import tools.colorConsole as cc
import tools.tumcolor as tc




#==============================================================================
#    CREATE GEOMETRY
#==============================================================================

with MyLogging('ExampleDualFace'):
    
#-------------------------------------------------------------------------
#    Nodes
#-------------------------------------------------------------------------       
    
    n0 = Node(4,4,2)
    n1 = Node(0,0,0)
    n2 = Node(2,0,0)
    n3 = Node(4,0,0)
    n4 = Node(0,2,0)
    n5 = Node(2,2,0)
    n6 = Node(4,2,0)
    n7 = Node(0,4,0)
    n8 = Node(2,4,0)
    n9 = Node(4,4,0)
    n10 = Node(0,0,2)
    n11 = Node(2,0,2)
    n12 = Node(4,0,5)
    n13 = Node(0,2,2)
    n14 = Node(2,2,2)
    n15 = Node(4,2,2)
    n16 = Node(0,4,2)
    n17 = Node(2,4,2)
    
    nodes = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17]
    
#-------------------------------------------------------------------------
#    Edges
#-------------------------------------------------------------------------       
    
    e1 = Edge(n1,n2)
    e2 = Edge(n2,n3)
    e3 = Edge(n4,n5)
    e4 = Edge(n5,n6)
    e5 = Edge(n7,n8)
    e6 = Edge(n8,n9)
    e7 = Edge(n10,n11)
    e8 = Edge(n11,n12)
    e9 = Edge(n13,n14)
    e10 = Edge(n14,n15)
    e11 = Edge(n16,n17)
    e12 = Edge(n17,n0)
    e13 = Edge(n1,n4)
    e14 = Edge(n2,n5)
    e15 = Edge(n3,n6)
    e16 = Edge(n4,n7)
    e17 = Edge(n5,n8)
    e18 = Edge(n6,n9)
    e19 = Edge(n10,n13)
    e20 = Edge(n11,n14)
    e21 = Edge(n12,n15)
    e22 = Edge(n13,n16)
    e23 = Edge(n14,n17)
    e24 = Edge(n15,n0)
    e25 = Edge(n1,n10)
    e26 = Edge(n2,n11)
    e27 = Edge(n3,n12)
    e28 = Edge(n4,n13)
    e29 = Edge(n5,n14)
    e30 = Edge(n6,n15)
    e31 = Edge(n7,n16)
    e32 = Edge(n8,n17)
    e33 = Edge(n9,n0)
    e34 = Edge(n11,n15)
    edges = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34]
    
#-------------------------------------------------------------------------
#    Faces
#-------------------------------------------------------------------------       
    
    f1 = Face([e1,e14,-e3,-e13])
    f2 = Face([e2,e15,-e4,-e14])
    f3 = Face([e3,e17,-e5,-e16])
    f4 = Face([e4,e18,-e6,-e17])
    f5 = Face([e7,e20,-e9,-e19])
    f6 = Face([-e10,-e20,e34])
    f7 = Face([e9,e23,-e11,-e22])
    f8 = Face([e10,e24,-e12,-e23])
    f9 = Face([e1,e26,-e7,-e25])
    f10 = Face([e2,e27,-e8,-e26])
    f11 = Face([e3,e29,-e9,-e28])
    f12 = Face([e4,e30,-e10,-e29])
    f13 = Face([e5,e32,-e11,-e31])
    f14 = Face([e6,e33,-e12,-e32])
    f15 = Face([e13,e28,-e19,-e25])
    f16 = Face([e14,e29,-e20,-e26])
    f17 = Face([e15,e30,-e21,-e27])
    f18 = Face([e16,e31,-e22,-e28])
    f19 = Face([e17,e32,-e23,-e29])
    f20 = Face([e18,e33,-e24,-e30])
    f21 = Face([e21,-e34,e8])
    faces = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21]
    
#-------------------------------------------------------------------------
#    Volumes
#-------------------------------------------------------------------------   
    
    v1 = Volume([-f1,f9,f16,-f11,-f15,f5])
    v2 = Volume([-f2,f10,f17,-f12,-f16,f6,f21])
    v3 = Volume([-f3,f11,f19,-f13,-f18,f7])
    v4 = Volume([-f4,f12,f20,-f14,-f19,f8])
    volumes = [v1,v2,v3,v4]

#-------------------------------------------------------------------------
#    Complex
#-------------------------------------------------------------------------       
    
    c = PrimalComplex3D(nodes,edges,faces,volumes)
    dc = DualComplex3D(c)
   
    
    
#==============================================================================
#    PLOT
#==============================================================================      
    
    (figs,ax) = pf.getFigures(numTotal=6)
            
#-------------------------------------------------------------------------
#    Figure 1: primal graph
#-------------------------------------------------------------------------         
    if True:   
        c.plotComplex(ax[0],showLabel=False)
        plt.figure(figs[0].number)
        plt.title('Nodes and edges of primal graph')

#-------------------------------------------------------------------------
#    Figure 2: border of primal graph
#-------------------------------------------------------------------------     
    if True:
        c.plotBorderFaces(ax[1])
        plt.figure(figs[1].number)
        plt.title('Border of primal graph')
        
#-------------------------------------------------------------------------
#    Figure 3: dual nodes
#-------------------------------------------------------------------------  
        
    if True:
        for e in c.edges:
            e.showLabel = False
            e.plotEdge(ax[2])
        for n in dc.nodes:
            n.showLabel = False
            n.plotNode(ax[2])
            
        for n in dc.additionalBorderNodes:
            n.showLabel = False
            n.color = tc.TUMRose()
            n.plotNode(ax[2])
            
        plt.figure(figs[2].number)
        ax[2].text2D(0.05, 0.95, "inner", transform=ax[2].transAxes,color=dc.nodes[0].color.html)
        ax[2].text2D(0.05, 0.90, "additional border", transform=ax[2].transAxes,color=dc.additionalBorderNodes[0].color.html)
        ax[2].text2D(0.75, 0.875, "primal edges", transform=ax[2].transAxes,color=c.edges[0].color.html)
        plt.title('Dual nodes')
        
        
#-------------------------------------------------------------------------
#    Figure 4: Dual inner and border edges
#-------------------------------------------------------------------------         
    if True:
        numFig=3
        for e in dc.innerEdges+dc.borderEdges:
            e.plotEdge(ax[numFig],showLabel=False)
        plt.figure(figs[numFig].number)
        plt.title('Dual inner and border edges')
        
        
        
#-------------------------------------------------------------------------
#    Figure 5: dual additional border edges
#-------------------------------------------------------------------------
    if True:
        numFig=4
        for e in dc.additionalBorderEdges:
            e.plotEdge(ax[numFig],showLabel=False)
        plt.figure(figs[numFig].number)
        plt.title('Dual additional border edges')
        
        

#-------------------------------------------------------------------------
#    Figure 6: dual inner faces
#-------------------------------------------------------------------------
    if True:
        numFig = 5
        for f in dc.innerFaces:
            f.plotFace(ax[numFig])
        
        c.plotComplex(ax[numFig],showLabel=False)
        
        plt.figure(figs[numFig].number)
        plt.title('Dual face')
        
        





