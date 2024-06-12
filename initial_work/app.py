import pygame
import cor_generator
import rotations

CUBE_3D_COORDINATES = cor_generator.cube_coordinates()
WIDTH, HEIGHT = 800, 800
RED = (255, 0, 0)
def draw_cube(cube_coordinates):
    for x in cube_coordinates:
        pygame.draw.circle(screen, RED, (x[0], x[1]), 10)

def draw_lines(cube_2d, cube_3d):
    for x, a in zip(cube_3d, cube_2d):
        for y, b in zip(cube_3d, cube_2d):
            dis = round(sum([(x[i] - y[i])**2 for i in range(0,3)]))
            if dis ==4:
                pygame.draw.line(screen, RED, a, b)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True


alpha = 10

rotated = CUBE_3D_COORDINATES
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # alpha += 10
    # rotated = rotations.rotate(rotated, alpha)
    rotated = rotations.rotate(rotated, alpha, x=False, y=True)
    rotated = rotations.rotate(rotated, alpha, x=False, z=True)
    pygame.time.delay(100)

    cube_2d_cor = rotations.project_on_xy(rotated)
    cube_2d_cor = rotations.scale_coordinates(cube_2d_cor, WIDTH / 2, HEIGHT / 2)
    draw_cube(cube_2d_cor)
    draw_lines(cube_2d_cor, rotated)
    pygame.display.update()

