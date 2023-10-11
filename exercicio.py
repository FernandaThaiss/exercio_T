#Exercicio 1
"""import turtle

turtle = turtle.Turtle() 
turtle.shape('turtle')

turtle.forward(200)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(400)

#Exercicio 2
import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')
turtle.color('blue')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

#Exercicio 3
import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')
turtle.pensize(7)

for color in ['blue', 'black', 'red', 'pink']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.forward(200)
turtle.pendown()   


for color in ['blue', 'black', 'red', 'pink']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

#Exercicio 4
import turtle
import random

turtle = turtle.Turtle()
colors = ['purple', 'blue','black','pink']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.pensize(7)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(120)

#Exercicio 5

import turtle
import random

turtle = turtle.Turtle()
colors = ['purple', 'blue','black','pink','green','red','brown']
 
for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.shape("square")
    turtle.forward(200)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
  color = random.choice(colors)
  turtle.color(color)
  turtle.shape("turtle")
  turtle.forward(200)
  turtle.right(90)

#Exercício 6
import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in [1, 2, 3]:
    turtle.forward(100)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
  turtle.forward(100)
  turtle.right(90)

#Exercício 7

import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(200)

turtle.backward(100)
turtle.backward(200)
turtle.right(90)

for _ in range(3):
  turtle.forward(200)
  turtle.left(90)

#Exercício 8

import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(7)

colors = ['purple', 'blue', 'yellow', 'green', 'pink','brown','red']
for _ in range (12):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(30)"""

#Exercício 9
import turtle
import random

turtle = turtle.Turtle()

colors = ['purple','blue','black','green','orange','red','pink']
for c in range(720):
  color = random.choice(colors)
  turtle.color(color)
  turtle.forward(2)
  turtle.right(1)


#Exercício 10
"""import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.color('green')
    turtle.forward(100)
    turtle.right(90)
  
turtle.penup() 
turtle.backward(50)
turtle.left(90)
turtle.pendown() 

for _ in range(4):
   turtle.color('blue')
   turtle.shape('turtle')
   turtle.left(90)
   turtle.forward(100)

turtle.penup()
turtle.forward(50)
turtle.pendown()

for _ in range(4):
   turtle.color('pink')
   turtle.shape('square')
   turtle.forward(100)
   turtle.left(90)

turtle.penup()
turtle.left(90)
turtle.backward(50)
turtle.pendown()

for _ in range(4):
   turtle.color('orange')
   turtle.shape('circle')
   turtle.right(90)
   turtle.forward(100)
  
turtle.penup()
turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.pendown()

for _ in range(2):
  turtle.color('blue')
  turtle.right(90)
  turtle.backward(250)
  turtle.right(90)
  turtle.forward(250)"""