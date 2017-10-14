from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


def circlecxcy():
	cx=0
	cy=0
	r=1
	angl = 0
	print math.sin(30*(math.pi)/180)
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(2)
	for angl in range(0,360):
		x = cx + r*(math.cos(angl*(math.pi)/180))
		y = cy + r*(math.sin(angl*(math.pi)/180))
		glBegin(GL_POINTS)
		glColor3f(1.0, 0, 0)
		glVertex2f(x,y)
		glEnd()

	glFlush()

glutInit(sys.argv)

glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(250, 250)
glutCreateWindow('Circle Draw')

glutDisplayFunc(circlecxcy)
glutMainLoop()