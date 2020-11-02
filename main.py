import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 400, 400
collide = False

rect_size = w, h = 70, 70
rect_pos = ((WIDTH_WIN - w) // 2, (HEIGHT_WIN - h) // 2)

circle_radius = 35
circle_pos = (0, 0)

RED = (255, 0, 0, 180)
BLUE = (0, 0, 255, 180)
YELLOW = (255, 255, 0, 180)
BG = (128, 128, 128)
x = 0
block = False

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
font = pygame.font.SysFont('Arial', 24, True, False)
FPS = 60
clock = pygame.time.Clock()

surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
            e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1_center = e.pos

    screen.fill(BG)

    # rect1 = pygame.draw.circle(screen, YELLOW, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))

    if rect1.colliderect(rect2):
        collide = True
        if not block:
            x += 1
        block = True
    else:
        collide = False
        block = False

    screen.blit(surface, rect1)
    screen.blit(font.render(str(x), 1, RED), (10,10))
    pygame.display.update()
    clock.tick(FPS)