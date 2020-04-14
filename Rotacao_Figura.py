# Funcionalidades do Sistema
import os

# imports the Pygame library
import pygame

# Cor
black = (0, 0, 0)

def main():
    # Iniciando Pygame
    pygame.init()

    # Título
    window_title = u'Rotate image'
    pygame.display.set_caption(window_title)

    # Janela
    window_size = (600, 600)
    screen = pygame.display.set_mode(window_size)

    # Ocupação da figura na janela no centro
    screen_rect = screen.get_rect()
    screen_center = screen_rect.center

    # Carregando Imagem
    image = pygame.image.load(os.path.join('imagens', 'pygame_logo.png'))

    # Converter imagem para ser compativel
    image = image.convert_alpha()

    # Angulo de rotação
    rotation_angle = 90

    # Clock
    clock = pygame.time.Clock()

    # Verifica se a aplicação está em execução
    is_running = True
	
    # x e y Define a posição inicial que o objeto
    x = 150
    y = 280

    #Atribui valor a variáveis
    a = 60
    b = 60

    #Define o tamanho do movimento
    vel = 10


    # Inicia aplicação LOOP
    while is_running:
        # Limite de 30 FPS
        clock.tick(30)

        # Verifica se mantem a janela aberta
        for event in pygame.event.get():
            # Verifica se o botão X foi pressionado
            if event.type == pygame.QUIT:
                # Para a aplicação
                is_running = False

            # Verifica se alguma tecla foi precionada
            if event.type == pygame.KEYDOWN:
                #Rotacionar
                if event.key == pygame.K_SPACE:
                    image = pygame.transform.rotate(image, rotation_angle)
                #Esquerda
                if event.key == pygame.K_LEFT:
                    x -= vel
                #Direita
                if event.key == pygame.K_RIGHT:
                    x += vel
                #Cima
                if event.key == pygame.K_UP:
                    y -= vel
                #Baixo
                if event.key == pygame.K_DOWN:
                    y += vel
                #Dimunuir
                if event.key == pygame.K_d:
                    if a > 11 :
                        a -= vel; b -= vel;
                #Aumentar
                if event.key == pygame.K_a:
                    a += vel; b+=  vel;


        # Cor de Fundo
        screen.fill(black)
        
        nova_image = pygame.transform.scale(image,(a, b))

        # Posicionando imagem na janela
        screen.blit(nova_image, (x, y))

        # Atualiza a janela
        pygame.display.flip()

    # finalia o Pygame
    pygame.quit()


if __name__ == '__main__':
    main()

