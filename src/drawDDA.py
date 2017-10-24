from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glOrtho(-100,100,-100,100,-1,1)

def ROUND(a):
	return int(a + 0.5)

def point(x,y):

	glBegin(GL_POINTS)
	glColor3f(1.0, 0, 0)
	glVertex2d(x,y)
	glEnd()


def drawDDA():
	x1,y1,x2,y2 = -50,-25,20,40
	x,y = x1,y1
	dx = (x2-x1)
	dy = (y2-y1)
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(2)

	if abs(dx)>abs(dy):
		slope=dx

	else:
		slope=dy

	xi=dx/slope
	yi=dy/slope
	steps=int(slope)
	for i in range(steps):
		x = x + xi
		y = y + yi
		x = (ROUND(x))
		y = (ROUND(y))
		point(x,y)

	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow('DDALine')
init()
glutDisplayFunc(drawDDA)
glutMainLoop()
