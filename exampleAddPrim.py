# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Thu Dec  7 14:16:21 2017

'''
Doc

'''
#==============================================================================
#    IMPORTS
#==============================================================================
import os
os.chdir('../')

from kCells import Node
from kCells import Edge
from kCells import Face
from kCells import Volume
from complex import PrimalComplex3D, DualComplex3D
import tools.placeFigures as pf
from tools import MyLogging

with MyLogging('addPrim'):
#==============================================================================
#    NODES
#==============================================================================
    
    
    a = 3
    b = 2.5
    c = 2


#-------------------------------------------------------------------------
#    Inner nodes
#------------------------------------------------------------------------- 
    ni1  = Node(  a,  b,  c, 1, category='inner')
    ni2  = Node(2*a,  b,  c, 2, category='inner')

    innerNodes = [ni1,ni2]
#    for n in innerNodes:
#        n.category = 'inner'


#-------------------------------------------------------------------------
#    Border nodes
#-------------------------------------------------------------------------   
    
    nb1  = Node(  0,  0,  0, 1, category='border')
    nb2  = Node(  a,  0,  0, 2, category='border')
    nb3  = Node(2*a,  0,  0, 3, category='border')
    nb4  = Node(  0,  b,  0, 4, category='border')
    nb5  = Node(  a,  b,  0, 5, category='border')
    nb6  = Node(2*a,  b,  0, 6, category='border')
    nb7  = Node(  0,2*b,  0, 7, category='border')
    nb8  = Node(  a,2*b,  0, 8, category='border')
    nb9  = Node(2*a,2*b,  0, 9, category='border')
    nb10 = Node(  0,  0,  c,10, category='border')
    nb11 = Node(  a,  0,  c,11, category='border')
    nb12 = Node(2*a,  0,  c,12, category='border')
    nb13 = Node(  0,  b,  c,13, category='border')
    nb14 = Node(  0,2*b,  c,14, category='border')
    nb15 = Node(  a,2*b,  c,15, category='border')
    nb16 = Node(2*a,2*b,  c,16, category='border')
    nb17 = Node(  0,  0,2*c,17, category='border')
    nb18 = Node(  a,  0,2*c,18, category='border')
    nb19 = Node(2*a,  0,2*c,19, category='border')
    nb20 = Node(  0,  b,2*c,20, category='border')
    nb21 = Node(  a,  b,2*c,21, category='border')
    nb22 = Node(2*a,  b,2*c,22, category='border')
    nb23 = Node(  0,2*b,2*c,23, category='border')
    nb24 = Node(  a,2*b,2*c,24, category='border')
    nb25 = Node(2*a,2*b,2*c,25, category='border')
    
    borderNodes = [ nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9,nb10,
                   nb11,nb12,nb13,nb14,nb15,nb16,nb17,nb18,nb19,nb20,
                   nb21,nb22,nb23,nb24,nb25]
#    for n in borderNodes:
#        n.category = 'border'

#-------------------------------------------------------------------------
#    Additional border nodes
#-------------------------------------------------------------------------   
    nB1 = Node(2.5*a,  0,  0,1)
    nB2 = Node(2.5*a,  b,  0,2)
    nB3 = Node(2.5*a,2*b,  0,3)
    nB4 = Node(2.5*a,  0,  c,1)
    nB5 = Node(2.5*a,  b,  c,2)
    nB6 = Node(2.5*a,2*b,  c,3)
    nB7 = Node(2.5*a,  0,2*c,1)
    nB8 = Node(2.5*a,  b,2*c,2)
    nB9 = Node(2.5*a,2*b,2*c,3)
    
    additionalBorderNodes = [nB1,nB2,nB3,nB4,nB5,nB6,nB7,nB8,nB9]
    
    for n in additionalBorderNodes:
        n.category = 'additionalBorder'
        
    nodes = [*innerNodes,*borderNodes,*additionalBorderNodes]

#==============================================================================
#    EDGES
#==============================================================================


