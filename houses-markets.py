import turtle
import random
import math
from math import hypot
from random import randint
sc=turtle.Screen()
t = turtle.Turtle()
t.speed(0)

#houses a is red , house b is green and not random; 2 houses
#markets are blue and random ; 4 markets
#house a
t.penup()
t.setposition(160,260)
t.pendown()
t.pencolor("red")
for i in range(4):
  t.forward(20)
  t.left(90)

#house b
t.penup()
t.setposition(-100,-160)
t.pendown()
t.pencolor("green")
for i in range(4):
  t.forward(20)
  t.left(90)


t.penup()
t.pencolor("blue")
x= random.randint(-300,300)
y= random.randint(-300,300)
t.setposition(x,y)
t.pendown()
for i in range(2):
  t.forward(20)
  t.left(90)
  t.forward(40)
  t.left(90)
dist = math.sqrt( (x - 160)**2 + (y - 260)**2 )
dist_2 = math.sqrt( (x + 100)**2 + (y + 160)**2 )
print("a", dist)
print("b", dist_2)
#-----------------------------------------------------------
t.penup()
t.pencolor("blue")
x= random.randint(-300,300)
y= random.randint(-300,300)
t.setposition(x,y)
t.pendown()
for i in range(2):
  t.forward(20)
  t.left(90)
  t.forward(40)
  t.left(90)
d_1 = math.sqrt( (x - 160)**2 + (y - 260)**2 )
d_2 = math.sqrt( (x + 100)**2 + (y + 160)**2 )
print("a", d_1)
print("b", d_2)
#-----------------------------------------------------------

t.penup()
t.pencolor("blue")
x= random.randint(-300,300)
y= random.randint(-300,300)
t.setposition(x,y)
t.pendown()
for i in range(2):
  t.forward(20)
  t.left(90)
  t.forward(40)
  t.left(90)
d_3 = math.sqrt( (x - 160)**2 + (y - 260)**2 )
d_4 = math.sqrt( (x + 100)**2 + (y + 160)**2 )
print("a", d_3)
print("b", d_4)
#-----------------------------------------------------------

t.penup()
t.pencolor("blue")
x= random.randint(-300,300)
y= random.randint(-300,300)
t.setposition(x,y)
t.pendown()
for i in range(2):
  t.forward(20)
  t.left(90)
  t.forward(40)
  t.left(90)
d_5 = math.sqrt( (x - 160)**2 + (y - 260)**2 )
d_6 = math.sqrt( (x + 100)**2 + (y + 160)**2 )
print("a", d_5)
print("b", d_6)

c=[]
d=[]
#c is market' distance from house a
#b is market' distance from house b
c.extend(( dist , d_1 ,  d_3 , d_5))
c.sort()
print(c)

d.extend(( dist_2 , d_2 , d_4 , d_6))
d.sort()
print(d)

if c[0]>d[0]:
  print("you should buy house b")
  print("the distance between house and closest market is:" , int(d[0]))

elif c[0]<=d[0]:
  print("you should buy house a")
  print("the distance between house and closest market is:" , int(c[0]))

else:
  print("you can buy one of them because the distances are same.")

sc.exitonclick()
