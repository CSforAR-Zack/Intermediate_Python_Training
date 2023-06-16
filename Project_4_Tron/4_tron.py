from turtle import Turtle, Screen

# Global scope
t = Turtle()
s = Screen()

def main():
    t.color('cyan')
    s.bgcolor('black')
    t.speed(1)

    # Event-driven programming paradigm
    s.onkey(turn_left, 'Left')
    s.onkey(turn_right, 'Right')
    s.onkey(center, 'space')
    s.listen()

    while True:
        t.forward(1)

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

def center():
    t.goto((0,0))

if __name__ == '__main__':
    main()