#-------------------------------------------------------------------------
#    Inner edges
#------------------------------------------------------------------------- 
    ei1  = Edge( nb5, ni1, 1)
    ei2  = Edge( nb6, ni2, 2)
    ei3  = Edge(nb13, ni1, 3)
    ei4  = Edge( ni1, ni2, 4)
    ei5  = Edge( ni2, nB5, 5)
    ei6  = Edge(nb11, ni1, 6)
    ei7  = Edge(nb12, ni2, 7)
    ei8  = Edge( ni1,nb15, 8)
    ei9  = Edge( ni2,nb16, 9)
    ei10 = Edge( ni1,nb21,10)
    ei11 = Edge( ni2,nb22,11)
    
    innerEdges = [ ei1, ei2, ei3, ei4, ei5, ei6, ei7, ei8, ei9,ei10,
                  ei11]
    
    for e in innerEdges:
        e.category = 'inner'

#-------------------------------------------------------------------------
#    Border edges
#-------------------------------------------------------------------------   
    
    eb1  = Edge( nb1, nb2, 1)
    eb2  = Edge( nb2, nb3, 2)
    eb3  = Edge( nb4, nb5, 3)
    eb4  = Edge( nb5, nb6, 4)
    eb5  = Edge( nb7, nb8, 5)
    eb6  = Edge( nb8, nb9, 6)
    eb7  = Edge( nb1, nb4, 7)
    eb8  = Edge( nb2, nb5, 8)
    eb9  = Edge( nb3, nb6, 9)
    eb10 = Edge( nb4, nb7,10)
    eb11 = Edge( nb5, nb8,11)
    eb12 = Edge( nb6, nb9,12)
    eb13 = Edge( nb1,nb10,13)
    eb14 = Edge( nb2,nb11,14)
    eb15 = Edge( nb3,nb12,15)
    eb16 = Edge( nb4,nb13,16)
    eb17 = Edge( nb7,nb14,17)
    eb18 = Edge( nb8,nb15,18)
    eb19 = Edge( nb9,nb16,19)
    eb20 = Edge(nb10,nb11,20)
    eb21 = Edge(nb11,nb12,21)
    eb22 = Edge(nb14,nb15,22)
    eb23 = Edge(nb15,nb16,23)
    eb24 = Edge(nb10,nb13,24)
    eb25 = Edge(nb13,nb14,25)
    eb26 = Edge(nb10,nb17,26)
    eb27 = Edge(nb11,nb18,27)
    eb28 = Edge(nb12,nb19,28)
    eb29 = Edge(nb13,nb20,29)
    eb30 = Edge(nb14,nb23,30)
    eb31 = Edge(nb15,nb24,31)
    eb32 = Edge(nb16,nb25,32)
    eb33 = Edge(nb17,nb18,33)
    eb34 = Edge(nb18,nb19,34)
    eb35 = Edge(nb20,nb21,35)
    eb36 = Edge(nb21,nb22,36)
    eb37 = Edge(nb23,nb24,37)
    eb38 = Edge(nb24,nb25,38)
    eb39 = Edge(nb17,nb20,39)
    eb40 = Edge(nb18,nb21,40)
    eb41 = Edge(nb19,nb22,41)
    eb42 = Edge(nb20,nb23,42)
    eb43 = Edge(nb21,nb24,43)
    eb44 = Edge(nb22,nb25,44)
    
    
    borderEdges = [ eb1, eb2, eb3, eb4, eb5, eb6, eb7, eb8, eb9,eb10,
                   eb11,eb12,eb13,eb14,eb15,eb16,eb17,eb18,eb19,eb20,
                   eb21,eb22,eb23,eb24,eb25,eb26,eb27,eb28,eb29,eb30,
                   eb31,eb32,eb33,eb34,eb35,eb36,eb37,eb38,eb39,eb40,
                   eb41,eb42,eb43,eb44]
    
    for e in borderEdges:
        e.category = 'border'

