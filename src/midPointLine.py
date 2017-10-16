from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw():
	x1,y1 = -7,-5
	x2,y2 = 2,4
	dx = x2 - x1
	dy = y2 - y1
	d = dy - (dx/2)
	x,y = x1,y1
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(5)
	glBegin(GL_POINTS)
	glColor3f(1.0, 0, 0)
	glVertex2f(x*0.1,y*0.1)
	glEnd()
	while (x < x2):
	 	x=x+1
	 	if(d<0):
	 		d=d+dy

	 	else:
	 		d=d+(dy - dx)
	 		y=y+1

	 	glBegin(GL_POINTS)
		glColor3f(1.0, 0, 0)
		glVertex2f(x*0.1,y*0.1)
		glEnd()

	glFlush()

glutInit(sys.argv)

glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(250, 250)
glutCreateWindow('Mid-point Line')
glutDisplayFunc(draw)
glutMainLoop()