from RiveraFunctions import *
bob.tracer(False)
turtle.bgcolor("black")
for times in range(50):
    c = (137 - times * 2, 207 - times * 2, 240 - times * 2)
    bob.color(c)
    jump(25,100)
    Rasengan()
    bob.left(800)
    bob.forward(100)

for times in range(25):
    c = (0, 104, 135)
    bob.color(c)
    jump(25,100)
    Rasengan()
    bob.left(800)
    bob.forward(100)
bob.tracer(True)




    









