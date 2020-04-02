# Importa a biblioteca pygame
import pygame

# cores
shape_color = (40, 210, 250)


def main():
    # inicia o Pygame
    pygame.init()

    # Dando nome ao título
    pygame.display.set_caption('Figura')

    # Define o tamanho da janela
    screen = pygame.display.set_mode((400, 400))

    # Desenhar a figura
    pointlist = [(150, 150), (100, 100), (200, 100)]
    pygame.draw.lines(screen, shape_color, True, pointlist, 1)

    # Atualiza a tela
    pygame.display.flip()

    # Mantem a janela aberta com um loop
    while True:
        # Retorna o evento
        event = pygame.event.wait()

        # Para fechar a janela
        if event.type == pygame.QUIT:
            break

    # finaliza o Pygame
    pygame.quit()


if __name__ == '__main__':
    main()