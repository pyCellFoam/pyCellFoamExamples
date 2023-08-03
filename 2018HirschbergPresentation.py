# -*- coding: utf-8 -*-
#==============================================================================
# GENERATE PICTURES FOR HIRSCHBERG 2018 PRESENTATION
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Thu Dec  7 14:16:21 2017

'''

'''
#==============================================================================
#    IMPORTS
#==============================================================================

#-------------------------------------------------------------------------
#    Change to Main Directory
#-------------------------------------------------------------------------
import os



#-------------------------------------------------------------------------
#    Standard Libraries
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#    Local Libraries
#-------------------------------------------------------------------------


#    kCells
#--------------------------------------------------------------------
from kCells import Node, DualNode1D, DualNode2D, DualNode3D
from kCells import Edge, DualEdge3D, DualEdge2D, DualEdge1D
from kCells import Face, DualFace3D
from kCells import Volume

#    Complex & Grids
#--------------------------------------------------------------------
from complex import PrimalComplex2D, DualComplex2D, DualComplex3D
from grids import Grid3DCubic, Grid2DRectangular

#    Tools
#--------------------------------------------------------------------

from tools import MyLogging
import tools.placeFigures as pf
import tools.colorConsole as cc
import tools.tumcolor as tc






#==============================================================================
#    PREPARE PLOT
#==============================================================================

def doPlots(exportPath,doPlots1=False,doPlots2=False,doPlots3=False,doExports=True,doPrints=True,closeWhenFinished=False): 
    
    
    if not os.path.isdir(exportPath):
        os.makedirs(exportPath, exist_ok=True)
    
    
    axNum = -1
    
    
    (figs,ax) = pf.getFigures(numTotal=12)
    
    
    if doPlots1 and doPlots2:
        doPlots2 = False
        if doPrints:
            cc.printRed('Too many plots - deactivating doPlots2')
    if doPlots1 and doPlots3:
        doPlots3 = False
        if doPrints:
            cc.printRed('Too many plots - deactivating doPlots3')
    if doPlots2 and doPlots3:
        doPlots3 = False
        if doPrints:
            cc.printRed('Too many plots - deactivating doPlots3')
            
            
            
    myRed = tc.TUMcolor([255,0,0],'Red')
    
    
#    for a in ax:
#        pf.setAxesEqual(a)

