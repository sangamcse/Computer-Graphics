import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)

    x = -10.0

    sinc=0

    glPointSize(2)
    glBegin(GL_LINE_STRIP)
    while (x<10.0):
    	sinc = math.sin(x) / x
    	glVertex2f(x*0.09*0.1, sinc*0.09)
        x = x + 0.1
    glEnd()
    glFlush()

    
glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (1500, 1500)
glutCreateWindow ('Sinc Function')
glutDisplayFunc(display)
glutMainLoop()