# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Wed Oct 30 14:57:33 2019

    

#==============================================================================
#    IMPORTS
#==============================================================================

import os

if __name__ == '__main__':
    os.chdir('../')


import tools.colorConsole as cc
from tools import MyLogging
from kCells import Node, Edge, Face, Volume
from complex import PrimalComplex3D, DualComplex3D
import tools.placeFigures as pf




#==============================================================================
#    SETTINGS
#==============================================================================

compileLaTeX = True
filename = 'categorization3D'




#==============================================================================
#    CREATE GEOMETRY
#==============================================================================

with MyLogging('ExampleCategorization3D'):
    exportPath = ('graphicExport/categorization3D/')
    
    if not os.path.isdir(exportPath):
        os.makedirs(exportPath)    
    
#-------------------------------------------------------------------------
#    Nodes
#-------------------------------------------------------------------------       
    n0  = Node(0,0,0,tikZLabelPosition = 'right')
    n1  = Node(1,0,0,tikZLabelPosition = 'below')
    n2  = Node(1.5,0,0,tikZLabelPosition = 'below right')
    n3  = Node(0,1,0)
    n4  = Node(1,1,0,tikZLabelPosition = 'below left')
    n5  = Node(0,1.5,0)
    n6  = Node(1.5,1.5,0)
    n7  = Node(0,0,1)
    n8  = Node(1,0,1,tikZLabelPosition = 'above right')
    n9  = Node(0,1,1)
    n10 = Node(1,1,1)
    n11 = Node(0,0,1.5)
    n12 = Node(1.5,0,1.5)
    n13 = Node(0,1.5,1.5)
    n14 = Node(1.5,1.5,1.5,tikZLabelPosition = 'left')
    
    nodes = [ n0, n1, n2, n3, n4, n5, n6, n7, n8, n9,
             n10,n11,n12,n13,n14]
    

#-------------------------------------------------------------------------
#    Edges
#-------------------------------------------------------------------------       
    e0  = Edge(n0,n1) 
    e1  = Edge(n1,n4) 
    e2  = Edge(n4,n3) 
    e3  = Edge(n3,n0) 
    e4  = Edge(n7,n8) 
    e5  = Edge(n8,n10) 
    e6  = Edge(n10,n9) 
    e7  = Edge(n9,n7) 
    e8  = Edge(n0,n7) 
    e9  = Edge(n1,n8) 
    e10 = Edge(n3,n9)
    e11 = Edge(n4,n10) 
    e12 = Edge(n1,n2) 
    e13 = Edge(n2,n6) 
    e14 = Edge(n6,n4)
    e15 = Edge(n3,n5)
    e16 = Edge(n5,n6)
    e17 = Edge(n8,n12)
    e18 = Edge(n10,n14)
    e19 = Edge(n9,n13)
    e20 = Edge(n7,n11)
    e21 = Edge(n2,n12)
    e22 = Edge(n12,n14)
    e23 = Edge(n14,n6)
    e24 = Edge(n5,n13)
    e25 = Edge(n13,n14)
    e26 = Edge(n13,n11)
    e27 = Edge(n11,n12)
    
    edges = [ e0, e1, e2, e3, e4, e5, e6, e7, e8, e9,
             e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,
             e20,e21,e22,e23,e24,e25,e26,e27]
    
#-------------------------------------------------------------------------
#    Faces
#-------------------------------------------------------------------------       
    f0 = Face([e0,e1,e2,e3])
    f1 = Face([e1,e11,-e5,-e9])
    f2 = Face([e2,e10,-e6,-e11])
    f3 = Face([e3,e8,-e7,-e10])
    f4 = Face([e0,e9,-e4,-e8])
    f5 = Face([e4,e5,e6,e7])
    f6 = Face([[e12,e13,e14,-e1],[e21,e22,e23,-e13],[e9,e17,-e21,-e12]])
    f7 = Face([e5,e18,-e22,-e17])
    f8 = Face([e11,e18,e23,e14])
    f9 = Face([[e2,e15,e16,e14],[e24,e25,e23,-e16],[e10,e19,-e24,-e15]])
    f10 = Face([e6,e19,e25,-e18])
    f11 = Face([[e4,e17,-e27,-e20],[e27,e22,-e25,e26],[e7,e20,-e26,-e19]])
    
    faces = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11]
    
#-------------------------------------------------------------------------
#    Volumes
#-------------------------------------------------------------------------   
    v0 = Volume([-f0,f1,f2,f3,f4,f5],category='inner')
    v1 = Volume([-f1,-f6,-f7,f8],category='border')
    v2 = Volume([-f8,f9,-f10,-f2],category='border')
    v3 = Volume([f11,-f5,f10,f7],category='border')
        
    volumes = [v0,v1,v2,v3]     
    
