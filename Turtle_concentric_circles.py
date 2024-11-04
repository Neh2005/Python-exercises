import turtle
# Set up the turtle
turtle.speed(0)
def drawCircle(x, y, r):
    # Draws a circle with radius r and center (x, y)
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)
    if r > 10:  # Recursive base case
        drawCircle(x+r, y, r/2)
        drawCircle(x-r, y, r/2)
        drawCircle(x, y+r, r/2)
        drawCircle(x, y-r, r/2) 
       
# Call the function to draw concentric circles
drawCircle(0, 0, 200)  # Example: Center at (0, 0) with radius 200
# Keep the window open until manually closed
turtle.done()
