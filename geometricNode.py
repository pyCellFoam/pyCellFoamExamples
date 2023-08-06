# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Tue May  9 17:06:52 2023

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
#    Change to Main Directory
#-------------------------------------------------------------------------
import os
if __name__ == '__main__':
    os.chdir('.')


#-------------------------------------------------------------------------
#    Standard Libraries
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#    Local Libraries
#-------------------------------------------------------------------------


#    kCells
#--------------------------------------------------------------------
from kCells import Node, Edge

#    Complex & Grids
#--------------------------------------------------------------------


#    Tools
#--------------------------------------------------------------------
import tools.colorConsole as cc
import tools.placeFigures as pf
from tools import MyLogging
from tools.tikZPicture import TikZPicture3D

#==============================================================================
#    CLASS DEFINITION
#==============================================================================

class Name:
    '''
    This is the explanation of this class.
    
    '''
    
#==============================================================================
#    SLOTS
#==============================================================================
    __slots__ = ('__a',
                 '__b')

#==============================================================================
#    INITIALIZATION
#==============================================================================
    def __init__(self,a=0,b=''):
        '''
        This is the explanation of the __init__ method. 
        
        All parameters should be listed:
        
        :param int a: Some Number
        :param str b: Some String
        
        '''
        self.__a = a
        self.__b = b
        
        
    
#==============================================================================
#    SETTER AND GETTER
#==============================================================================
    def __getA(self): return self.__a
    def __setA(self,a): self.__a = a
    a = property(__getA,__setA)

    
#==============================================================================
#    METHODS
#==============================================================================
    
#-------------------------------------------------------------------------
#    Method 1
#-------------------------------------------------------------------------
    def __method1(self,a=0,b=''):
        '''
        This is the explanation of the private method 1 
        
        All parameters should be listed, as well as the output values:
        
        :param int a: Some Number
        :param str b: Some String
        :return: Returns maybe something
        
        '''
        
        return -1
#-------------------------------------------------------------------------
#    Method 2
#-------------------------------------------------------------------------
    def method2(self,a,b):
        '''
        This is the explanation of the public method 2 
        
        All parameters should be listed, as well as the output values:
        
        :param int a: Some Number
        :param str b: Some String
        :return: Returns maybe something
        
        '''
        
        c = a*b
        return c

#-------------------------------------------------------------------------
#    Plot for Documentation
#-------------------------------------------------------------------------         
    @classmethod
    def plotDoc(cls):    
        cc.printRed('Not implemented')
    
#==============================================================================
#    TEST FUNCTIONS
#==============================================================================
if __name__ == '__main__':
    
    with MyLogging('geometricNode'):

#-------------------------------------------------------------------------
#    Create some examples
#-------------------------------------------------------------------------
        
        
        n0 = Node(0,0,0)
        n1 = Node(-2.5,1,0)
        n2 = Node(-1,1,0)
        
        nodesA = [n0,n1]        
        nodesB = [n0,n1,n2]
        
        e0 = Edge(n0,n1)
        e1 = Edge(n0,n1,geometricNodes=[n2,])
        
        edges = [e0,e1]
        
        
    


#-------------------------------------------------------------------------
#    Plotting
#-------------------------------------------------------------------------    
    
        # Choose plotting method. Possible choices: pyplot, VTK, TikZ, animation, doc, None
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
            for n in nodesB:
                n.plotNode(axes[0])
            for e in edges:
                e.plotEdge(axes[0])

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
            n1.tikZLabelPosition = 'above left'
            n2.tikZLabelPosition = 'above right'
            for n in nodesA:
                n.plotNodeTikZ(pic1)
            e0.tikZLabelPosition = 'above right'
            e0.plotEdgeTikZ(pic1)
            pic1.writeLaTeXFile('latex','geometricNode1Full',compileFile=True,openFile=True)
            pic1.writeTikZFile('latex','geometricNode1')
            
            pic2 = TikZPicture3D()
            for n in nodesB:
                n.plotNodeTikZ(pic2,draw=True)
            e1.tikZLabelPosition = 'above right'
            e1.plotEdgeTikZ(pic2)
            pic2.writeLaTeXFile('latex','geometricNode2Full',compileFile=True,openFile=True)
            pic2.writeTikZFile('latex','geometricNode2') 
            
            
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
        
    