#-------------------------------------------------------------------------
#    Complex
#-------------------------------------------------------------------------           
    c = PrimalComplex3D(nodes,edges,faces,volumes,renumber=True)
    dc = DualComplex3D(c)
    
    
    
    
#==============================================================================
#    PLOT
#==============================================================================       
    cc.printBlue('Plotting')
    
    c.useCategory = 2
    (figs,axes) = pf.getFigures()
    c.plotComplex(axes[0])
    c.plotFaces(axes[1])
    c.plotVolumes(axes[2])
    
    dc.plotComplex(axes[3])
    dc.plotFaces(axes[4])
    dc.plotVolumes(axes[5])
    
    c.useCategory = 1
    
    
#==============================================================================
#    EXPORT TIKZ 
#==============================================================================    
    cc.printBlue('TikZ export')
    
    c.tikzScale = 2
    c.writeTikZ('primalCube',color=True,showLabel=False)
    
    
    c.tikzScale = 0.8
    dc.tikzScale = 0.8
    
    
    
#-------------------------------------------------------------------------
#    Categorize 1
#-------------------------------------------------------------------------       
    
    for cell in c.nodes+c.edges+c.faces+c.volumes+c.geometricNodes+c.geometricEdges:
        cell.grayInTikz = True
    c.writeTikZ(exportPath+'3DTotalPrimal',color=True)
    
#    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges:
        cell.grayInTikz = True
    dc.writeTikZ(exportPath+'3DTotalDual',color=True)
    
    
    
    # Inner nodes
    for cell in c.nodes+c.edges+c.faces+c.volumes+c.geometricNodes+c.geometricEdges:
        cell.grayInTikz = True
    for n in c.innerNodes:
        n.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim0NodesInner',color=True)
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for v in dc.innerVolumes:
        v.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual3VolumesInner',color=True,plotVolumes=True)
    
    
    # Border nodes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for n in c.borderNodes:
        n.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim0NodesBorder',color=True)
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for v in dc.borderVolumes:
        v.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual3VolumesBorder',color=True,plotVolumes=True)
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for f in dc.additionalBorderFaces:
        f.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual2FacesAddBorder',color=True,plotVolumes=True)
    
    
    
    # Additional border nodes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for n in c.additionalBorderNodes:
        n.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim0NodesAddBorder',color=True)   
    
    
    
    # Inner edges    
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for e in c.innerEdges:
        e.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim1EdgesInner',color=True) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for f in dc.innerFaces:
        f.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual2FacesInner',color=True,plotVolumes=True)
    
    
    # Border edges
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for e in c.borderEdges:
        e.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim1EdgesBorder',color=True) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for f in dc.borderFaces:
        f.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual2FacesBorder',color=True,plotVolumes=True)
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for e in dc.additionalBorderEdges:
        e.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual1EdgesAddBorder',color=True,plotVolumes=True)
    
    # Additional border Edges
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for e in c.additionalBorderEdges:
        e.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim1EdgesAddBorder',color=True) 
    
    
    
    # Inner faces
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for f in c.innerFaces:
        f.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim2FacesInner',color=True) 
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for e in dc.innerEdges:
        e.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual1EdgesInner',color=True,plotVolumes=True)
    
    
    # Border faces
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for f in c.borderFaces:
        f.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim2FacesBorder',color=True) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for e in dc.borderEdges:
        e.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual1EdgesBorder',color=True,plotVolumes=True)
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for n in dc.additionalBorderNodes:
        n.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual0NodesAddBorder',color=True,plotVolumes=True)
    
    
    
    
    # Additional border faces
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for f in c.innerFaces:
        f.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim2FacesAddBorder',color=True) 
    
    
    # Inner volumes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for v in c.innerVolumes:
        v.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim3VolumesInner',plotVolumes=True,color=True) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for n in dc.innerNodes:
        n.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual0NodesInner',color=True,plotVolumes=True)
    
    
    # Border volumes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for v in c.borderVolumes:
        v.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat1Prim3VolumesBorder',plotVolumes=True,color=True) 
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for n in dc.borderNodes:
        n.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat1Dual0NodesBorder',color=True,plotVolumes=True)
    
    
    
