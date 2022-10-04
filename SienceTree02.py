import turtle
hr = turtle.Turtle()
hr.screen.bgcolor("white")
hr.left(90)
hr.speed(150)
hr.backward(100)
hr.shape('classic')

def tree(i):
        if i < 10:
                return
        else:
                hr.forward(i)
                hr.color("purple")
                hr.circle(2)
        

                hr.color("green")
                hr.left(30)

                tree(3*i/4)

                hr.color("red")
                hr.right(60)
                tree(3*i/4)

                hr.left(30)
                hr.backward(i)
tree(100)
turtle.done()