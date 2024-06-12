import numpy as np
import math

# Helper function to connect points within a certain distance
def generate_lines_from_points(points, max_distance):
    lines = set()
    num_points = len(points)
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = np.linalg.norm(np.array(points[i]) - np.array(points[j]))
            if distance <= max_distance:
                line = tuple(sorted((tuple(points[i]), tuple(points[j]))))
                lines.add(line)
    return lines

# Generate cube vertices and edges
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
    rec([])
    return cube

def line_coordinates(cube):
    lines = set()
    for x in cube:
        for y in cube:
            if x != y:
                diff = sum(1 for i in range(3) if x[i] != y[i])
                if diff == 1:
                    line = tuple(sorted((tuple(x), tuple(y))))
                    lines.add(line)
    return lines

# Generate sphere vertices and edges
def generate_sphere_points(radius, num_points):
    points = []
    for _ in range(num_points):
        theta = np.random.uniform(0, 2 * np.pi)
        phi = np.random.uniform(0, np.pi)
        x = radius * np.sin(phi) * np.cos(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(phi)
        points.append([x, y, z])
    return points

# Generate pyramid vertices and edges
def generate_pyramid_points(base_size, height):
    half_base = base_size / 2
    points = [
        [-half_base, -half_base, 0], [half_base, -half_base, 0],
        [half_base, half_base, 0], [-half_base, half_base, 0],
        [0, 0, height]
    ]
    lines = [
        (points[0], points[1]), (points[1], points[2]), (points[2], points[3]), (points[3], points[0]),
        (points[0], points[4]), (points[1], points[4]), (points[2], points[4]), (points[3], points[4])
    ]
    return points, lines

# Generate torus vertices and edges
def generate_torus_points(R, r, num_points):
    points = []
    for _ in range(num_points):
        theta = np.random.uniform(0, 2 * np.pi)
        phi = np.random.uniform(0, 2 * np.pi)
        x = (R + r * np.cos(phi)) * np.cos(theta)
        y = (R + r * np.cos(phi)) * np.sin(theta)
        z = r * np.sin(phi)
        points.append([x, y, z])
    return points

# Generate crown vertices and edges
def generate_crown_points(base_radius=2, spike_height=3, num_spikes=10, base_height=1):
    points = []

    # Generate points for the circular base
    for i in range(num_spikes):
        angle = 2 * math.pi * i / num_spikes
        x = base_radius * math.cos(angle)
        y = base_radius * math.sin(angle)
        z = 0  # Base at height 0
        points.append((x, y, z))
        points.append((x, y, base_height))  # Top edge of the base

    # Generate points for the spikes
    for i in range(num_spikes):
        angle = 2 * math.pi * i / num_spikes
        next_angle = 2 * math.pi * (i + 1) / num_spikes
        x1 = base_radius * math.cos(angle)
        y1 = base_radius * math.sin(angle)
        x2 = base_radius * math.cos(next_angle)
        y2 = base_radius * math.sin(next_angle)
        z_base = base_height
        z_tip = base_height + spike_height

        # Base vertices of the spike
        points.append((x1, y1, z_base))
        points.append((x2, y2, z_base))

        # Tip of the spike
        points.append(((x1 + x2) / 2, (y1 + y2) / 2, z_tip))

    lines = generate_lines_from_points(points, max_distance=base_radius)

    return points, lines

# Generate and print cube points and lines
cube_points = cube_coordinates()
cube_lines = line_coordinates(cube_points)
print("Cube Points:", cube_points)
print("Cube Lines:", list(cube_lines))

# Generate and print sphere points and lines
sphere_points = generate_sphere_points(1, 100)
sphere_lines = generate_lines_from_points(sphere_points, max_distance=0.2)
print("Sphere Points:", sphere_points)
print("Sphere Lines:", list(sphere_lines))

# Generate and print pyramid points and lines
pyramid_points, pyramid_lines = generate_pyramid_points(2, 3)
print("Pyramid Points:", pyramid_points)
print("Pyramid Lines:", pyramid_lines)

# Generate and print torus points and lines
torus_points = generate_torus_points(3, 1, 100)
torus_lines = generate_lines_from_points(torus_points, max_distance=0.5)
print("Torus Points:", torus_points)
print("Torus Lines:", list(torus_lines))

# Generate and print crown points and lines
crown_points, crown_lines = generate_crown_points()
print("Crown Points:", crown_points)
print("Crown Lines:", list(crown_lines))
