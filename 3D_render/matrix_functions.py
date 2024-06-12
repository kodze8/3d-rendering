import math


class Matrix_manipulations:
    @staticmethod
    def identity_matrix():
        return [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]

    @staticmethod
    def matrix_rotation_x_axis(alpha_rad):
        return [[1, 0, 0],
                [0, math.cos(alpha_rad), -math.sin(alpha_rad)],
                [0, math.sin(alpha_rad), math.cos(alpha_rad)]]

    @staticmethod
    def matrix_rotation_y_axis(alpha_rad):
        return [[math.cos(alpha_rad), 0, math.sin(alpha_rad)],
                [0, 1, 0],
                [- math.sin(alpha_rad), 0, math.cos(alpha_rad)]]

    @staticmethod
    def matrix_rotation_z_axis(alpha_rad):
        return [[math.cos(alpha_rad), -math.sin(alpha_rad), 0],
                [math.sin(alpha_rad), math.cos(alpha_rad), 0],
                [0, 0, 1]]

    @staticmethod
    def scale_matrix(k):
        return [[k, 0, 0],
                [0, k, 0],
                [0, 0, k]]

    @staticmethod
    def matrix_multiplication(coordinates, transformation_matrix):
        transformed_coordinates = []
        for cor in coordinates:
            temp = []
            for row in transformation_matrix:
                temp.append(sum([x[0] * x[1] for x in zip(row, cor)]))
            transformed_coordinates.append(temp)
        return transformed_coordinates

    @staticmethod
    def project_on_xy(coordinates_3d):
        matrix = [[1, 0, 0], [0, 1, 0]]
        return Matrix_manipulations.matrix_multiplication(coordinates_3d, matrix)
