#Importando a biblioteca Pygame
import pygame
#Iniciando o Pygame
pygame.init()

#Definir tamanho da janela
win = pygame.display.set_mode((700,700))
#Definir título para a janela
pygame.display.set_caption("Movimentando Uma Figura")

# x e y Define a posição inicial que o objeto
x = 150
y = 280
#Atribui valor a variáveis
a = 60
b = 60
#Define a velocidade de movimento
vel = 10

#Inicia o loop
run = True

while run:
    #Define um tempo de atraso(milissegundos)
    pygame.time.delay(100)

    #Percorre a lista de eventos do teclado ou mouse
    for event in pygame.event.get():
        #Verifica se o botão X foi clicado para fechar a janela
        if event.type == pygame.QUIT:
            #Encerra o loop
            run = False

    #Verifica se a tecla do pressionada
    keys = pygame.key.get_pressed()
    #Verifica qual tecla foi pressionada
    #Esquerda
    if keys[pygame.K_LEFT]:
        x -= vel
    #Direita
    if keys[pygame.K_RIGHT]:
        x += vel
    #Cima
    if keys[pygame.K_UP]:
        y -= vel
    #Baixo
    if keys[pygame.K_DOWN]:
        y += vel
    #Dimunuir
    if keys[pygame.K_d]:
        if a > 11 :
            a -= vel; b -= vel;
    #Aumentar
    if keys[pygame.K_a]:
        a += vel; b+=  vel;
    
    #Preencher com Branco o fundo
    win.fill((255,255,255)) 
    #Desenha a forma geométrica (Janela, Cor, Posicionamento/Tamanho)
    pygame.draw.rect(win, (0,0,0), (x, y, a, b))
    #Atualiza a Janela   
    pygame.display.update() 

#Encerra    
pygame.quit()


