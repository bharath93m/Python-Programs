import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("black")
alex.speed(0)
def line(a,b,c,d):
    alex.penup()
    alex.goto(a,b)
    alex.pendown()
    alex.goto(c,d)

def draw_square(x,y,r):
    alex.begin_fill()
    line(x-r/2,y+r/2,x+r/2,y+r/2)
    line(x+r/2,y+r/2,x+r/2,y-r/2)
    line(x+r/2,y-r/2,x-r/2,y-r/2)
    line(x-r/2,y-r/2,x-r/2,y+r/2)
    alex.end_fill()

def Square_Fractal(x,y,r,min_len):
    draw_square(x,y,r)
    if r > min_len:
        Square_Fractal(x-r/2,y+r/2,r/2,min_len)
        Square_Fractal(x+r/2,y+r/2,r/2,min_len)
        Square_Fractal(x+r/2,y-r/2,r/2,min_len)
        Square_Fractal(x-r/2,y-r/2,r/2,min_len)

if __name__ == "__main__":
    x = int(raw_input("Enter x_axis"))
    y = int(raw_input("Enter y axis"))
    r = int(raw_input("length"))
    m = int(raw_input("min length"))
    Square_Fractal(x,y,r,m)  
    wn.exitonclick()
