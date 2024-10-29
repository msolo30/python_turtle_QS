import turtle
t = turtle.Turtle()
t.shape(name="turtle")
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

for i in range (500):
  t.forward(i)
  t.color(colors[i % len (colors)])
  t.left(1234567890)
