def draw_star(l):
    import turtle
    

    
    scr=turtle.Screen()
    t=turtle.Turtle()
    for i in range(5):
        t.forward(l)
        t.right(144)
    turtle.done()
    
    
l=input("Please enter the side length of your star:")
draw_star(int(l))