#==============================================================================
#    NODES
#==============================================================================
    # Create nodes at [0,0,0], [1,0,0], [0,1,0] and [0,0,1]
    
    
    if doPlots1 or doPlots2:
        if doPrints:
            cc.printBlue('Creating nodes')
        a = 3
        n0 = Node(0,0,0)
        n1 = Node(a,0,0)
        n2 = Node(0,a,0)
        n3 = Node(0,0,a)
        
        # put all nodes in a list to simplify handling:
        nodes = [n0,n1,n2,n3]
        
        # plot all nodes
        
        
        if doPlots1:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting nodes in figure {}'.format(axNum+1))
            for n in nodes:
                n.plotNode(ax[axNum])
                
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'01Nodes')
            
            
            
    #==============================================================================
    #    EDGES
    #==============================================================================
                
    #-------------------------------------------------------------------------
    #    Positive edge
    #-------------------------------------------------------------------------
        if doPrints:
            cc.printBlue('Creating edges')
        # Create some edges by defining their endpoints
        e0 = Edge(n0,n1)
        e1 = Edge(n0,n2)
        e2 = Edge(n0,n3)
        e3 = Edge(n1,n2)
        e4 = Edge(n1,n3)
        e5 = Edge(n2,n3)
        
        
        # Put them in a list, too
        edges = [e0,e1,e2,e3,e4,e5]
        
        
        if doPlots1:
        # plot all nodes
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting positive edge in figure {}'.format(axNum+1))
            for n in [n0,n1]:
                n.plotNode(ax[axNum])
            
            # plot all edges
            e0.plotEdge(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'02EdgesA')
        
    
    #-------------------------------------------------------------------------
    #    Negative edge
    #-------------------------------------------------------------------------    
        
        # plot all nodes
        if doPlots1:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting negative edge in figure {}'.format(axNum+1))
            for n in [n0,n1]:
                n.plotNode(ax[axNum])
            e0.myReverse.plotEdge(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'02EdgesB')
                
                
    #-------------------------------------------------------------------------
    #    Edge with geometric node
    #-------------------------------------------------------------------------
        if doPrints:
            cc.printBlue('Creating edge with geometric node')
        
        n4 = Node(0.5*a,0.5*a,0)
        e0.geometricNodes = [n4,]    
         # plot all nodes
         
         
        if doPlots1: 
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting edge with geometric node in figure {}'.format(axNum+1))
            for n in [n0,n1, n4]:
                n.plotNode(ax[axNum])
            # plot all edges
            e0.plotEdge(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'02EdgesC')
                
        e0.geometricNodes = []  
        
        
        
    #==============================================================================
    #    FACES
    #==============================================================================
        
    #-------------------------------------------------------------------------
    #    Positive face
    #-------------------------------------------------------------------------   
        
        if doPrints:
            cc.printBlue('Creating faces')
        # Create faces by defining the border edges
        f0 = Face([e0,e4,-e2])
        f1 = Face([e3,e5,-e4])
        f2 = Face([e0,e3,-e1])
        f3 = Face([e1,e5,-e2])
        
        # Put faces in a list, we've seen that before ;)
        faces = [f0,f1,f2,f3]
        # plot all nodes
        if doPlots1:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting positive face in figure {}'.format(axNum+1))
            for n in [n0,n1,n2]:
                n.plotNode(ax[axNum])
            
            # plot all edges
            for e in f2.edges:
                e.plotEdge(ax[axNum])
                
            # Plot the faces
            f2.plotFace(ax[axNum])
            pf.setAxesEqual(ax[axNum])
            
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'03FaceA')
        
        
     
        
    #-------------------------------------------------------------------------
    #    Negative face
    #-------------------------------------------------------------------------
        if doPlots1:       
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting negative face in figure {}'.format(axNum+1))
            for n in [n0,n1,n2]:
                n.plotNode(ax[axNum])
            
            # plot all edges
            for e in f2.myReverse.edges:
                e.plotEdge(ax[axNum])
            
            if doExports:    
                pf.exportPNG(figs[axNum],exportPath+'03FaceB')
                
    #-------------------------------------------------------------------------
    #    Face with geometric edge
    #-------------------------------------------------------------------------   
        if doPrints:
            cc.printBlue('Creating face with geometric edge')
        n5 = Node(0.5*a,0.0*a,0.4*a)
        e0.geometricNodes = n5
        e6 = Edge(n5,n2)
        f2.edges =  [[e0,e3,-e6],[e6,-e1,e0]]
        
        
        if doPlots1:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting face with geometric edge in figure {}'.format(axNum+1))
            f2.plotFace(ax[axNum])
            for n in [n0,n1,n2,n5]:
                n.plotNode(ax[axNum])
            
            # plot all edges
            for e in [*f2.edges,*f2.geometricEdges]:
                e.plotEdge(ax[axNum])
                
            # Plot the faces
            
            ax[axNum].view_init(40,-40)
            pf.setAxesEqual(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'03FaceC')
            
        
        e0.geometricNodes = []
        f2.edges = [e0,e3,-e1]
        
        
    #==============================================================================
    #    VOLUME
    #============================================================================== 
        #Create a volume by defining the border faces
        if doPrints:
            cc.printBlue('Creating volume')
        v0 = Volume([f0,f1,-f2,-f3])
    #   
        if doPlots1:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting faces for volume in figure {}'.format(axNum+1))
            for n in nodes:
                n.plotNode(ax[axNum],showLabel=False)
            for f in faces:
                f.plotFace(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'04VolumeA')
        
        
        # plot the volume
        if doPlots1:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting volume in figure {}'.format(axNum+1))
            for n in nodes:
                n.plotNode(ax[axNum],showLabel=False)
            v0.plotVolume(ax[axNum],showNormalVec=True)
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'04VolumeB')
    
    
    
