import math


def __matrix_rotation_x_axis(alpha_rad):
    return [[1, 0, 0],
            [0, math.cos(alpha_rad), -math.sin(alpha_rad)],
            [0, math.sin(alpha_rad), math.cos(alpha_rad)] ]


def __matrix_rotation_y_axis(alpha_rad):
    return [[math.cos(alpha_rad), 0, math.sin(alpha_rad)],
            [0, 1, 0],
            [- math.sin(alpha_rad), 0, math.cos(alpha_rad)] ]


def __matrix_rotation_z_axis(alpha_rad):
    return [[math.cos(alpha_rad), -math.sin(alpha_rad), 0],
            [math.sin(alpha_rad), math.cos(alpha_rad), 0],
            [0, 0, 1]]

def rotate(coordinates_3d, alpha, x = True, y= False, z = False):
    alpha = math.radians(alpha)

    if x:
        transformation_matrix = __matrix_rotation_x_axis(alpha)
    elif y:
        transformation_matrix = __matrix_rotation_y_axis(alpha)
    elif z:
        transformation_matrix = __matrix_rotation_z_axis(alpha)

    transformed_coordinates = __matrix_multiplication(coordinates_3d,transformation_matrix)

    return transformed_coordinates


def __matrix_multiplication(coordinates, transformation_matrix):
    transformed_coordinates = []
    for cor in coordinates:
        temp = []
        for row in transformation_matrix:
            temp.append(sum([x[0]*x[1] for x in zip(row, cor)]))
        transformed_coordinates.append(temp)
    return transformed_coordinates

def project_on_xy(coordinates_3d):
    matrix = [[1,0,0], [0,1,0]]
    return __matrix_multiplication(coordinates_3d, matrix)

def scale_coordinates(coordinates, screen_width, screen_height):
    # coordinates_2d = []
    # for x, y in coordinates:
    #     x_screen = (x + 1) / 2 * screen_width
    #     y_screen = (1 - y) / 2 * screen_height
    #     coordinates_2d.append((x_screen, y_screen))
    # return coordinates_2d

    scaled_points = []
    for x, y in coordinates:
        scaled_x = int(screen_width/2 + x * screen_width/4)
        scaled_y = int(screen_height/2 - y * screen_height/4)
        scaled_points.append((scaled_x, scaled_y))
    return scaled_points


# coord = help.cube_coordinates()
# coord_2 = rotate(coord, math.pi/2, x = True)
# print(coord_2)
# print("--------")
# coord_2 = project_on_xy(coord_2)
# print(coord_2)

