import OpenGL

# Importação das bibliotecas
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500 #Definindo tamanho da grade
def square(): #Definindo o nome da função
    # Temos que declarar os pontos nesta sequência: inferior esquerdo, inferior direito, superior direito, superior esquerdo
    glBegin(GL_QUADS) #Começando o esboço
    glVertex2f(100, 100) # Coordenadas para o ponto inferior esquerdo
    glVertex2f(200, 100) # Coordenadas para o ponto inferior direito
    glVertex2f(150, 150) # Coordenadas para o ponto superior direito
    glVertex2f(150, 150) # Coordenadas para o ponto superior esquerdo
    glEnd() # Marque o final do desenho
    #2f -> 2d
    #3d -> 3d

# Função showScreen
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remova tudo da tela (ou seja, exibe tudo branco)
    glLoadIdentity() # Redefinir toda a posição do gráfico / forma
    iterate()
    glColor3f(1.0, 0.0, 3.0) #Define a cor para rosa
    square() # Chama a função
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500) # Defina w eh da sua janela
glutInitWindowPosition(0, 0) # Defina a posição em que essa janela deve aparecer
wind = glutCreateWindow("OpenGL Coding Practice") # Defina o titulo da janela
glutDisplayFunc(showScreen) # Abrir a janela
glutIdleFunc(showScreen) # Mantém a janela aberta
glutMainLoop() # Mantém a janela criada acima exibindo / executando em um loop