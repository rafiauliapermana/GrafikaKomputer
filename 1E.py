# Nama  : Rafi Aulia Permana
# NIM   : 20051397071
# Prodi : D4 Manajemen Informatika (2020A)
# Praktikum 1 Grafika Komputer

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-6, 6, -6, 6, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.00)
    glVertex2f(6.00, 4.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(2.00, 1.00)
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutCreateWindow("Praktikum 1 Grafika Komputer - No. 1E")
glutDisplayFunc(draw)
glutMainLoop()