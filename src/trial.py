from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random

x=115
y=121

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0, 0.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)
    

def mouseFun(button,state,xIn,yIn):
    global x
    global y
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        x=xIn
        y=480-yIn

    glutPostRedisplay()
    
def displayFun():
    global x
    global y
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)

    M=40
    L=3
    for i in range(0,500000):
        glVertex2f(x,y)
        tmp=x
        x=M*(1+2*L)-y+ abs(x-L*M)
        y=tmp
    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()    
    glutInitWindowSize(640,480)
    glutCreateWindow("Gingerbread")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    glutMouseFunc(mouseFun)
    initFun()
    glutMainLoop()