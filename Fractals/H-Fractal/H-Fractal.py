import turtle

wn = turtle.Screen()
alex = turtle.Turtle()


def line(a,b,c,d):
    alex.penup()
    alex.goto(a,b)
    alex.pendown()
    alex.goto(c,d)


def draw_H(x,y,r):
    line(x-r/2,y+r/2,x-r/2,y-r/2)
    line(x+r/2,y+r/2,x+r/2,y-r/2)
    line(x+r/2,y,x-r/2,y)

def H_Fractal(x_axis,y_axis,radius, min_length):
    draw_H(x_axis,y_axis,radius)
    if radius > min_length:
        H_Fractal(x_axis-radius/2,y_axis+radius/2,radius/2,min_length)
        H_Fractal(x_axis-radius/2,y_axis-radius/2,radius/2,min_length)
        H_Fractal(x_axis+radius/2,y_axis+radius/2,radius/2,min_length)
        H_Fractal(x_axis+radius/2,y_axis-radius/2,radius/2,min_length)

if __name__ == "__main__":
    x = int(raw_input("Enter x_axis"))
    y = int(raw_input("Enter y axis"))
    r = int(raw_input("Radius"))
    m = int(raw_input("min radius"))
    H_Fractal(x,y,r,m)  
    wn.exitonclick()
