from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawLines1():
    glBegin(GL_LINES)
    glVertex2f(200, 300)
    glVertex2f(200, 100)
    glVertex2f(300, 300)
    glVertex2f(300, 100)
    glVertex2f(200, 100)
    glVertex2f(300, 100)
    glEnd()
def drawLines2():
    glBegin(GL_LINES)
    glVertex2f(205, 290)
    glVertex2f(235, 290)
    glVertex2f(205, 290)
    glVertex2f(205, 250)
    glVertex2f(205, 250)
    glVertex2f(235, 250)
    glVertex2f(235, 250)
    glVertex2f(235, 290)
    glEnd()
def drawLines3():
    glBegin(GL_LINES)
    glVertex2f(295, 290)
    glVertex2f(295, 250)
    glVertex2f(295, 290)
    glVertex2f(265, 290)
    glVertex2f(265, 290)
    glVertex2f(265, 250)
    glVertex2f(265, 250)
    glVertex2f(295, 250)
    glEnd()
def drawLines4():
    glBegin(GL_LINES)
    glVertex2f(240, 220)
    glVertex2f(255, 220)
    glVertex2f(240, 220)
    glVertex2f(240, 100)
    glVertex2f(255, 220)
    glVertex2f(255, 100)
    glEnd()
def drawTriangle():
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 300)
    glVertex2f(300, 300)
    glVertex2f(250, 350)
    glEnd()
def draw_points(x, y):
    glPointSize(3) #pixel size. by default 1 thake
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
    glColor3f(255, 255, 255) #konokichur color set (RGB)
    #call the draw methods here
    drawTriangle()
    drawLines1()
    drawLines2()
    drawLines3()
    drawLines4()
    draw_points(248,160)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2_20101528") #window name
glutDisplayFunc(showScreen)
glutMainLoop()