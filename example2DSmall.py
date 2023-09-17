# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Sun Oct  6 16:14:30 2019

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

import os
os.chdir('../')

#==============================================================================
#    IMPORTS
#==============================================================================
from kCells import Node, Edge, Face
from tools.tikZPicture import TikZPicture

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
    
    
#==============================================================================
#    TEST FUNCTIONS
#==============================================================================
if __name__ == '__main__':
    from tools import MyLogging
    import tools.placeFigures as pf
    with MyLogging('smallExample2D'):
        n0 = Node(0,0,0,category='border')
        n1 = Node(1,0,0,category='border')
        n2 = Node(1.5,0,0)
        n3 = Node(0,1,0,category='border')
        n4 = Node(1,1,0,category='inner')
    #        n5 = Node(1.5,1,0)
        n5 = Node(0,1.5,0)
    #        n7 = Node(1,1.5,0)
        n6 = Node(1.5,1.5,0)
        
        
        nodes = [n0,n1,n2,n3,n4,n5,n6]
        
        
        e0 = Edge(n0,n1) 
        e1 = Edge(n1,n4) 
        e2 = Edge(n4,n3) 
        e3 = Edge(n3,n0) 
        e4 = Edge(n1,n6,geometricNodes=[n2,])
        e5 = Edge(n3,n6,geometricNodes=[n5,])
        e6 = Edge(n4,n6)
#        e5 = Edge()
        
        
        edges = [e0,e1,e2,e3,e4,e5,e6]
    
    
        (figs,axes) = pf.getFigures(2,2)
        for n in nodes:
            n.plotNode(axes[0])
        for e in edges:
            e.plotEdge(axes[0])
            

