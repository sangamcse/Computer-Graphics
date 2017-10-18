from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw():
	r = 10
	cx,cy=0,0
	x,y=0,r
	p = 1 - r
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(5)
	glBegin(GL_POINTS)
	glColor3f(1.0, 0, 0)
	glVertex2f(x*0.1,y*0.1)
	glEnd()
	while (y>=x):

		if (p<0):
			x=x+1
			p = p + 2*x +1
		else:
			x=x+1
			y=y-1
			p = p + 2*x +1 - 2*y

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