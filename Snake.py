import pygame

pygame.init()
display = pygame.display.set_mode((500,500))
pygame.display.update()
pygame.display.set_caption('Snake Game')
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            game_exit = True


pygame.quit()
quit()