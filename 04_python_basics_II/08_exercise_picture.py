# Exercise !!
from bokeh.colors.groups import pink

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# print(picture)

new_list = []
for image in picture:
    for pixel in image:
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    print('')  # need a new line after each row
