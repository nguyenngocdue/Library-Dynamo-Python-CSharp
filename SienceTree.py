import turtle
hr = turtle.Turtle()
hr.left(90)
hr.speed(150)

def tree(i):
        if i < 10:
                return
        else:
                hr.forward(i)
                hr.left(30)
                hr.color("green")
                tree(3*i/4)
                hr.right(60)
                tree(3*i/4)
                hr.left(30)
                hr.backward(i)
tree(100)
turtle.done()


quocan.architecture@gmail.com
engr.datnt97@gmai.com
ngdoanhoa@gmail.com
tranhoaivuut@gmail.com
danhnhanhuynh1@gmail.com
haulph99.xd@gmail.com
nguyendung10198@gmail.com
