import turtle

def sierpinski(turtle, order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        sierpinski(turtle, order-1, size/2)
        turtle.speed("fastest")
        turtle.forward(size/2)
        sierpinski(turtle, order-1, size/2)
        turtle.backward(size/2)
        turtle.left(60)
        turtle.forward(size/2)
        turtle.right(60)
        sierpinski(turtle, order-1, size/2)
        turtle.left(60)
        turtle.backward(size/2)
        turtle.right(60)

# Create a Turtle object
myTurtle = turtle.Turtle()

# Set the order and size of the triangle
order_of_fractal = 4
triangle_size = 200

# Draw the Sierpinski triangle
sierpinski(myTurtle, order_of_fractal, triangle_size)

# Close the Turtle graphics window when done
turtle.done()
