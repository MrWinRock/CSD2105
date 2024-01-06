import matplotlib.pyplot as plt


def draw_circle(radius):
    x = 0
    y = radius
    p = 1 - radius

    x_points = []
    y_points = []

    while x <= y:
        plot_octant_points(x, y, x_points, y_points)
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1

    # Reflect and add points to complete the circle
    all_points = list(zip(x_points, y_points))
    all_points.extend([(y, x) for x, y in all_points])
    all_points.extend([(-x, y) for x, y in all_points])
    all_points.extend([(-y, x) for x, y in all_points])
    all_points.extend([(x, -y) for x, y in all_points])
    all_points.extend([(y, -x) for x, y in all_points])
    all_points.extend([(-x, -y) for x, y in all_points])
    all_points.extend([(-y, -x) for x, y in all_points])

    x_points, y_points = zip(*all_points)

    plt.scatter(x_points, y_points, marker='o')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def plot_octant_points(x, y, x_points, y_points):
    x_points.append(x)
    y_points.append(y)


def main():
    radius = 25
    draw_circle(radius)


if __name__ == "__main__":
    main()