#==============================================================================
#    DUAL NODES
#==============================================================================    

#-------------------------------------------------------------------------
#    3D dual node
#-------------------------------------------------------------------------
    if doPlots2:
        if doPrints:
            cc.printBlue('Creating dual node 3D')
        v0.category1 = 'inner'
        dn0 = DualNode3D(v0)
        
        
        
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting dummy complex for limits in figure {}'.format(axNum+1))
            for n in nodes:
                n.plotNode(ax[axNum])
            
            axNum += 1
            v0.plotVolume(ax[axNum],showLabel=False,showBarycenter=False)
            dn0.plotNode(ax[axNum])
            pf.copylimits(ax[axNum-1],ax[axNum])
            if doPrints:
                cc.printGreen('Plotting 3D dual node in figure {}'.format(axNum+1))
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'05DualNodeA')
            
        
    
    #-------------------------------------------------------------------------
    #    2D dual node
    #-------------------------------------------------------------------------  
        if doPrints:
            cc.printBlue('Creating dual node 2D')
        dn1 = DualNode2D(f2)
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting 2D dual node in figure {}'.format(axNum+1))
            f2.plotFace(ax[axNum],showNormalVec=False,showBarycenter=False,showLabel=False)
            pf.copylimits(ax[axNum-1],ax[axNum])
            dn1.plotNode(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'05DualNodeB')
                
                
    #-------------------------------------------------------------------------
    #    1D dual node
    #-------------------------------------------------------------------------
        if doPrints:
            cc.printBlue('Creating dual node 1D')
        dn2 = DualNode1D(e0)
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting 1D dual node in figure {}'.format(axNum+1))
            e0.plotEdge(ax[axNum],showLabel=False,showArrow=False)
            dn2.plotNode(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'05DualNodeC')
            
            
            
    #==============================================================================
    #    DUAL EDGES
    #============================================================================== 
                
    #-------------------------------------------------------------------------
    #    3D dual edge
    #-------------------------------------------------------------------------            
                
        if doPrints:
            cc.printBlue('Creating dual edge 3D')      
        n6 = Node(0.5*a,0.5*a,a)
        
        nodes.append(n6)
        
        e7 = Edge(n1,n6)
        e8 = Edge(n2,n6)
        e9 = Edge(n3,n6)
        
        for e in [e7,e8,e9]:
            edges.append(e)
            
        f4 = Face([e4,e9,-e7])
        f5 = Face([e3,e8,-e7])
        f6 = Face([e5,e9,-e8])
        
        for f in [f4,f5,f6]:
            faces.append(f)
        
        v1 = Volume([-f1,-f4,f5,f6])
        
        volumes = [v0,v1]
        
        v1.category1 = 'inner'
        dn3 = DualNode3D(v1)
        f1.category1 = 'inner'
        de0 = DualEdge3D(f1)
        
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting 3D dual edge in figure {}'.format(axNum+1))
            for v in volumes:
                v.plotVolume(ax[axNum],showLabel = False, showBarycenter=False)
            pf.copylimits(ax[axNum-2],ax[axNum])
            de0.plotEdge(ax[axNum])
            de0.startNode.plotNode(ax[axNum])
            de0.endNode.plotNode(ax[axNum])
            ax[axNum].view_init(15,-100)
            ax[axNum].set_xlim3d(0.5,2.5)
            ax[axNum].set_ylim3d(0.75,2.75)
            ax[axNum].set_zlim3d(0.5,2.5)
            pf.setLabels(ax[axNum])
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'06DualEdgeA')
            
        
    #-------------------------------------------------------------------------
    #    2D dual edge
    #-------------------------------------------------------------------------     
        if doPrints:
            cc.printBlue('Creating dual edge 2D')     
        n7 = Node(a,a,0,num=7)
        nodes.append(n7)
        
        
        e10 = Edge(n1,n7)
        e11 = Edge(n7,n2)
        e12 = Edge(n1,n2)
        edges.append(e10)
        edges.append(e11)
        
        f7 = Face([e10,e11,-e12])
        f8 = Face([e0,e12,-e1])
        
        faces.append(f7)
    #    faces.append(f8)
        
        dn4 = DualNode2D(f7)
        dn5 = DualNode2D(f8)
        e12.category1 = 'inner'
        de1 = DualEdge2D(e12)
        
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting 2D dual edge in figure {}'.format(axNum+1))
            for n in [dn4,dn5]:
                n.plotNode(ax[axNum],showLabel=False)
        #    for e in [e0,e1,e10,e11,e12]:
        #        e.plotEdge(ax[axNum],showLabel=False,showArrow=False)
            pf.copylimits(ax[axNum-1],ax[axNum])
            ax[axNum].view_init(80,-70)
                
            for f in [f7,f8]:
                f.plotFace(ax[axNum],showLabel=False,showNormalVec=False,showBarycenter=False)
            
            de1.plotEdge(ax[axNum])
                
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'06DualEdgeB')   
                
        
        
    #-------------------------------------------------------------------------
    #    1D dual edge
    #-------------------------------------------------------------------------     
        if doPrints:
            cc.printBlue('Creating dual edge 1D')             
        n0.category1 = 'border'
        e0.category1 = 'border'
        e1.category1 = 'border'
    #    DualNode1D(e0)
        DualNode1D(e1)
        de2 = DualEdge1D(n0)
        
        
    #    v0.plotVolume(ax[axNum],showLabel=False,showBarycenter=False)
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting 3D dual edge in figure {}'.format(axNum+1))
            f2.plotFace(ax[axNum],showLabel=False,showBarycenter=False,showNormalVec=False)
            pf.copylimits(ax[axNum-1],ax[axNum])
            de2.plotEdge(ax[axNum])
            n0.plotNode(ax[axNum],showLabel=False)
            
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'06DualEdgeC')  
            
       
    #==============================================================================
    #    DUAL FACES
    #==============================================================================      
            
    #-------------------------------------------------------------------------
    #    3D dual face
    #-------------------------------------------------------------------------  
        if doPrints:
            cc.printBlue('Creating dual face 3D') 
        n8 = Node(a,a,a,num=8)
        n10 = Node(a/2,a/2,-a,num=10)
        
        for n in [n8,n10]:
            nodes.append(n)
        
            
            
        e13 = Edge(n6,n8)
        e14 = Edge(n1,n8)
        e15 = Edge(n2,n8)
        e16 = Edge(n7,n8)
        e17 = Edge(n1,n10)
        e18 = Edge(n10,n7)
        e19 = Edge(n2,n10)
    #    e20 = Edge(n10,n9)
        e20 = Edge(n10,n0)
    #    e23 = Edge(n10,n1)
    #    e24 = Edge(n10,n2)
        
        for e in [e13,e14,e15,e16,e17,e18,e19,e20]:
            edges.append(e)   
            
        f7.edges = [e10,e11,-e3]   
        f9 = Face([e3,e15,-e14])
        f10 = Face([e7,e13,-e14])
        f11 = Face([e8,e13,-e15])
        f12 = Face([e10,e16,-e14])
        f13 = Face([e17,e18,-e10])
        f14 = Face([e18,e11,e19])
        f15 = Face([e3,e19,-e17])
        f16 = Face([e17,e20,e0])
        f17 = Face([e20,e1,e19])
        f18 = Face([e11,e15,-e16])
        
        for f in [f9,f10,f11,f12,f13,f14,f15,f16,f17,f18]:
            faces.append(f)
            
            
            
            
        v2 = Volume([-f5,f11,-f10,f9])
        v3 = Volume([-f9,-f7,f12,f18])
        v4 = Volume([f13,-f14,f7,f15])
        v5 = Volume([-f15,f17,-f16,f2])
    #    for f in [-f15,f17,-f16,f2]:
    #        f.plotFace(ax[axNum+1])
        
        for v in [v2,v3,v4,v5]:
            volumes.append(v)
            
        
            
            
            
    
    
        
        
        dualNodes = []
        for v in volumes:
            if v.category1 == 'undefined':
                v.category1 = 'inner'
            if not v.dualCell3D:
                DualNode3D(v)
            dualNodes.append(v.dualCell3D)
            
            
        dualEdges = []
        for f in faces:
            if not f.dualCell2D:
                DualNode2D(f)
            
            if f.category1 == 'undefined':
                if len(f.volumes) == 1:
                    f.category1 = 'border'
                else:
                    f.category1 = 'inner'
            if not f.dualCell3D:
                DualEdge3D(f)
                
            if f.category1 == 'inner':
                dualEdges.append(f.dualCell3D)
             
        e3.category1 = 'inner'
        df0 = DualFace3D(e3)
            
        
    
    
        if doPlots2:    
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting dummy complex for limits in figure {}'.format(axNum+1))
            
            for n in nodes:
                n.plotNode(ax[axNum],showLabel=False)
            
            
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting 3D dual face in figure {}'.format(axNum+1))
            pf.copylimits(ax[axNum-1],ax[axNum])
            
            
            for v in volumes:
                v.plotVolume(ax[axNum],showLabel=False,showBarycenter=False,alpha=0.05)
            
            ax[axNum].view_init(14,-59)
            
            for dn in dualNodes:
                dn.plotNode(ax[axNum],showLabel=False)
            for de in dualEdges:
                de.plotEdge(ax[axNum],showLabel=False,showArrow=False)
        #    e3.plotEdge(ax[axNum])
            df0.simplifyFace()
            df0.plotFace(ax[axNum],alpha=0.5)
            
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'07DualFaceA')  
        
        
        
     
        
        
    #-------------------------------------------------------------------------
    #    2D dual face
    #-------------------------------------------------------------------------       
        
        if doPrints:
            cc.printBlue('Creating dual face 2D')     
        
    #    
        
    #    import grids.grid2DRectangular as grid2D
        c2D = Grid2DRectangular()
    #    c2D.plotComplex(ax[axNum])
        dc2D = DualComplex2D(c2D)
        
        
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting 2D dual face in figure {}'.format(axNum+1))
            for e in c2D.edges:
                e.plotEdge(ax[axNum],showLabel=False,showArrow=False)
            for n in c2D.innerNodes:
                n.plotNode(ax[axNum])
                
            dc2D.faces[0].plotFace(ax[axNum],showNormalVec=False,showBarycenter=False,showLabel=False) # ,color='#006400'
            ax[axNum].view_init(90,-90)
            
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'07DualFaceB')  
    #    
    #==============================================================================
    #    DUAL VOLUME
    #==============================================================================   

        
        if doPrints:
            cc.printBlue('Creating dual volume 3D')     
        
        c = Grid3DCubic(2)
        
        
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting dummy complex for limits in figure {}'.format(axNum+1))
            c.plotComplex(ax[axNum])
        
        
    #    c.plotComplex(ax[axNum])
        dc = DualComplex3D(c)
        for f in dc.innerFaces:
            f.simplifyFace()
            
            
        if doPlots2:
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting dual volume in figure {}'.format(axNum+1))
            pf.copylimits(ax[axNum-1],ax[axNum])
            for v in c.volumes:
                v.plotVolume(ax[axNum],alpha=0.05,showLabel=False,showBarycenter=False)
                
            dc.volumes[0].color = myRed
            c.innerNodes[0].plotNode(ax[axNum])
            dc.volumes[0].plotVolume(ax[axNum])
            
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'08DualVolumeA')  
    
    
    

