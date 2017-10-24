from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

xc=0
yc=0

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glOrtho(-100,150,-100,150,-1,1)

def point(x,y):
	glBegin(GL_POINTS)
	glColor3f(1.0, 0, 0)
	glVertex2d(xc-x,yc+y)
	glVertex2d(xc+x,yc-y)
	glEnd()

def draw():
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(2)
	xc=200
	yc=200
	a=100
	b=70
	x,y=0,b
	point(x,y)
	p1=(b*b)-(a*a*b)+(a*a)/4
	while ((2.0*b*b*x)<=(2.0*a*a*y)):
		x=x+1
		if (p1<=0):
			p1=p1+(2.0*b*b*x)+(b*b)
		else:
			y=y-1
			p1=p1+(2.0*b*b*x)+(b*b)-(2.0*a*a*y)
		point(x,y)
		x=-x
		point(x,y)
		x=-x
	x=a
	y=0
	point(x,y)
	p2=(a*a)+2.0*(b*b*a)+(b*b)/4
	while ((2.0*b*b*x)>(2.0*a*a*y)):
		y=y+1
		if (p2>0):
			p2=p2+(a*a)-(2.0*a*a*y)
		else:
			x=x-1
			p2=p2+(2.0*b*b*x)-(2.0*a*a*y)+(a*a)
		point(x,y)
		y=-y
		point(x,y)
		y=-y
	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(1000, 1500)
glutCreateWindow('Mid-point Ellipse')
init()
glutDisplayFunc(draw)
glutMainLoop()