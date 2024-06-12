import math
import numpy as np
screen_width = 600
screen_height = 800

def perpsective_projection_matrix(fov_radians = math.pi/2, aspect = 1, near = 1, far = 10):
    f = 1/math.tan(fov_radians/2)
    matrix = [[f/aspect, 0, 0, 0],
              [0, f, 0, 0],
              [0, 0, (far+near)/(near-far),2*far*near/(near-far)],
              [0, 0, -1, 0]]
    np_matrix = np.array(matrix)
    return np_matrix

def transform(coordinates_3d):
    transformation_matrix = perpsective_projection_matrix()
    transformed_coordinates = []

    for cor in coordinates_3d:
        cor = list(cor)
        cor.append(1)
        cor = np.array(cor)

        temp = []
        for row in transformation_matrix:
            temp.append(sum(cor*row))
        transformed_coordinates.append(temp)

    return transformed_coordinates

def get_2d_coordinates(coordinates_3d):
    transformed_coordinates = transform(coordinates_3d)
    coordinates_2d = []

    print(transformed_coordinates)
    for cor in transformed_coordinates:
        x = cor[0] / cor[3]  # Perspective divide
        y = cor[1] / cor[3]  # Perspective divide

        x_screen = (x + 1) / 2 * screen_width
        y_screen = (1 - y) / 2 * screen_height

        coordinates_2d.append((x_screen, y_screen))
    print(coordinates_2d)
    return coordinates_2d




coordinates_3d = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]])
get_2d_coordinates(coordinates_3d)


