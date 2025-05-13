import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
DANCER_SIZE = 10
MOVE_SPEED = 0.05  # Moves 5% towards target
BACKGROUND_COLOR = (30, 30, 30)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Dancer:
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(0, WIDTH)
        self.y = y if y is not None else random.randint(0, HEIGHT)
        self.target_x = self.x
        self.target_y = self.y
        self.size = DANCER_SIZE
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def __str__(self):
        return f"Dancer({self.x:.2f}, {self.y:.2f})"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def move(self):
        self.x += (self.target_x - self.x) * MOVE_SPEED
        self.y += (self.target_y - self.y) * MOVE_SPEED

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y

# Create initial list of dancers
dancers = [Dancer() for _ in range(5)]

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dancers[0].set_target(mouse_x, mouse_y)  # First dancer follows mouse

    # Move and update dancers
    for i in range(len(dancers)):
        if i > 0:
            dancers[i].set_target(dancers[i - 1].x, dancers[i - 1].y)
        dancers[i].move()
        dancers[i].draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:  # Add new dancer
                dancers.append(Dancer())
            elif event.key == pygame.K_q:  # Quit program
                running = False

    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
