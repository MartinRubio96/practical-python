# bounce.py
#
# Exercise 1.5

height = 100
bounces = 1

while bounces <= 10:
    height = round(height * 3 / 5,4)
    print(bounces, height)
    bounces = bounces + 1