from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
def draw():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0, 0)
    glVertex2f(0,0)
    glVertex2f(0.20, 0.0)
    glVertex2f(0.20, 0.20)
    glVertex2f(0.0, 0.20)
    glVertex2f(0.10, 0.25)
    glEnd()
    glFlush()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(250, 250)
glutCreateWindow('Point Draw')
glutDisplayFunc(draw)
glutMainLoop()
