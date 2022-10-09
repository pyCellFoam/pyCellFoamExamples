# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Sun Oct  9 15:47:57 2022

'''
This is the explanation of the whole module and will be printed at the very 
beginning

Use - signs to declare a headline
--------------------------------------------------------------------------

* this is an item
* this is another one

#. numbered lists
#. are also possible


Maths
--------------------------------------------------------------------------

Math can be inline :math:`a^2 + b^2 = c^2` or displayed

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

Always remember that the last line has to be blank

'''
#==============================================================================
#    IMPORTS
#==============================================================================


#-------------------------------------------------------------------------
#    Standard Libraries
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#    Local Libraries
#-------------------------------------------------------------------------


#    kCells
#--------------------------------------------------------------------

from kCells import Node, Edge, Face, Volume
from complex import PrimalComplex3D, DualComplex3D

#    Complex & Grids
#--------------------------------------------------------------------


#    Tools
#--------------------------------------------------------------------
    

from tools import MyLogging
from tools import colorConsole as cc
from tools import placeFigures as pf
from tools.tikZPicture import TikZPicture3D
 



#==============================================================================
#    TEST FUNCTIONS
#==============================================================================
if __name__ == '__main__':
    
    with MyLogging('Paper'):

#-------------------------------------------------------------------------
#    Create Example
#-------------------------------------------------------------------------
        
        
        n0 = Node(0,0,0)
        n1 = Node(2,0,0)
        n2 = Node(0,2,0)
        n3 = Node(0,0,2)
        
        nodes = [n0,n1,n2,n3]
        
        
        e0 = Edge(n0,n1)
        e1 = Edge(n1,n2)
        e2 = Edge(n0,n2)
        e3 = Edge(n0,n3)
        e4 = Edge(n1,n3)
        e5 = Edge(n2,n3)
        
        edges = [e0,e1,e2,e3,e4,e5]
        
        
        f0 = Face([e0,e4,-e3])
        f1 = Face([e1,e5,-e4])
        f2 = Face([e2,e5,-e3])
        f3 = Face([e2,-e1,-e0])
                  
        faces = [f0,f1,f2,f3]
        
        v0 = Volume([f0,f1,-f2,f3])
        v0.category='inner'
        
        volumes = [v0,]
        
        pc = PrimalComplex3D(nodes,edges,faces,volumes)
        dc = DualComplex3D(pc)
            
        
        

#-------------------------------------------------------------------------
#    Plotting
#-------------------------------------------------------------------------    
    
        # Choose plotting method. Possible choices: pyplot, VTK, TikZ, animation, None
        plottingMethod = 'TikZ'   
        
        
#    Disabled
#--------------------------------------------------------------------- 
        if plottingMethod is None or plottingMethod == 'None':
            cc.printBlue('Plotting disabled')
        
#    Pyplot
#---------------------------------------------------------------------         
        elif plottingMethod == 'pyplot':
            cc.printBlue('Plot using pyplot')
            (figs,axes) = pf.getFigures()
            for f in faces:
                f.plotFace(axes[0])
                
            # dn0.plotNode(axes[0])

#    VTK
#--------------------------------------------------------------------- 
        elif plottingMethod == 'VTK' :
            cc.printBlue('Plot using VTK')
            cc.printRed('Not implemented')
            

#    TikZ
#--------------------------------------------------------------------- 
        elif plottingMethod == 'TikZ' :
            cc.printBlue('Plot using TikZ')            
            
            pic1 = TikZPicture3D()
            
            for n in nodes:
                n.plotNodeTikZ(pic1)
            pic1.addTikZCoSy3D(n0.getTikZNode(pic1))
                
            # pic1.writeLaTeXFile('latex','nodes_Full',compileFile=True,openFile=True)
            pic1.writeTikZFile('latex','0_nodes')
            
            pic2 = TikZPicture3D()
            
            for n in nodes:
                n.showLabel = False
                n.plotNodeTikZ(pic2)
            
            for e in edges:
                e.plotEdgeTikZ(pic2)
                
            # pic2.writeLaTeXFile('latex','edges_Full',compileFile=True,openFile=True)
            pic2.writeTikZFile('latex','1_edges')
            
            
            pic3 = TikZPicture3D()
            for n in nodes:
                n.plotNodeTikZ(pic3)
            for e in edges:
                e.showLabel=False
                e.showArrow=False
                e.plotEdgeTikZ(pic3)
            for f in faces:
                f.plotFaceTikZ(pic3)
                
            # pic3.writeLaTeXFile('latex','faces_Full',compileFile=True,openFile=True)
            pic3.writeTikZFile('latex','2_faces')
            
            
            pic4 = TikZPicture3D()
            v0.plotVolumeTikZ(pic4)
            # pic4.writeLaTeXFile('latex','volume_Full',compileFile=True,openFile=True)
            pic4.writeTikZFile('latex','3_volume')          
            
            
            pic5 = TikZPicture3D()
            v0.showLabel=False
            v0.showArrow = False
            v0.showNormalVec=False
            v0.showBarycenter=False
            v0.plotVolumeTikZ(pic5)
            for n in dc.innerNodes:
                n.plotNodeTikZ(pic5)
            # pic5.writeLaTeXFile('latex','dualNodes_Full',compileFile=True,openFile=True)
            pic5.writeTikZFile('latex','0_dualNode')  
            
            
            pic6 = TikZPicture3D()
            for f in faces:
                f.showLabel=False
                f.plotFaceTikZ(pic6,showArrow=False)
            for n in dc.innerNodes:
                n.showLabel=False
                n.plotNodeTikZ(pic6)
            dc.borderEdges[0].plotEdgeTikZ(pic6)
            # pic6.writeLaTeXFile('latex','dualEdges_Full',compileFile=True,openFile=True)
            pic6.writeTikZFile('latex','1_dualEdge')   
            
            
            pic7 = TikZPicture3D()
            for e in edges:
                e.plotEdgeTikZ(pic7)
                
            dc.borderFaces[0].plotFaceTikZ(pic7,showArrow=False)
                
            # pic7.writeLaTeXFile('latex','dualFaces_Full',compileFile=True,openFile=True)
            pic7.writeTikZFile('latex','2_dualFace')  

            pic8 = TikZPicture3D()
            for n in nodes:
                n.plotNodeTikZ(pic8)
            dc.volumes[0].plotVolumeTikZ(pic8,showArrow=False)      
            pic8.writeLaTeXFile('latex','dualVolumes_Full',compileFile=True,openFile=True)
            pic8.writeTikZFile('latex','3_dualVolume') 
            
            
            
            
            
            
            
#    Animation
#--------------------------------------------------------------------- 
        elif plottingMethod == 'animation':
            cc.printBlue('Creating animation')
            cc.printRed('Not implemented')
            

            
#    Unknown
#---------------------------------------------------------------------             
        else:
            cc.printRed('Unknown plotting method {}'.format(plottingMethod))        
        
    
