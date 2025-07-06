from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()



def DDA(x0,y0,x1,y1):
    dx=x1-x0
    dy=y1-y0
    step=None
    if abs(dy)>abs(dx):
        step=dy
    else:
        step=dx
    xinc=float(dx)/step
    yinc=float(dy)/step
    glBegin(GL_POINTS)
    glVertex2f(x0,y0)
    while y0<y1:
        if step==dx:
            x0 += xinc
            y0 += yinc
            glVertex2f(x0, round(y0))
        else:
            x0 += xinc
            y0 += yinc
            glVertex2f(round(x0), y0)
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
    glColor3f(204, 0, 0) #konokichur color set (RGB)
    #call the draw methods here
    x, y = 100, 350
    for i in range(50):
        if i==50//2:
            draw_points(x, y)
            DDA(x,y-200,x,y)
        else:
            draw_points(x, y)
        x += 5
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 3_20101528") #window name
glutDisplayFunc(showScreen)

glutMainLoop()