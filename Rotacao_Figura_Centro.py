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
    size = (600, 600)
    screen = pygame.display.set_mode(size)

    # Ocupação da figura na janela no centro
    screen_rect = screen.get_rect()

    # Carregando Imagem
    image_orig = pygame.image.load(os.path.join('imagens', 'pygame_logo.png'))
    
    # Converter imagem para ser compativel
    image_conv = image_orig.convert_alpha()
    image = image_conv.copy()


    # Angulo de rotação
    rotation_angle = 0

    # Clock
    clock = pygame.time.Clock()

    # Verifica se a aplicação está em execução
    is_running = True
	
    # x e y Define a posição inicial que o objeto
    x = 380
    y = 350

    #Atribui valor a variáveis
    a = 60
    b = 60

    #Define o tamanho do movimento
    vel = 10

    image_rect = image_orig.get_rect(center=[x, y])

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
                    rotation_angle += 9;
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
        
        # Redimensionar Figura
        imagem = pygame.transform.scale(image_orig, (a, b))
        
        # Mover Figura
        image_rect = image_orig.get_rect(center=[x, y])
        
        # Processo de pegar o centro da figura e rotacionar
        image_rect = image.get_rect(center=image_rect.center)
        image = pygame.transform.rotate(imagem, rotation_angle)
        
        # Exibir figura na tela
        screen.blit(image, image_rect)
        
        # Atualiza a janela
        pygame.display.flip()

    # finalia o Pygame
    pygame.quit()


if __name__ == '__main__':
    main()

