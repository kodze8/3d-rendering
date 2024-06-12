from matrix_functions import Matrix_manipulations

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 700

class Axis:

    move_step = 1

    def __init__(self):
        self.axis_coordinates_3d = Axis.center() + Axis.x_cor() + Axis.y_cor() + Axis.z_cor()
        self.x_color = (255, 255, 51)
        self.y_color = (30, 144, 255)
        self.z_color = (255, 99, 71)
        self.axis_coordinates_2d = Matrix_manipulations.project_on_xy(self.axis_coordinates_3d)
        self.scale_coordinates()
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0

    def get_center(self):
        return self.axis_coordinates_2d[0]

    def scale_coordinates(self):
        scaled_points = []
        for x, y in self.axis_coordinates_2d:
            scaled_x = int(SCREEN_WIDTH / 2 + x * SCREEN_WIDTH / 3)
            scaled_y = int(SCREEN_HEIGHT / 2 - y * SCREEN_HEIGHT / 3)
            scaled_points.append([scaled_x, scaled_y])
        self.axis_coordinates_2d = scaled_points

    @staticmethod
    def x_cor():
        return [[-1, 0, 0], [1, 0, 0]]

    @staticmethod
    def center():
        return [[0, 0, 0]]

    @staticmethod
    def y_cor():
        return [[0, -1, 0], [0, 1, 0]]

    @staticmethod
    def z_cor():
        return [[0, 0, -1], [0, 0, 1]]