#==============================================================================
#    Complex for discretization
#==============================================================================      
            
    if doPlots3:
        if doPrints:
            cc.printBlue('Creating complex for discretization')
    #    from grids.grid2Dtriangular import getComplexTriangular
        
        n100 = Node(1,1,0,num=0)
        n101 = Node(1,0,0,num=1)
        n102 = Node(2,2,0,num=2)
        n103 = Node(0,2,0,num=3)
        n104 = Node(-3,-0.7,0,num=4)
        n105 = Node(5,-0.7,0,num=5)
        n106 = Node(1,3,0,num=6)
    
        nodes = [n100,n101,n102,n103,n104,n105,n106]
        
        e100 = Edge(n100,n101,num=0)
        e101 = Edge(n100,n102,num=1)
        e102 = Edge(n103,n100,num=2)
        e103 = Edge(n104,n101,num=3)
        e104 = Edge(n101,n105,num=4)
        e105 = Edge(n105,n102,num=5)
        e106 = Edge(n102,n106,num=6)
        e107 = Edge(n106,n103,num=7)
        e108 = Edge(n103,n104,num=8)
        
        edges = [e100,e101,e102,e103,e104,e105,e106,e107,e108]
        
        
        f100 = Face([e103,-e100,-e102,e108],num=0)
        f101 = Face([e100,e104,e105,-e101],num=1)
        f102 = Face([e102,e101,e106,e107],num=2)
        
        faces = [f100,f101,f102]
        
        c2D = PrimalComplex2D(nodes,edges,faces)
        dc2D = DualComplex2D(c2D)
        
        df100 = n100.dualCell2D
        de100 = e100.dualCell2D
        de101 = e101.dualCell2D
        de102 = e102.dualCell2D
    
        
        
    #    c2DTri = getComplexTriangular()
    #    dc2DTri = c2DTri.calcDualComplex()
        
    #    f = c2DTri.findFace(60)[0]
    #    
    #    dn60 = f.dualCell2D
    #    de = dn60.edges
        
        
        
        
        if doPlots3:
            axNum +=1
            if doPrints:
                cc.printGreen('Plotting triangular complex in figure {}'.format(axNum+1))
            
            c2D.plotComplex(ax[axNum])
    ##        f.dualCell2D.plotNode(ax[axNum])
    #        
            axNum += 1
            if doPrints:
                cc.printGreen('Plotting triangular dual complex in figure {}'.format(axNum+1))
            dc2D.plotComplex(ax[axNum])
            
            
            
    
            
            axNum +=1
            if doPrints:
                cc.printGreen('Plotting dual face for energy balance in figure {}'.format(axNum+1))
            df100.plotFace(ax[axNum])
            ax[axNum].set_xlim3d(-1,3)
            ax[axNum].set_ylim3d(-0.5,2.5)
            
            
            de100.plotEdge(ax[axNum],dy=0.1)
            de101.plotEdge(ax[axNum],dx=0.1)
            de102.plotEdge(ax[axNum],dx=0.2)
            ax[axNum].view_init(90,-90)
            
            if doExports:
                pf.exportPNG(figs[axNum],'09DiskretA')
            
            
            axNum +=1
            if doPrints:
                cc.printGreen('Plotting primal edges for driving forces in figure {}'.format(axNum+1))
            df100.plotFace(ax[axNum],showLabel=False,showBarycenter=False,showNormalVec=False,color=tc.TUMBlack())
            de100.plotEdge(ax[axNum],showLabel=False,showArrow=False,color=tc.TUMBlack())
            de101.plotEdge(ax[axNum],showLabel=False,showArrow=False,color=tc.TUMBlack())
            de102.plotEdge(ax[axNum],showLabel=False,showArrow=False,color=tc.TUMBlack())
            
            
            n100.plotNode(ax[axNum],dx=0.2,dy=-0.2)
            n101.plotNode(ax[axNum],dx=0.2,dy=-0.2)
            n102.plotNode(ax[axNum],dx=0.2,dy=-0.2)
            n103.plotNode(ax[axNum],dx=0.2,dy=-0.2)
            pf.copylimits(ax[axNum-1],ax[axNum])
            e100.plotEdge(ax[axNum],dy=-0.2)
            e101.plotEdge(ax[axNum],dx=0.2)
            e102.plotEdge(ax[axNum],dx=-0.5)
            ax[axNum].view_init(90,-90)
    
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'09DiskretB')        
            
                
                
                
    #==============================================================================
    #    Complex for interpolation
    #==============================================================================
        if doPrints:
            cc.printBlue('Creating complex for interpolation')
        n200 = Node(0,0,0,num='k')
        n201 = Node(2,0,0,num='l')
        n202 = Node(1,1,0,num='m')
        
