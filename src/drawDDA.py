from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glOrtho(-100,100,-100,100,-1,1)

def point(x,y):

	glBegin(GL_POINTS)
	glColor3f(1.0, 0, 0)
	glVertex2d(x,y)
	glEnd()


def drawDDA():
	x1,y1,x2,y2 = 20,25,-25,-20
	dx = (x2-x1)
	dy = (y2-y1)
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(2)
	steps=1
	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	xi=yi=x=y=0.0
	xi = dx / float(steps)
	yi = dy / float(steps)

	x = x1
	y = y1
	i=0
	for i in range(1,steps):
		point(x,y)
		x=x+xi
		y=y+yi

	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow('DDALine')
init()
glutDisplayFunc(drawDDA)
glutMainLoop()
