# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Sun Oct 17 15:46:11 2021

'''


'''
#==============================================================================
#    IMPORTS
#==============================================================================
#-------------------------------------------------------------------------
#    Change to Main Directory
#-------------------------------------------------------------------------
from tools.myLogging import MyLogging
import tools.colorConsole as cc
import tools.placeFigures as pf

from kCells import Node, Edge, Face
from complex import PrimalComplex2D, DualComplex2D






    
with MyLogging('Template'):

#-------------------------------------------------------------------------
#    Create some examples
#-------------------------------------------------------------------------
    
    n0  = Node(1  , 0  , 0)
    n1  = Node(2  , 0  , 0)
    n2  = Node(0  , 1  , 0)
    n3  = Node(1  , 0.7, 0)
    n4  = Node(2  , 1  , 0)
    n5  = Node(3  , 1  , 0)
    n6  = Node(0  , 2  , 0)
    n7  = Node(1  , 2  , 0)
    n8  = Node(2.7, 2.2, 0)
    n9  = Node(3.0, 2.3, 0)
    n10 = Node(1.5, 3  , 0)
    n11 = Node(0  , 0  , 0)
    n12 = Node(3  , 0  , 0)
    n13 = Node(0  , 3  , 0)
    n14 = Node(3  , 3  , 0)
    
    nodes = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14]
    
    
    e0  = Edge( n0, n3)
    e1  = Edge( n1, n4)
    e2  = Edge( n2, n3)
    e3  = Edge( n3, n4)
    e4  = Edge( n4, n5)
    e5  = Edge( n3, n7)
    e6  = Edge( n4, n7)
    e7  = Edge( n4, n8)
    e8  = Edge( n7, n8)    
    e9  = Edge( n7,n10)
    e10 = Edge( n8, n9)
    e11 = Edge( n6, n7)
    e12 = Edge( n0, n2, geometricNodes=n11)
    e13 = Edge( n0, n1)
    e14 = Edge( n1, n5, geometricNodes=n12)
    e15 = Edge( n5, n9)
    e16 = Edge( n9,n10, geometricNodes=n14)
    e17 = Edge( n6,n10, geometricNodes=n13)
    e18 = Edge( n2 ,n6)
    
    edges = [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18]
    
    
    
    f0 = Face([e0,-e2,-e12])
    f1 = Face([e13,e1,-e3,-e0])
    f2 = Face([e14,-e4,-e1])
    f3 = Face([e2,e5,-e11,-e18])
    f4 = Face([e3,e6,-e5])
    f5 = Face([e7,-e8,-e6])
    f6 = Face([e4,e15,-e10,-e7])
    f7 = Face([e10,e16,-e9,e8])
    f8 = Face([e9,-e17,e11])
    
    faces = [f0,f1,f2,f3,f4,f5,f6,f7,f8]
    
    
    # for f in [f0,f1,f2,f3,f6,f7,f8]:
    for f in [f0,f1,f2]:
        f.category1 = 'border'
    
    
    pc = PrimalComplex2D(nodes,edges,faces)
    dc = DualComplex2D(pc)
    




#-------------------------------------------------------------------------
#    Plotting
#-------------------------------------------------------------------------    

    # Choose plotting method. Possible choices: pyplot, VTK, TikZ, animation, doc, None
    plottingMethod = 'pyplot'
    
    
#    Disabled
#--------------------------------------------------------------------- 
    if plottingMethod is None or plottingMethod == 'None':
        cc.printBlue('Plotting disabled')
    
#    Pyplot
#---------------------------------------------------------------------         
    elif plottingMethod == 'pyplot':
        cc.printBlue('Plot using pyplot')
        (figs,axes) = pf.getFigures()
        for n in nodes:
            n.plotNode(axes[0])
        for e in edges:
            e.plotEdge(axes[0])
            
        for f in faces:
            f.plotFace(axes[0],showNormalVec = False)
            
            
        pc.plotComplex(axes[0])
        dc.plotComplex(axes[1])
            
        axes[0].view_init(90,-90)
        
        

#    VTK
#--------------------------------------------------------------------- 
    elif plottingMethod == 'VTK' :
        cc.printBlue('Plot using VTK')
        cc.printRed('Not implemented')

#    TikZ
#--------------------------------------------------------------------- 
    elif plottingMethod == 'TikZ' :
        cc.printBlue('Plot using TikZ')            
        cc.printRed('Not implemented')
        
#    Animation
#--------------------------------------------------------------------- 
    elif plottingMethod == 'animation':
        cc.printBlue('Creating animation')
        cc.printRed('Not implemented')
        
#    Documentation
#--------------------------------------------------------------------- 
    elif plottingMethod == 'doc':
        cc.printBlue('Creating plots for documentation')
        test.plotDoc()
        
#    Unknown
#---------------------------------------------------------------------             
    else:
        cc.printRed('Unknown plotting method {}'.format(plottingMethod))        
    
    
