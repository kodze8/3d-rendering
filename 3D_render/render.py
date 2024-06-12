import pygame
from cor_generator import *
from object import *

WIDTH, HEIGHT = axis.SCREEN_WIDTH, axis.SCREEN_HEIGHT
BEIGE = (245, 245, 220)
FILL_COLOR = (255, 255, 51)
RADIUS = 5
ALPHA = 2
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Render")
FONT = pygame.font.SysFont("Tiny5", 34)
BACKGROUND_COLOR = (0, 0, 51)

BUTTON_X = 700
BUTTON_Y = 110
BUTTON_DISTANCE = 70


def figure_button(x, y, figure_name, font, color=BEIGE):
    BUTTON_CONTINUE_GAME = pygame.Rect(x, y, 100, 50)
    pygame.draw.rect(screen, color, BUTTON_CONTINUE_GAME)
    screen.blit(font.render(f"{figure_name}", False, (0, 0, 0)),
                (BUTTON_CONTINUE_GAME.x, BUTTON_CONTINUE_GAME.y + 10))
    return BUTTON_CONTINUE_GAME


def cube_button(font):
    return figure_button(BUTTON_X, BUTTON_Y, "cube", font)


def sphere_button(font):
    return figure_button(BUTTON_X, BUTTON_Y + BUTTON_DISTANCE, "Sphere", font)


def pyramid_button(font):
    return figure_button(BUTTON_X, BUTTON_Y + 2 * BUTTON_DISTANCE, "Pyramid", font)


def Torus_button(font):
    return figure_button(BUTTON_X, BUTTON_Y + 3 * BUTTON_DISTANCE, "Torus", font)


def fill_button(font):
    return figure_button(BUTTON_X, BUTTON_Y - BUTTON_DISTANCE, "Fill", font, color=FILL_COLOR)


def draw_vertices(cube_coordinates):
    for x in cube_coordinates:
        pygame.draw.circle(screen, BEIGE, (x[0], x[1]), RADIUS)


def draw_edges(list_pairs, cube_2d):
    for pair in list_pairs:
        pygame.draw.line(screen, BEIGE, cube_2d[pair[0]], cube_2d[pair[1]])


def draw_axes(axis_object):
    cor_2d = axis_object.axis.axis_coordinates_2d
    for i in range(len(cor_2d)):
        if i < 3:
            pygame.draw.line(screen, axis_object.axis.x_color, cor_2d[i], axis_object.axis.get_center())
        elif 2 < i < 5:
            pygame.draw.line(screen, axis_object.axis.y_color, cor_2d[i], axis_object.axis.get_center())
        else:
            pygame.draw.line(screen, axis_object.axis.z_color, cor_2d[i], axis_object.axis.get_center())


def render():
    running = True
    rotate = False
    fill = False

    # In default cube is rendered
    CUBE_3D_COORDINATES = Cooridnate_generator.cube_coordinates()
    figure = Object(CUBE_3D_COORDINATES, Cooridnate_generator.cube_connected_pair_indexes(CUBE_3D_COORDINATES))

    while running:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if sphere_button(FONT).collidepoint(mouse_pos):
                    fill = False
                    sphere_3d = Cooridnate_generator.generate_sphere_points()
                    figure = Object(sphere_3d, Cooridnate_generator.sphere_connected_pair_indexes(sphere_3d))
                elif cube_button(FONT).collidepoint(mouse_pos):
                    fill = False
                    cube_3d = Cooridnate_generator.cube_coordinates()
                    figure = Object(cube_3d, Cooridnate_generator.cube_connected_pair_indexes(cube_3d))
                elif Torus_button(FONT).collidepoint(mouse_pos):
                    fill = False
                    torus_3d = Cooridnate_generator.generate_torus_points()
                    figure = Object(torus_3d, Cooridnate_generator.torus_connected_pair_indexes(torus_3d))
                elif pyramid_button(FONT).collidepoint(mouse_pos):
                    fill = False
                    pyramid_3d = Cooridnate_generator.generate_pyramid_points()
                    figure = Object(pyramid_3d, Cooridnate_generator.pyramid_connected_pair_indexes())
                elif fill_button(FONT).collidepoint(mouse_pos):
                    fill = not fill

            # rotate in x, y, z direction
            if event.type == pygame.MOUSEBUTTONDOWN:
                rotate = True
            if event.type == pygame.MOUSEBUTTONUP:
                rotate = False
            if event.type == pygame.MOUSEMOTION:
                if rotate:
                    dx, dy = event.rel
                    if dy > 0:
                        figure.rotate(ALPHA, x=True)
                    elif dy < 0:
                        figure.rotate(-ALPHA, x=True)
                    if dx > 0:
                        figure.rotate(ALPHA, y=True)
                    elif dx < 0:
                        figure.rotate(-ALPHA, y=True)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                figure.rotate(ALPHA, z=True)
            if keys[pygame.K_x]:
                figure.rotate(-ALPHA, z=True)

            # Update the keys you are suing for enlarging
            if keys[pygame.K_m]:
                figure.enlarge(1.1)
            elif keys[pygame.K_n]:
                figure.enlarge(float(1 / 1.1))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            figure.move(right=True)
        elif keys[pygame.K_LEFT]:
            figure.move(left=True)
        elif keys[pygame.K_UP]:
            figure.move(up=True)
        elif keys[pygame.K_DOWN]:
            figure.move(down=True)

        draw_vertices(figure.coordinates_2d)
        if fill:
            draw_edges(figure.pair_index, figure.coordinates_2d)

        draw_axes(figure)

        cube_button(FONT)
        sphere_button(FONT)
        pyramid_button(FONT)
        Torus_button(FONT)
        fill_button(FONT)

        pygame.display.update()


if __name__ == '__main__':
    render()
