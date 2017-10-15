from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


def ROUND(a):
	return int(a + 0.5)

def drawDDA():
	x1,y1,x2,y2 = -7,-5,2,4
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(4)
	x = (ROUND(x))
	y =	(ROUND(y))

	glBegin(GL_POINTS)
	glColor3f(1.0, 0, 0)
	glVertex2f(x*0.1,y*0.1)
	glEnd()

	for i in range(length):
		x += dx
		y += dy
		x = (ROUND(x))
		y = (ROUND(y))
		glBegin(GL_POINTS)
		glColor3f(1.0, 0, 0)
		glVertex2f(x*0.1,y*0.1)
		glEnd()

	glFlush()

glutInit(sys.argv)

glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow('DDALine')

glutDisplayFunc(drawDDA)
glutMainLoop()
