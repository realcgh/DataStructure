def draw_square(s,d,u):
    import turtle
    

    
    scr=turtle.Screen()
    t=turtle.Turtle()
    for j in range(0,u):
        for i in range(4):
          t.forward(s)
          t.right(90)
        t.up()
        t.forward(s+u)
        t.down()
    turtle.done() 

    
    
s=input("Please enter the side length of your square:")
d=input("Please enter the distance between the squares:")
u=input("Please enter the number of squares you need:")
draw_square(int(s),int(d),int(u))