#        nodes200 = [n200,n201,n202]
        
        e200 = Edge(n200,n201,num='m')
        e201 = Edge(n201,n202,num='k')
        e202 = Edge(n202,n200,num='l')
        
#        edges200 = [e200,e201,e202]
        
        f200 = Face([e200,e201,e202],num='j')
        
        if doPlots3:
            axNum += 1
            ax[axNum].view_init(90,-90)
            ax[axNum].set_xlim3d(-0.25,2.25)
            ax[axNum].set_ylim3d(-0.25,1.25)
            n200.plotNode(ax[axNum],dx=-0.2,dy=-0.15)
            n201.plotNode(ax[axNum],dx=0.1,dy=-0.15)
            n202.plotNode(ax[axNum],dy=0.1)
            e200.plotEdge(ax[axNum],dy=-0.2)
            e201.plotEdge(ax[axNum],dx=0.1)
            e202.plotEdge(ax[axNum],dx=-0.3)
            f200.plotFace(ax[axNum],showNormalVec=False,showBarycenter=False)
            
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'09DiskretC')  
    #            for n in nodes200:
    #                n.plotNode(ax[axNum])
    #            for e in edges200:
    #                e.plotEdge(ax[axNum])
    #                
                
            
                
        
    #==============================================================================
    #    Complex for categories
    #==============================================================================    
        if doPrints:
            cc.printBlue('Creating complex for categories')
        from grids.grid2DTriangular import Grid2DTriangular
        c2DTri = Grid2DTriangular()
        dc2DTri = DualComplex2D(c2DTri)
        
        if doPlots3:
            axNum += 1
            for e in c2DTri.borderEdges:
                e.color = tc.TUMMustard()
            
            c2DTri.plotComplex(ax[axNum],showLabel=False,showBarycenter =False, showNormalVec=False)
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'09DiskretD')  
            
            axNum += 1
            ax[axNum].view_init(90,-90)
            for f in c2DTri.faces:
                f.plotFace(ax[axNum],color=tc.TUMBlack(),showLabel=False,showNormalVec=False,showBarycenter=False)
            for e in dc2DTri.innerEdges:
                e.plotEdge(ax[axNum],showLabel=False)
                
            for n in dc2DTri.innerNodes:
                n.plotNode(ax[axNum],showLabel=False)
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'09DiskretE')  
                
                
            axNum += 1
            ax[axNum].view_init(90,-90)
            for f in c2DTri.faces:
                f.plotFace(ax[axNum],color=tc.TUMBlack(),showLabel=False,showNormalVec=False,showBarycenter=False)
            for e in dc2DTri.innerEdges:
                e.plotEdge(ax[axNum],showLabel=False)
            for e in dc2DTri.borderEdges:
                e.plotEdge(ax[axNum],color=myRed,showLabel=False)
                
            for n in dc2DTri.innerNodes:
                n.plotNode(ax[axNum],showLabel=False)
                
                
            if doExports:
                pf.exportPNG(figs[axNum],exportPath+'09DiskretF')  
        
    if  closeWhenFinished:
        pf.closeFigures()
 
if __name__ == '__main__':
    with MyLogging ('pic4Hirschberg'):
        exportPath = ('graphicExport/Hirschberg2018/')
        doPlots(exportPath,doPlots1=True)       
        doPlots(exportPath,doPlots2=True)       
        doPlots(exportPath,doPlots3=True)         
    
        
   