# Author: Su
import turtle as t

color = ['red','pink','green']
ra = [20, 50, 100]
for i in range(3):
    t.pu()
    t.goto(0,-ra[i])
    t.pd()
    t.pencolor(color[i])
    t.circle(ra[i])
t.done()
