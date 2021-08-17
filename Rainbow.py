from turtle import *
from HSB2RGB import *
#Turtle Art 彩虹桥
def rainbow():
    hues = 0.0
    color(1,0,0)
    #绘制彩虹
    hideturtle()
    speed(100)
    pensize(3)
    penup()
    goto(-400,-300)
    pendown()
    right(110)
    for i in range(100):
        circle(1000)
        right(0.13)
        hues = hues + 1
        rgb = HSB2RGB(hues)
        color(rgb[0],rgb[1],rgb[2])
    penup()
def main():
    setup(800,600,0,0)
    bgcolor((0.8,0.8,1.0))
    #tracer(False)
    rainbow()
    #输出文字
    goto(100,-100)
    pendown()
    color("red")
    write("Rainbow", align = "center", font = ("Script MT Bold", 80, "bold"))
    #tracer(True)
    mainloop()
main()