#-------------------------------------------------------------------------
#    Additional border edges
#-------------------------------------------------------------------------  
    
    eB1  = Edge( nb3, nB1, 1)
    eB2  = Edge( nb6, nB2, 2)
    eB3  = Edge( nb9, nB3, 3)
    eB4  = Edge( nB1, nB2, 4)
    eB5  = Edge( nB2, nB3, 5)
    eB6  = Edge( nB1, nB4, 6)
    eB7  = Edge( nB2, nB5, 7)
    eB8  = Edge( nB3, nB6, 8)
    eB9  = Edge(nb12, nB4, 9)
    eB10 = Edge(nb16, nB6,10)
    eB11 = Edge( nB4, nB5,11)
    eB12 = Edge( nB5, nB6,12)
    eB13 = Edge( nB4, nB7,13)
    eB14 = Edge( nB5, nB8,14)
    eB15 = Edge( nB6, nB9,15)
    eB16 = Edge(nb19, nB7,16)
    eB17 = Edge(nb22, nB8,17)
    eB18 = Edge(nb25, nB9,18)
    eB19 = Edge( nB7, nB8,19)
    eB20 = Edge( nB8, nB9,20)
    
    
    additionalBorderEdges= [ eB1, eB2, eB3, eB4, eB5, eB6, eB7, eB8, eB9,eB10,
                            eB11,eB12,eB13,eB14,eB15,eB16,eB17,eB18,eB19,eB20]
    
    for e in additionalBorderEdges:
        e.category = 'additionalBorder'
        
    edges = [*innerEdges,*borderEdges,*additionalBorderEdges]

#==============================================================================
#    FACES
#==============================================================================
    
#faceEdges = [eB17,eB20,-eB18,-eb44]

    
#-------------------------------------------------------------------------
#    Inner faces
#------------------------------------------------------------------------- 
    
    fi1  = Face([ eb3, ei1, -ei3,-eb16], 1)
    fi2  = Face([ eb4, ei2, -ei4, -ei1], 2)
    fi3  = Face([ eb8, ei1, -ei6,-eb14], 3)
    fi4  = Face([ eb9, ei2, -ei7,-eb15], 4)
    fi5  = Face([eb11,eb18, -ei8, -ei1], 5)
    fi6  = Face([eb12,eb19, -ei9, -ei2], 6)
    fi7  = Face([eb20, ei6,- ei3,-eb24], 7)
    fi8  = Face([eb21, ei7, -ei4,- ei6], 8)
    fi9  = Face([ ei3, ei8,-eb22,-eb25], 9)
    fi10 = Face([ ei4, ei9,-eb23, -ei8],10)
    fi11 = Face([ ei3,ei10,-eb35,-eb29],11)
    fi12 = Face([ ei4,ei11,-eb36,-ei10],12)
    fi13 = Face([ ei6,ei10,-eb40,-eb27],13)
    fi14 = Face([ ei7,ei11,-eb41,-eb28],14)
    fi15 = Face([ ei8,eb31,-eb43,-ei10],15)
    fi16 = Face([ ei9,eb32,-eb44,-ei11],16)
    fi17 = Face([ eB2, eB7, -ei5, -ei2],17)
    fi18 = Face([ eB9,eB11, -ei5, -ei7],18)
    fi19 = Face([ ei5,eB12,-eB10, -ei9],19)
    fi20 = Face([ ei5,eB14,-eB17,-ei11],20)

       
    innerFaces = [ fi1, fi2, fi3, fi4, fi5, fi6, fi7, fi8, fi9,fi10,
                  fi11,fi12,fi13,fi14,fi15,fi16,fi17,fi18,fi19,fi20]
    for f in innerFaces:
        f.category = 'inner'
