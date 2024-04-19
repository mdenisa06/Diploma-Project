import math


def fourier_transform(image):
    h, w = len(image), len(image[0])
    f_transform = [[0 for _ in range(w)] for _ in range(h)]

    for u in range(h):
        for v in range(w):
            sum_real = 0
            sum_imaginary = 0
            for x in range(h):
                for y in range(w):
                    intensity = image[x][y]
                    angle = -2 * math.pi * ((u * x / h) + (v * y / w))
                    sum_real += intensity * math.cos(angle)
                    sum_imaginary += intensity * math.sin(angle)
                f_transform[u][v] = complex(sum_real, sum_imaginary)

    return f_transform
