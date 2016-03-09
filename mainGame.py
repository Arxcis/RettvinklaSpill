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

# ---- Init objekter ----
player1 = Turtle()
screen = Screen()

# ---- Init player1 ----
player1.color("hotpink")
player1.shape("arrow")
player1.penup()

# ---- Init screen ----
screen.setup(600, 600)              # Størrelsen på vinduet
screen.screensize(550, 550)         # Størrelsen på "spillskjermen"
screen.bgcolor("lightblue")

# ----------------- MAIN ------------------------

screen.mainloop()


"""
    session  23:04 - 23:14       jonas
"""