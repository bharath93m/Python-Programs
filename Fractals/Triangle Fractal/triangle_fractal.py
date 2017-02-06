import turtle
import math

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("black")
alex.speed(0)

def draw_triangle(a,b,c,d,e,f):
    line(a,b,c,d)
    line(c,d,e,f)
    line(e,f,a,b)
    
def line(a,b,c,d):
    alex.penup()
    alex.goto(a,b)
    alex.pendown()
    alex.goto(c,d)

def tri_Fractal(a,b,c,d,e,f,r,minimum):
    draw_triangle((a+c)/2,(b+d)/2,(c+e)/2,(d+f)/2,(e+a)/2,(f+b)/2)
    if r > minimum:
        tri_Fractal(a,b,(a+c)/2,(b+d)/2,(e+a)/2,(f+b)/2,r/2,minimum)
        tri_Fractal((a+c)/2,(b+d)/2,c,d,(c+e)/2,(d+f)/2,r/2,minimum)
        tri_Fractal((e+a)/2,(f+b)/2,(c+e)/2,(d+f)/2,e,f,r/2,minimum)
if __name__ == "__main__":
    x = int(raw_input("Enter x_axis"))
    y = int(raw_input("Enter y axis"))
    r = int(raw_input("length"))
    m = int(raw_input("min length"))
    draw_triangle(x,y+(r/1.732),x-(r/2),y-(r/(2*1.732)),x+(r/2),y-(r/(2*1.732)))
    tri_Fractal(x,y+(r/1.732),x-(r/2),y-(r/(2*1.732)),x+(r/2),y-(r/(2*1.732)),r,m)  
    wn.exitonclick()    
