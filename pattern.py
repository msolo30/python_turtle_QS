import turtle
t = turtle.Turtle()
t.shape(name="turtle")
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

for i in range (500):
  t.forward(i)
  t.left(2000)