#-------------------------------------------------------------------------
#    Categorize 2
#-------------------------------------------------------------------------       
    
    c.useCategory = 2
    
    
    
    # Inner nodes
    for cell in c.nodes+c.edges+c.faces+c.volumes+c.geometricNodes+c.geometricEdges:
        cell.grayInTikz = True
        
    for n in c.nodes:
        n.showInPlot = False
    for n in c.innerNodes:
        n.grayInTikz = False
        n.showInPlot = True
    c.writeTikZ(exportPath+'3DCat2Prim0NodesInner',color=True,showLabel=False)
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for v in dc.innerVolumes:
        v.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual3VolumesInner',color=True,plotVolumes=True,showLabel=False)
    
    
    # Border nodes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
        
    for n in c.nodes:
        n.showInPlot = False
    for n in c.borderNodes:
        n.grayInTikz = False
        n.showInPlot = True
    c.writeTikZ(exportPath+'3DCat2Prim0NodesBorder',color=True,showLabel=False)
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for v in dc.borderVolumes:
        v.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual3VolumesBorder',color=True,plotVolumes=True,showLabel=False)
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for f in dc.additionalBorderFaces:
        f.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual2FacesAddBorder',color=True,plotVolumes=True,showLabel=False)
    
    
    
    # Additional border nodes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
        
    for n in c.nodes:
        n.showInPlot = False
    for n in c.additionalBorderNodes:
        n.grayInTikz = False
        n.showInPlot = True
    c.writeTikZ(exportPath+'3DCat2Prim0NodesAddBorder',color=True,showLabel=False)   
    
    
    for n in c.nodes:
        n.showInPlot = True
    
    # Inner edges    
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for e in c.innerEdges:
        e.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim1EdgesInner',color=True,showLabel=False) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for f in dc.innerFaces:
        f.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual2FacesInner',color=True,plotVolumes=True,showLabel=False)
    
    
    # Border edges
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for e in c.borderEdges:
        e.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim1EdgesBorder',color=True,showLabel=False) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for f in dc.borderFaces:
        f.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual2FacesBorder',color=True,plotVolumes=True,showLabel=False)
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for e in dc.additionalBorderEdges:
        e.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual1EdgesAddBorder',color=True,plotVolumes=True,showLabel=False)
    
    # Additional border Edges
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for e in c.additionalBorderEdges:
        e.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim1EdgesAddBorder',color=True,showLabel=False) 
    
    
    
    # Inner faces
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for f in c.innerFaces:
        f.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim2FacesInner',color=True,showLabel=False) 
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for e in dc.innerEdges:
        e.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual1EdgesInner',color=True,plotVolumes=True,showLabel=False)
    
    
    # Border faces
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for f in c.borderFaces:
        f.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim2FacesBorder',color=True,showLabel=False) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for e in dc.borderEdges:
        e.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual1EdgesBorder',color=True,plotVolumes=True,showLabel=False)
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for n in dc.additionalBorderNodes:
        n.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual0NodesAddBorder',color=True,plotVolumes=True,showLabel=False)
    
    
    
    
    # Additional border faces
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for f in c.additionalBorderFaces:
        f.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim2FacesAddBorder',color=True,showLabel=False)
    
    
    # Inner volumes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for v in c.innerVolumes:
        v.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim3VolumesInner',plotVolumes=True,color=True,showLabel=False) 
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for n in dc.innerNodes:
        n.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual0NodesInner',color=True,plotVolumes=True,showLabel=False)
    
    
    # Border volumes
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for v in c.borderVolumes:
        v.grayInTikz = False
    c.writeTikZ(exportPath+'3DCat2Prim3VolumesBorder',plotVolumes=True,color=True,showLabel=False) 
    
    
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
    for n in dc.borderNodes:
        n.grayInTikz = False
    dc.writeTikZ(exportPath+'3DCat2Dual0NodesBorder',color=True,plotVolumes=True,showLabel=False)    
    
    
    c.tikzScale = 1.3
    dc.tikzScale = 1.3
    
    
    # Duality node
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
        
    for n in dc.nodes+c.nodes:
        n.showInPlot = False
    c.innerVolumes[0].grayInTikz = False
    dc.innerNodes[0].grayInTikz = False
    dc.innerNodes[0].showInPlot = True
    
    
    addText = dc.writeTikZ(plotEdges=False,color=True,showLabel=False)
    
    
    c.writeTikZ(exportPath+'3DCat2Duality0Node',plotVolumes=True,color=True,showLabel=False,additionalText=addText) 
 
    
    # Duality edge
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
        
    for n in dc.nodes+c.nodes:
        n.showInPlot = False
        
    for e in dc.edges+dc.geometricEdges:
        e.showInPlot = False
        
        
    c.innerFaces[1].grayInTikz = False
    dc.innerEdges[1].grayInTikz = False
    dc.innerEdges[1].showInPlot = True
    
    
    addText = dc.writeTikZ(color=True,showLabel=False)
    
    
    c.writeTikZ(exportPath+'3DCat2Duality1Edge',color=True,showLabel=False,additionalText=addText) 
    
    # Duality face
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
        

        
    for e in dc.edges+dc.geometricEdges:
        e.showInPlot = False
        
        
    c.innerEdges[11].grayInTikz = False
    dc.innerFaces[11].grayInTikz = False
    dc.innerFaces[11].showInPlot = True
    
    
    addText = dc.writeTikZ(color=True,showLabel=False,showArrow=False,plotFaces=True)
    
    
    c.writeTikZ(exportPath+'3DCat2Duality2Face',color=True,showLabel=False,additionalText=addText) 
    
    
    # Duality volume
    for cell in c.nodes+c.edges+c.faces+c.volumes:
        cell.grayInTikz = True
    for cell in dc.nodes+dc.edges+dc.faces+dc.volumes+dc.geometricNodes+dc.geometricEdges: 
        cell.grayInTikz = True
        

        
    for f in dc.faces:
        f.showInPlot = False
        
        
    c.innerNodes[0].grayInTikz = False
    c.innerNodes[0].showInPlot = True
    
    dc.innerVolumes[0].grayInTikz = False
