from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0,255,255) #konokichur color set (RGB)
    #call the draw methods here
    x,y=250,250
    c=1
    while c<=50:
        draw_points(x,y)
        x+=3
        y-=3
        c+=1
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1_20101528") #window name
glutDisplayFunc(showScreen)

glutMainLoop()