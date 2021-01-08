import pygame
from pygame.locals import *
import time
import random

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.apple_x = SIZE * 3
        self.apple_y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.apple, (self.apple_x, self.apple_y))
        pygame.display.flip()

    def move(self):
        self.apple_x = random.randint(1, 20) * SIZE
        self.apple_y = random.randint(1, 10) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.block_x = [SIZE] * length
        self.block_y = [SIZE] * length
        self.direction = 'down'
        self.length = length

    def draw(self):
        self.parent_screen.fill((71, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()

    def move(self):

        for i in range(self.length - 1, 0, -1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]

        if self.direction == 'left':
            self.block_x[0] -= SIZE

        if self.direction == 'right':
            self.block_x[0] += SIZE

        if self.direction == 'up':
            self.block_y[0] -= SIZE

        if self.direction == 'down':
            self.block_y[0] += SIZE

        self.draw()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        # This will set the size of the game window
        self.surface = pygame.display.set_mode((1000, 500))

        # This will set the color of window
        self.surface.fill((71, 110, 5))

        self.snake = Snake(self.surface, 2)
        self.snake.draw()

        self.apple = Apple(self.surface)
        self.apple.draw()

    def collision(self, sx, sy, ax, ay):
        if ax <= sx < ax + SIZE:
            if ay <= sy < ay + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (800, 100))

    def play(self):
        self.snake.move()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.apple_x, self.apple.apple_y):
            self.snake.increase_length()
            self.apple.move()

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.2)


if __name__ == '__main__':
    game = Game()
    game.run()