#-------------------------------------------------------------------------
#    Border faces
#------------------------------------------------------------------------- 
    
    fb1  = Face([ eb1, eb8, -eb3, -eb7], 1)
    fb2  = Face([ eb2, eb9, -eb4, -eb8], 2)
    fb3  = Face([ eb3,eb11, -eb5,-eb10], 3)
    fb4  = Face([ eb4,eb12, -eb6,-eb11], 4)
    fb5  = Face([ eb1,eb14,-eb20,-eb13], 5)
    fb6  = Face([ eb2,eb15,-eb21,-eb14], 6)
    fb7  = Face([ eb5,eb18,-eb22,-eb17], 7)
    fb8  = Face([ eb6,eb19,-eb23,-eb18], 8)
    fb9  = Face([ eb7,eb16,-eb24,-eb13], 9)
    fb10 = Face([eb10,eb17,-eb25,-eb16],10)
    fb11 = Face([eb20,eb27,-eb33,-eb26],11)
    fb12 = Face([eb21,eb28,-eb34,-eb27],12)
    fb13 = Face([eb22,eb31,-eb37,-eb30],13)
    fb14 = Face([eb23,eb32,-eb38,-eb31],14)
    fb15 = Face([eb24,eb29,-eb39,-eb26],15)
    fb16 = Face([eb25,eb30,-eb42,-eb29],16)
    fb17 = Face([eb33,eb40,-eb35,-eb39],17)
    fb18 = Face([eb34,eb41,-eb36,-eb40],18)
    fb19 = Face([eb35,eb43,-eb37,-eb42],19)
    fb20 = Face([eb36,eb44,-eb38,-eb43],20)
    
    borderFaces = [ fb1, fb2, fb3, fb4, fb5, fb6, fb7, fb8, fb9,fb10,
                   fb11,fb12,fb13,fb14,fb15,fb16,fb17,fb18,fb19,fb20]
    for f in borderFaces:
        f.category = 'border'

#-------------------------------------------------------------------------
#    Additional border faces
#-------------------------------------------------------------------------
    fB1  = Face([ eB1, eB4, -eB2, -eb9], 1)
    fB2  = Face([ eB2, eB5, -eB3,-eb12], 2)
    fB3  = Face([ eB1, eB6, -eB9,-eb15], 3)
    fB5  = Face([ eB3, eB8,-eB10,-eb19], 5)
    fB6  = Face([ eB4, eB7,-eB11, -eB6], 6)
    fB7  = Face([ eB5, eB8,-eB12, -eB7], 7)
    fB10 = Face([ eB9,eB13,-eB16,-eb28],10)
    fB12 = Face([eB10,eB15,-eB18,-eb32],12)
    fB13 = Face([eB11,eB14,-eB19,-eB13],13)
    fB14 = Face([eB12,eB15,-eB20,-eB14],14)
    fB15 = Face([eB16,eB19,-eB17,-eb41],15)
    fB16 = Face([eB17,eB20,-eB18,-eb44],16)
    
    additionalBorderFaces = [ fB1, fB2, fB3, fB5, fB6, fB7,fB10,
                             fB12,fB13,fB14,fB15,fB16]
    for f in additionalBorderFaces:
        f.category = 'additionalBorder'


    faces = [*innerFaces,*borderFaces,*additionalBorderFaces]

#==============================================================================
#    VOLUMES
#==============================================================================
#-------------------------------------------------------------------------
#    Inner volumes
#------------------------------------------------------------------------- 

    volumeFaces = [-fi16, -fi19, fi20,-fB12, fB14, fB16]
    
    
    vi1 = Volume([ -fi1,  fi3,  fi7, -fb1,  fb5, -fb9],1)
    vi2 = Volume([ -fi2, -fi3,  fi4,  fi8, -fb2,  fb6],2)
    vi3 = Volume([  fi1,  fi5,  fi9, -fb3, -fb7,-fb10],3)
    vi4 = Volume([  fi2, -fi5,  fi6, fi10, -fb4, -fb8],4)
    vi5 = Volume([ -fi7,-fi11, fi13, fb11,-fb15, fb17],5)
    vi6 = Volume([ -fi8,-fi12,-fi13, fi14, fb12, fb18],6)
    vi7 = Volume([ -fi9, fi11, fi15,-fb13,-fb16, fb19],7)
    vi8 = Volume([-fi10, fi12,-fi15, fi16,-fb14, fb20],8)
    
    innerVolumes = [vi1,vi2,vi3,vi4,vi5,vi6,vi7,vi8]
    
    for v in innerVolumes:
        v.category = 'inner'
    
