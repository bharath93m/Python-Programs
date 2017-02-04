import turtle

alex = turtle.Turtle()
wn = turtle.Screen()
alex.speed(0)
def circle_fractal(x_axis,y_axis,radius,min_radius):
    alex.penup()
    alex.goto(x_axis,y_axis-radius)
    alex.pendown()
    alex.circle(radius)
    if radius > min_radius :
        circle_fractal(x_axis+radius,y_axis,radius/2,min_radius)
        circle_fractal(x_axis,y_axis+radius,radius/2,min_radius)
        circle_fractal(x_axis,-y_axis-radius,radius/2,min_radius)
        circle_fractal(-x_axis-radius,y_axis,radius/2,min_radius)

if __name__ == "__main__":
    x = int(raw_input("Enter x_axis"))
    y = int(raw_input("Enter y axis"))
    r = int(raw_input("Radius"))
    m = int(raw_input("min radius"))
    circle_fractal(x,y,r,m)
    input()
        
