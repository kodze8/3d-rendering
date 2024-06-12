from matrix_functions import *
from axis import Axis
import axis


class Object:
    screen_width = axis.SCREEN_WIDTH
    screen_height = axis.SCREEN_HEIGHT
    move_step = 1

    def __init__(self, coordinates, connected_vertices_indexes):
        self.coordinates_3d = coordinates
        self.coordinates_2d = Matrix_manipulations.project_on_xy(self.coordinates_3d)
        self.__scale_coordinates()
        self.axis = Axis()
        self.pair_index = connected_vertices_indexes

    def __scale_coordinates(self):
        scaled_points = []
        for x, y in self.coordinates_2d:
            scaled_x = int(self.screen_width / 2 + x * self.screen_width / 8)
            scaled_y = int(self.screen_height / 2 - y * self.screen_height / 8)
            scaled_points.append([scaled_x, scaled_y])
        self.coordinates_2d = scaled_points

    def rotate(self, alpha, x=False, y=False, z=False):
        alpha = math.radians(alpha)
        transformation_matrix = Matrix_manipulations.identity_matrix()
        if x:
            transformation_matrix = Matrix_manipulations.matrix_rotation_x_axis(alpha)
            self.axis.x_angle += alpha
        elif y:
            transformation_matrix = Matrix_manipulations.matrix_rotation_y_axis(alpha)
            self.axis.y_angle += alpha
        elif z:
            transformation_matrix = Matrix_manipulations.matrix_rotation_z_axis(alpha)
            self.axis.z_angle += alpha

        self.coordinates_3d = Matrix_manipulations.matrix_multiplication(self.coordinates_3d, transformation_matrix)
        self.coordinates_2d = Matrix_manipulations.project_on_xy(self.coordinates_3d)

        self.axis.axis_coordinates_3d = Matrix_manipulations.matrix_multiplication(self.axis.axis_coordinates_3d,
                                                                                   transformation_matrix)
        self.axis.axis_coordinates_2d = Matrix_manipulations.project_on_xy(self.axis.axis_coordinates_3d)
        self.__scale_coordinates()
        self.axis.scale_coordinates()

    def enlarge(self, k):
        transformation_matrix = Matrix_manipulations.scale_matrix(k)
        self.coordinates_3d = Matrix_manipulations.matrix_multiplication(self.coordinates_3d, transformation_matrix)
        self.coordinates_2d = Matrix_manipulations.project_on_xy(self.coordinates_3d)

        self.axis.axis_coordinates_3d = Matrix_manipulations.matrix_multiplication(self.axis.axis_coordinates_3d,
                                                                                   transformation_matrix)
        self.axis.axis_coordinates_2d = Matrix_manipulations.project_on_xy(self.axis.axis_coordinates_3d)
        self.__scale_coordinates()
        self.axis.scale_coordinates()

    def move(self, left=False, right=False, up=False, down=False):

        def update_coordinate(coordinates_2d, dx, dy):
            for x in coordinates_2d:
                x[0] += dx
                x[1] += dy
            return coordinates_2d

        x_step = 0
        y_step = 0

        if left and min([x[0] for x in self.coordinates_2d]) > 0:
            x_step = -self.move_step
        elif right and max([x[0] for x in self.coordinates_2d]) < self.screen_width:
            x_step = self.move_step
        elif up and min([x[1] for x in self.coordinates_2d]) > 0:
            y_step = -self.move_step
        elif down and max([x[1] for x in self.coordinates_2d]) < self.screen_height:
            y_step = self.move_step

        self.coordinates_2d = update_coordinate(self.coordinates_2d, x_step, y_step)
        self.axis.axis_coordinates_2d = update_coordinate(self.axis.axis_coordinates_2d, x_step, y_step)
