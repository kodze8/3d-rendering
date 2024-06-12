import numpy as np


class Cooridnate_generator:
    @staticmethod
    def cube_coordinates():
        cube = []

        def rec(current, n=3):
            if len(current) == n:
                cube.append(current)
            else:
                with_one = current.copy()
                with_one.append(-1)
                with_zero = current.copy()
                with_zero.append(1)
                rec(with_one, n)
                rec(with_zero, n)

        rec(cube)
        return cube

    @staticmethod
    def cube_connected_pair_indexes(cube_3d):
        list_pairs = []
        indexes = [x for x in range(len(cube_3d))]
        for x, a in zip(cube_3d, indexes):
            for y, b in zip(cube_3d, indexes):
                dis = round(sum([(x[i] - y[i]) ** 2 for i in range(0, 3)]))
                if dis == 4:
                    list_pairs.append((a, b))
        return list_pairs

    @staticmethod
    def generate_sphere_points(radius=1, num_points=100):
        sphere = []
        for _ in range(num_points):
            theta = np.random.uniform(0, 2 * np.pi)
            phi = np.random.uniform(0, np.pi)
            x = radius * np.sin(phi) * np.cos(theta)
            y = radius * np.sin(phi) * np.sin(theta)
            z = radius * np.cos(phi)
            sphere.append([x, y, z])
        return sphere

    # connect everything
    @staticmethod
    def sphere_connected_pair_indexes(sphere_3d):
        list_pairs = []
        indexes = [x for x in range(len(sphere_3d))]
        for a in indexes:
            for b in indexes:
                list_pairs.append((a, b))
        return list_pairs

    @staticmethod
    def generate_pyramid_points(base_size=2, height=2):
        half_base = base_size / 2
        points = [
            [0, 0, height],
            [-half_base, -half_base, 0], [half_base, -half_base, 0],
            [half_base, half_base, 0], [-half_base, half_base, 0]
        ]
        return points

    # add top
    @staticmethod
    def pyramid_connected_pair_indexes():
        list_pairs = []
        for i in range(5):
            if i == 0:
                for k in range(1, 5):
                    list_pairs.append((i, k))
            elif i < 4:
                list_pairs.append((i, i + 1))
            else:
                list_pairs.append((i, i - 3))
        return list_pairs

    @staticmethod
    def generate_torus_points(R=1.5, r=0.5, num_points=100):
        points = []
        for _ in range(num_points):
            theta = np.random.uniform(0, 2 * np.pi)
            phi = np.random.uniform(0, 2 * np.pi)
            x = (R + r * np.cos(phi)) * np.cos(theta)
            y = (R + r * np.cos(phi)) * np.sin(theta)
            z = r * np.sin(phi)
            points.append([x, y, z])
        return points

    # only connect in the same parts, doesn't work
    @staticmethod
    def torus_connected_pair_indexes(torus_3d):
        list_pairs = []
        indexes = [x for x in range(len(torus_3d))]
        for x, a in zip(torus_3d, indexes):
            for y, b in zip(torus_3d, indexes):
                if abs(x[0] + y[0]) > abs(x[0]) and abs(x[1] + y[1]) > abs(x[1]) and abs(x[2] + y[2]) > abs(x[2]):
                    list_pairs.append((a, b))
        return list_pairs

    # print(torus_connected_pair_indexes(generate_torus_points()))
