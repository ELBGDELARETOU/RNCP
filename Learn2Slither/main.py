import pygame
from game import SnakeGame

def draw_game(screen, game):
    screen.fill((0,0,0))
    for x, y in game.snake:
        pygame.draw.rect(screen, (0,255,0), (x*40, y*40, 40, 40))
    gx, gy = game.g_apple
    pygame.draw.rect(screen, (0, 200, 0), (gx*40, gy*40, 40 ,40))
    rx, ry = game.r_apple
    pygame.draw.rect(screen, (255, 0, 0), (rx*40, ry*40, 40 ,40))
    pygame.display.flip()

def main():
    pygame.init()
    game = SnakeGame()
    screen = pygame.display.set_mode((game.width*40, game.height*40))
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(5)

        action = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    action = 1
                elif event.key == pygame.K_RIGHT:
                    action = 2

        game.step(action)
        draw_game(screen, game)
        
        if game.game_over:
            pygame.time.wait(1000)
            game._reset()

    pygame.quit()

if __name__ == "__main__":
    main()