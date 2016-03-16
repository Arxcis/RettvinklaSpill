"""
    Tittel: Et enkelt Turtle spill, samarbeid over GIT

    Opprettet: kl: 23:03 - 09.03.2015 av jonas
    Samarbeidspartner: jan cato
        Beskrivelse:
        Dette spillet blir laget for å demonstrere/øve på
        hvordan det er å samarbeide over git.

"""

# ---- Importer nødvendige bibliotek ----
from turtle import *
import math

# ---- Init objekter ----
p1 = Turtle()
s = Screen()

# ---- Init player1 ----
p1.color("hotpink")
p1.shape("arrow")
p1.penup()
p1.speed(3)

# ---- Init screen ----
s.bgcolor("lightblue")

# ---- Funksjoner ----
def on_right_click(x, y):
	angle = p1.towards(x, y)
	p1.seth(angle)
	p1.goto(x, y)

s.onclick(on_right_click)
s.listen()

s.mainloop()


#    Sessions:
#    15:07 - 15:16       jonas
#    23:25 - 23:36       jonas
#    23:04 - 23:14       jonas   