#    dc.innerFaces[11].showInPlot = True
    
    
    addText = dc.writeTikZ(color=True,showLabel=False,showArrow=False,plotVolumes=True)
    
    
    c.writeTikZ(exportPath+'3DCat2Duality3Volume',color=True,showLabel=False,additionalText=addText) 
    
    
#     # Duality edge
#    for cell in c.nodes+c.edges+c.faces+c.volumes:
#        cell.grayInTikz = True
#    c.innerFaces[1].grayInTikz = False
#    
#    addText = ''
#    nodeNames = []
#    for n in [dc.innerEdges[1].startNode,dc.innerEdges[1].endNode]:
#        n.grayInTikz = True
#        (nodeName,nodeText) = n.plotNodeTikZ(showLabel=False,color=True)
#        addText += nodeText
#        nodeNames.append(nodeName)
#            
#    addText += dc.innerEdges[1].plotEdgeTikZ(showLabel=False,color=True,possibleNodeNames = nodeNames)
#    c.writeTikZ(exportPath+'3DCat2Duality1Edge',plotVolumes=False,color=True,showLabel=False,additionalText=addText) 
    
    
    
    
#    for cell in c.nodes+c.edges+c.faces+c.volumes+c.geometricNodes+c.geometricEdges: 
#        cell.grayInTikz = False
#    c.useCategory = 2
#    c.writeTikZ(exportPath+'primalCube',color=True,plotFaces=False)
    
    
#==============================================================================
#    WRITE LATEX FILE
#==============================================================================  
 
    

    os.chdir(exportPath)
    with open(filename+'.tex','w') as file:
        file.write('\\documentclass{TUMnote}\n')
        file.write('\\usepackage{subcaption}\n')
        file.write(c.latexPreamble)     
        file.write('\\begin{document}\n')


#-------------------------------------------------------------------------
#    Categorize 1
#-------------------------------------------------------------------------            
        
        # Inner nodes
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim0NodesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual3VolumesInner.tex}
	\end{subfigure}
    \caption{Inner nodes and their dual inner volumes}
\end{figure}                   
        ''')
        
        # Border nodes 3D  
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim0NodesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual3VolumesBorder.tex}
	\end{subfigure}
    \caption{Border nodes and their dual border volumes}
\end{figure}                   
        ''')
        
        
        
        # Additional border nodes
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim0NodesAddBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DTotalDual.tex}
	\end{subfigure}
    \caption{Additional border nodes that have no dual}
\end{figure}                   
        ''')
        
        
        # Inner edges
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim1EdgesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual2FacesInner.tex}
	\end{subfigure}
    \caption{Inner edges and their dual inner faces}
\end{figure}                   
        ''')
        
        # Border edges 3D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim1EdgesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual2FacesBorder.tex}
	\end{subfigure}
    \caption{Border edges and their dual border faces}
\end{figure}                   
        ''')
        
        
        # Border nodes 2D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim0NodesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual2FacesAddBorder.tex}
	\end{subfigure}
    \caption{Border nodes and their dual additonal border faces}
\end{figure}                   
        ''')              
        
        
        # Additional border edges
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim1EdgesAddBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DTotalDual.tex}
	\end{subfigure}
    \caption{Additional border edges that have no dual}