#-------------------------------------------------------------------------
#    Border volumes
#-------------------------------------------------------------------------   
    vb1 = Volume([ -fi4, -fB1,  fB3, -fi17,  fB6,  fi18],1)
    vb2 = Volume([ -fi6, -fB2,  fi17, -fB5,  fB7,  fi19],2)
    vb3 = Volume([-fi14, -fi18, fB10,-fi20, fB13, fB15],3)
    vb4 = Volume([-fi16, -fi19, fi20,-fB12, fB14, fB16],4)
    borderVolumes = [vb1,vb2,vb3,vb4]
    
    for v in borderVolumes:
        v.category = 'border'
        
        
    volumes = [*innerVolumes,*borderVolumes]
        
        
#==============================================================================
#    COMPLEX
#==============================================================================
    c = PrimalComplex3D(nodes,edges,faces,volumes)
    if True:
        dc = DualComplex3D(c)
    
#==============================================================================
#    PLOT
#==============================================================================
    (fig,ax) = pf.getFigures(numTotal=10)
    
#-------------------------------------------------------------------------
#    Figure 1: primal nodes
#-------------------------------------------------------------------------      
    if True:
        for n in [*innerNodes,*borderNodes,*additionalBorderNodes]:
            n.plotNode(ax[0])
        pf.setLabels(ax[0])
        pf.setAxesEqual(ax[0])
        ax[0].set_title('Primal nodes')


#-------------------------------------------------------------------------
#    Figure 2: primal edges
#-------------------------------------------------------------------------    
    if True:
        for e in [*innerEdges,*borderEdges,*additionalBorderEdges]:
            e.plotEdge(ax[1])
        pf.setLabels(ax[0])
        pf.setAxesEqual(ax[1])
        ax[1].set_title('Primal edges')

#-------------------------------------------------------------------------
#    Figure 3: primal faces
#-------------------------------------------------------------------------       
    if True:
        for f in [*innerFaces,*borderFaces,*additionalBorderFaces]:
            f.showNormalVec = False
            f.plotFace(ax[2])
        pf.copylimits(ax[0],ax[2])
        pf.setLabels(ax[2])
        c.setupAxis(ax[2])
    

#-------------------------------------------------------------------------
#    Figure 4: primal volumes
#-------------------------------------------------------------------------            
    if True:            
        for v in [*innerVolumes,*borderVolumes]:
            v.plotVolume(ax[3])            
        pf.copylimits(ax[0],ax[3])   
        pf.setLabels(ax[3])
        ax[3].set_title('Primal volumes')
        

#-------------------------------------------------------------------------
#    Figure 5: dual nodes
#-------------------------------------------------------------------------         
    if True:
        for n in dc.nodes:
            n.plotNode(ax[4])
    
    
    
#-------------------------------------------------------------------------
#    Figure 6: Oblique plot
#-------------------------------------------------------------------------      

    if False:         
#        fig[3].clf()
        ax[5] = pf.returnTo2D(fig[5])
            
        for e in [*innerEdges,*borderEdges,*additionalBorderEdges]:
            
            e.plotEdgeOblique(ax[5])
           
        
        import matplotlib.pyplot as plt    
        plt.figure(fig[5].number)
        plt.savefig('oblique.png',dpi=300)
        
#-------------------------------------------------------------------------
#    Figure 7: incidence matrix
#-------------------------------------------------------------------------          
    d_1_ii = c.incidenceMatrix1ii
    d_1_ib = c.incidenceMatrix1ib
    d_1_iB = c.incidenceMatrix1iB
    d_1_bi = c.incidenceMatrix1bi
    d_1_bb = c.incidenceMatrix1bb
    d_1_bB = c.incidenceMatrix1bB
    print(d_1_bB.shape)
    
    
    c.plotIncidence1(fig[6])

##-------------------------------------------------------------------------
##    Figure 8: combine border faces
##-------------------------------------------------------------------------  
#
##    c.combineAdditionalBorderFaces()
#        
#    if True:
#        for f in [*innerFaces,*borderFaces,*additionalBorderFaces]:
#            f.showNormalVec = False
#            f.plotFace(ax[7])
##        pf.copylimits(ax[0],ax[])
##        pf.setLabels(ax[2])
#        c.setupAxis(ax[7])
#        ax[7].set_title('Primal faces')   
#        
        
#-------------------------------------------------------------------------
#    Figure 8: combine border faces
#-------------------------------------------------------------------------  
        
        
        
        
        
        
        
        
        
        