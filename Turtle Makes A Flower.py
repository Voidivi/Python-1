import turtle
import random

colors = ['#fce7e6', '#f6c492', '#fabab5', '#b5d0d4', '#a2c794' ]

def petal(t, r, angle):
  for i in range(2):
    t.circle(r,angle)
    t.left(180-angle)

def flower(t, n, r, angle):
  for i in range(n):
    petal(t,r,angle)
    t.left(360.0/n)
    
def draw(t, length):
  window = turtle.Screen()
  window.bgcolor('gray')
  t.pu()
  t.fd(length)
  t.pd()
  
def main():
  yertle = turtle.Turtle()
  yertle.color(random.choice(colors))
  yertle.shape('turtle')
  yertle.speed(5)
  draw(yertle,0)
  yertle.begin_fill()
  flower(yertle, 7, 60.0, 60.0)
  yertle.end_fill()

if __name__ == "__main__":
	main()