\end{figure}                   
        ''')
        
        
        # Inner faces
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim2FacesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual1EdgesInner.tex}
	\end{subfigure}
    \caption{Inner faces and their dual inner edges}
\end{figure}                   
        ''')
        
        
        # Border faces 3D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim2FacesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual1EdgesBorder.tex}
	\end{subfigure}
    \caption{Border faces and their dual border edges}
\end{figure}                   
        ''')
        
        # Border edges 2D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim1EdgesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual1EdgesAddBorder.tex}
	\end{subfigure}
    \caption{Border edges and their dual additional border edges}
\end{figure}                   
        ''')        
        
        
        # Additional border faces
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim2FacesAddBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DTotalDual.tex}
	\end{subfigure}
    \caption{Additional border faces that have no dual}
\end{figure}                   
        ''')
        
        
        
        # Inner volumes
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim3VolumesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual0NodesInner.tex}
	\end{subfigure}
    \caption{Inner volumes and their dual inner nodes}
\end{figure}                   
        ''')
        
        
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim3VolumesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual0NodesBorder.tex}
	\end{subfigure}
    \caption{Border volumes}
\end{figure}                   
        ''')
        
        
        # Border faces 2D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Prim2FacesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat1Dual0NodesAddBorder.tex}
	\end{subfigure}
    \caption{Border faces and their dual additional border nodes}
\end{figure}                   
        ''')        
        
        
#-------------------------------------------------------------------------
#    Categorize 2
#-------------------------------------------------------------------------            
        
        # Inner nodes
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim0NodesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual3VolumesInner.tex}
	\end{subfigure}
    \caption{Inner nodes and their dual inner volumes}
\end{figure}                   
        ''')
        
        # Border nodes 3D  
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim0NodesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual3VolumesBorder.tex}
	\end{subfigure}
    \caption{Border nodes and their dual border volumes}
\end{figure}                   
        ''')
        
        
        
        # Additional border nodes
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim0NodesAddBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DTotalDual.tex}
	\end{subfigure}
    \caption{Additional border nodes that have no dual}
\end{figure}                   
        ''')
        
        
        # Inner edges
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim1EdgesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual2FacesInner.tex}
	\end{subfigure}
    \caption{Inner edges and their dual inner faces}
\end{figure}                   
        ''')
        
        # Border edges 3D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim1EdgesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual2FacesBorder.tex}
	\end{subfigure}
    \caption{Border edges and their dual border faces}
\end{figure}                   
        ''')
        
        
        # Border nodes 2D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim0NodesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual2FacesAddBorder.tex}
	\end{subfigure}
    \caption{Border nodes and their dual additonal border faces}
\end{figure}                   
        ''')              
        
        
        # Additional border edges
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim1EdgesAddBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DTotalDual.tex}
	\end{subfigure}
    \caption{Additional border edges that have no dual}
\end{figure}                   
        ''')
        
        
        # Inner faces
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim2FacesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual1EdgesInner.tex}
	\end{subfigure}
    \caption{Inner faces and their dual inner edges}
\end{figure}                   
        ''')
        
        
        # Border faces 3D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim2FacesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual1EdgesBorder.tex}
	\end{subfigure}
    \caption{Border faces and their dual border edges}
\end{figure}                   
        ''')
        
        # Border edges 2D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim1EdgesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual1EdgesAddBorder.tex}
	\end{subfigure}
    \caption{Border edges and their dual additional border edges}
\end{figure}                   
        ''')        
        
        
        # Additional border faces
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim2FacesAddBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DTotalDual.tex}
	\end{subfigure}
    \caption{Additional border faces that have no dual}
\end{figure}                   
        ''')
        
        
        
        # Inner volumes
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim3VolumesInner.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual0NodesInner.tex}
	\end{subfigure}
    \caption{Inner volumes and their dual inner nodes}
\end{figure}                   
        ''')
        
        
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim3VolumesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual0NodesBorder.tex}
	\end{subfigure}
    \caption{Border volumes}
\end{figure}                   
        ''')
        
        
        # Border faces 2D
        file.write(r'''
\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Prim2FacesBorder.tex}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{3DCat2Dual0NodesAddBorder.tex}
	\end{subfigure}
    \caption{Border faces and their dual additional border nodes}
\end{figure}                   
        ''')                
        
        
          
        
        
    dc.checkCategory2()
    
#==============================================================================
#    COMPILE
#==============================================================================    
    
    if compileLaTeX:
        os.system('pdflatex {}.tex -interaction batchmode'.format(filename))
        os.startfile('{}.pdf'.format(filename))    
            
        
    levelsOfExportPath = exportPath.count('/')
    os.chdir('../'*levelsOfExportPath)

