from turtle import Turtle

def tree(plist, l, a, f):
    '''
    plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor y which branch is shortened
    '''
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)#沿着当前的方向画画
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l*f, a, f)

def maketree(x,y):
    p = Turtle()
    p.color("green")
    p.pensize(5)
    #p.setundobuffer(None)
    p.hideturtle()
    #p.speed(10)
    p.getscreen().tracer(30,0)
    p.left(90)
    p.penup()
    p.goto(x,y)
    p.pendown()
    #t = tree([p], 200, 65, 0.6375)
    t = tree([p], 110, 65, 0.6375)
    print(len(p.getscreen().turtles()))
    
def main():
    maketree(-200,-200)
    maketree(0,0)
    maketree(200,-200)
main()

'''
def main():
    p = Turtle()
    p.color("green")
    p.pensize(5)
    #p.setundobuffer(None)
    p.hideturtle()
    #p.speed(10)
    p.getscreen().tracer(30,0)
    p.left(90)
    p.penup()
    p.goto(0,0)
    p.pendown()
    #t = tree([p], 200, 65, 0.6375)
    t = tree([p], 110, 65, 0.6375)
main()
'''