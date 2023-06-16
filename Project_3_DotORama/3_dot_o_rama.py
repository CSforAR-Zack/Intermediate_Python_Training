from turtle import Turtle, Screen
from random import randint

def main():
    t = Turtle()
    s = Screen()

    # Uncomment tracer to make instant-ish
    # s.tracer(0)
    s.bgcolor('black')
    t.speed(0)
    t.penup()

    colors: list = ['hotpink', 'orange', 'cyan']

    for dot in range(1000):
        x = randint(-500, 500)
        y = randint(-500, 500)
        t.goto(x, y)
        size = randint(10, 75)

        if x < -167 and y > 167:
            t.dot(size, colors[0])
        elif x > 167:
            t.dot(size, colors[2])
        else:
            t.dot(size, colors[1])

    s.mainloop()

if __name__ == '__main__':
    main()

# Standard: CSPG.Y2.2.1 Construct and evaluate compound expressions using multiple relational and logical operators
# This program uses compound expressions to determine which color to use for each dot.
# For example, if the x coordinate is less than -167 and the y coordinate is greater than 167, the dot will be hotpink.

