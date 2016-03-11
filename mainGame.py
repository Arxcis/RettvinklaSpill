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
screen.bgcolor("lightblue")


# ---- Funksjoner ----
def move_left():
    player1.lt(30)


def move_right():
    player1.rt(30)


# ---- Main ----
def main_game():
    # ---- Variabler ----
    death = False
    victory = False

    # ---- Keybinds ----
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.listen()

    # ---- While loop ----
    while death is False or victory is False:
        player1.forward(2)

    # ---- While loop slutt ----


main_game()
screen.mainloop()


#    Sessions:
#
#    23:25 - 23:36       jonas
#    23:04 - 23:14       jonas   
