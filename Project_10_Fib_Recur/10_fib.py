from turtle import Turtle, Screen

def main():
    t = Turtle()
    colors = ["red", "orange", "yellow", "green", "blue", "darkblue", "purple"]
    t.speed(0)
    t.left(90)

    for i in range(1, 17):
        num = fib(i)
        t.color(colors[i % len(colors)])

        t.begin_fill()
        for j in range(6):
            t.forward(num)
            t.right(90)
        t.left(90)
        t.end_fill()


def fib(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

if __name__ == "__main__":
    main()
