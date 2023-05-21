import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from math import log, log2

MAX_ITER = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER

    return n + 1 - log(log2(abs(z)))


def julia(c, z0):
    z = z0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER

    return n + 1 - log(log2(abs(z)))



mandelbrot_width = 2000
mandelbrot_height = 2000
re_start = -0.22
re_end = -0.219
im_start = -0.70
im_end = -0.699


julia_width = 2000
julia_height = 2000
julia_re_start = -0.5
julia_re_end = 0.3
julia_im_start = -0.5
julia_im_end = 0.3
julia_c = complex(0.285, 0.01)


mandelbrot_img = Image.new('RGB', (mandelbrot_width, mandelbrot_height))
mandelbrot_draw = ImageDraw.Draw(mandelbrot_img)

for x in range(mandelbrot_width):
    for y in range(mandelbrot_height):
        c = complex(re_start + (x / mandelbrot_width) * (re_end - re_start),
                    im_start + (y / mandelbrot_height) * (im_end - im_start))
        m = mandelbrot(c)
        color = (0, 0, 0) if m == MAX_ITER else (int(255 * m / MAX_ITER), 0, 0)
        mandelbrot_draw.point([x, y], color)


julia_img = Image.new('RGB', (julia_width, julia_height))
julia_draw = ImageDraw.Draw(julia_img)

for x in range(julia_width):
    for y in range(julia_height):
        z0 = complex(julia_re_start + (x / julia_width) * (julia_re_end - julia_re_start),
                     julia_im_start + (y / julia_height) * (julia_im_end - julia_im_start))
        m = julia(julia_c, z0)
        color = (0, 0, 0) if m == MAX_ITER else (0, int(255 * m / MAX_ITER), 0)
        julia_draw.point([x, y], color)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


ax1.imshow(mandelbrot_img)
ax1.set_title('Mandelbrot Fractal')
ax1.set_xlabel('Real')
ax1.set_ylabel('Imaginary')


ax2.imshow(julia_img)
ax2.set_title('Julia Set')
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')

plt.tight_layout()
plt.show()
