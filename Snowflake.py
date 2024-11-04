import turtle

def koch(x, m):
    if x < m:
        turtle.forward(x)
    else:
        koch(x / 3, m)
        turtle.left(60)
        koch(x / 3, m)
        turtle.right(120)
        koch(x / 3, m)
        turtle.left(60)
        koch(x / 3, m)

def koch_snowflake(x, m):
    for _ in range(3):
        koch(x, m)
        turtle.right(120)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed("fastest")
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    colors = ["purple", "blue", "green", "yellow"]
    koch_snowflake(500, 50)

    turtle.done()

if __name__ == "__main__":
    main()
