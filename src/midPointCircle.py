from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glOrtho(-100,100,-100,100,-1,1)

def point(x,y):
	glBegin(GL_POINTS)
	glColor3f(1.0, 0, 0)
	glVertex2d(x,y);
	glVertex2d(-x,y);
	glVertex2d(-x,-y);
	glVertex2d(x,-y);
	glVertex2d(y,x);
	glVertex2d(-y,x);
	glVertex2d(-y,-x);
	glVertex2d(y,-x);
	glEnd()

def draw():
	r = 100
	cx,cy=0,0
	x,y=0,r
	p =  - r
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(2)
	point(x,y)
	while (y>=x):
		if (p<0):
			x=x+1
			p = p + 2*x +1
		else:
			x=x+1
			y=y-1
			p = p + 2*x +1 - 2*y

		point(x,y)

	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow('Mid-point Circle')
init()
glutDisplayFunc(draw)
glutMainLoop()