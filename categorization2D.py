# -*- coding: utf-8 -*-
#==============================================================================
# TITLE
#==============================================================================
# Author:         Tobias Scheuermann
# Institution:    Chair of Automatic Control
#                 Department of Mechanical Engineering
#                 Technical University of Munich (TUM)
# E-Mail:         tobias.scheuermann@tum.de
# Created on:     Wed Oct 30 16:21:47 2019

'''


'''
#==============================================================================
#    IMPORTS
#==============================================================================
import os
if __name__ == '__main__':
    os.chdir('../')


from tools import MyLogging
from kCells import Node, Edge, Face
#from complex import PrimalComplex3D
import tools.placeFigures as pf
#from complex.primalComplex2D import PrimalComplex2D
from complex.complex2D import Complex2D



with MyLogging('ExampleCategorization2D'):

    exportPath = ('graphicExport/categorization2D/')
    
    if not os.path.isdir(exportPath):
        os.mkdir(exportPath)  
    
    
    compileLaTeX = True
    filename = 'categorization2D'
    
    
    
    (figs,ax) = pf.getFigures()
    
    
    n100 = Node(0,0,0,num=0)
    n101 = Node(1,0,0,num=1)
    n102 = Node(1.5,0,0,num=2)
    n103 = Node(0,1,0,num=3)
    n104 = Node(1,1,0,num=4)
    n105 = Node(1.5,1,0,num=5)
    n106 = Node(0,-0.5,0,num=6)
    n107 = Node(1,-0.5,0,num=7)
    n108 = Node(1.5,-0.5,0,num=8)
    nodes100 = [n100,n101,n102,n103,n104,n105,n106,n107,n108]
    
    e100 = Edge(n100,n101)
    e101 = Edge(n102,n104,geometricNodes=n105)
    e102 = Edge(n103,n104)
    e103 = Edge(n101,n102)
    e104 = Edge(n107,n102,geometricNodes=n108)
    e105 = Edge(n100,n107,geometricNodes=n106)
    e106 = Edge(n100,n103)
    e107 = Edge(n101,n107)
    e108 = Edge(n101,n104)
    edges100 = [e100,e101,e102,e103,e104,e105,e106,e107,e108]

    fi100 = Face([e100,e108,-e102,-e106],num=0)
    fi100.category1 = 'inner'    
    fb100 = Face([e105,-e107,-e100],num=0)
    fb100.category1 = 'border'
    fb101 = Face([e104,-e103,e107],num=1)
    fb101.category1 = 'border'
    fb102 = Face([e103,e101,-e108],num=2)
    fb102.category1 = 'border'
    
    faces100 = [fi100,fb100,fb101,fb102]
    
    c1 = Complex2D(nodes100,edges100,faces100)    
    c1.plotComplex(ax[0])
    
    c1.tikzScale = 3
    c1.writeTikZ(exportPath+'pic1')
    
    
    
    n200 = Node(0,0,0,num=0)
    n201 = Node(1,0,0,num=1)
    n202 = Node(1.5,1,0,num=2)
    n203 = Node(0,1,0,num=3)
    n204 = Node(1,1,0,num=4)
    n205 = Node(0,-0.5,0,num=5)
    n206 = Node(1.5,-0.5,0,num=6)
    nodes200 = [n200,n201,n202,n203,n204,n205,n206]
    
    
    
    e200 = Edge(n200,n201,num=0)
    e201 = Edge(n201,n204,num=1)
    e202 = Edge(n203,n204,num=2)
    e203 = Edge(n200,n203,num=3)
    e204 = Edge(n200,n206,num=4,geometricNodes=n205)
    e205 = Edge(n206,n204,num=5,geometricNodes=n202)
    e206 = Edge(n206,n201,num=6)
#    e205 = Edge(n203,n206,num=5)
#    
    
    edges200 = [e200,e201,e202,e203,e204,e205,e206]
#    edges200 = []
    
    fi200 = Face([e200,e201,-e202,-e203],num=0)
    fi200.category1 = 'inner'
    fb200 = Face([e204,e206,-e200],num=0)
    fb200.category1 = 'border'
    fb201 = Face([e205,-e201,-e206])
    fb201.category1 = 'border'
    faces200 = [fi200,fb200,fb201]
    
    c2 = Complex2D(nodes200,edges200,faces200)
    c2.plotComplex(ax[1])
    c2.tikzScale = 3
    c2.writeTikZ(exportPath+'pic2')
    
    os.chdir(exportPath)
    with open(filename+'.tex','w') as file:
        file.write('\\documentclass{TUMnote}\n')
        file.write('\\usepackage{subcaption}\n')
        file.write(c1.latexPreamble)     
        file.write('\\begin{document}\n')
        file.write(r'''The complexity of the example is reduced by removing 
the additional border face in the bottom right corner. 
In the 2D example, this may have only little effect: 
the number of faces is reduced from 4 to 3. 
But in the 3D case the equivalent procedure reduces the number of volumes from 8 to 4.

\begin{figure}[!ht]
	\begin{subfigure}[c]{0.4\textwidth}
		\input{pic1.tex}
        \caption{Example from Kotyczka2017Dis}
	\end{subfigure}
    \hfill
	\begin{subfigure}[c]{0.4\textwidth}
		\input{pic2.tex}
        \caption{Reduced example used in the following}
	\end{subfigure}
\end{figure}
''')
            
        
#        file.write('\\input{pic1.tex}\n')
        file.write('\\end{document}\n')
            
#        self.writeTikZ()
    
    
    if compileLaTeX:
        os.system('pdflatex {}.tex -interaction batchmode'.format(filename))
        os.startfile('{}.pdf'.format(filename))    
        
    levelsOfExportPath = exportPath.count('/')
    os.chdir('../'*levelsOfExportPath)
    
    