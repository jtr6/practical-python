# bounce.py
#
# Exercise 1.5

height_init = 100       # height in meters
height = height_init
bounce = 0              # number of bounces

while bounce < 10:
    bounce += 1
    height = 0.6 * height
    print(bounce, round(height, 4))

