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
data = Turtle()
figur = Turtle()
s = Screen()

# ---- Init player1 ----
p1.color("hotpink")
p1.shape("arrow")
p1.penup()
p1.speed(3)

#--figur
figur.ht()

data.ht()
data.penup()
data.speed(0)
data.color("white")

# ---- Init screen ----
s.bgcolor("black")
# --- Get koordinatsystem
win_w = s.window_width()
win_h = s.window_height()
min_x = win_w / 2 * (-1)
min_y = win_h / 2 * (-1)


# ---- Funksjoner ----
def calculate_data(x, y):
    """ Mottar variabel x og y, fra museklikk event.
    --------------------------------- Jonas ------ """
	
    x_start, y_start = p1.position()
    print(" Startposition: ", x_start, " ", y_start)
    print(" Klikkposition: ", x, " ", y)
    katet_1 = abs(y - y_start)
    print(" Katet_mot = ", katet_1)
    katet_2 = abs(x - x_start)
    print(" Katet_hos = ", katet_2)
    hypotenus = math.sqrt((x-x_start)**2 + (y-y_start)**2)
    print(" Hypotenus = ", hypotenus)
    vinkel_sinus = katet_1/hypotenus
    print(" Sinus alfa = ", vinkel_sinus)
    vinkel_rad = math.asin(vinkel_sinus)
    print(" Vinkel radianer = ", vinkel_rad)
    
    vinkel_grad = vinkel_rad * 180 / math.pi
    print(" Vinkel i grader = ", vinkel_grad)
    
    angle = 0 

    if x < x_start and y < y_start:
        angle = 180 + vinkel_grad
    elif x < x_start and y >= y_start:
        angle = 180 - vinkel_grad
    elif x > x_start and y < y_start:
        angle = 360 - vinkel_grad
    elif x > x_start and y >= y_start:
    	angle = 0 + vinkel_grad
    else: 
        print("ERROR! Something went wrong.")
    print(" Endelig vinkel er : ", angle, "\n\n")

    return angle, katet_1, katet_2, hypotenus, vinkel_sinus, vinkel_rad, vinkel_grad


def show_figur_data(a, k1, k2):
	# --- Init attributes ---
    figur.reset()
    figur.speed(0)
    figur.penup()
    figur.ht()
    figur.color("green")

    figur.setpos(p1.position())
    if 90 > a >= 0:
    	figur.pendown()
    	figur.seth(0)
    	figur.fd(k2)
    	figur.left(90)
    	figur.fd(k1)
    	figur.penup()

    elif 180 >= a >= 90:
    	figur.pendown()
    	figur.seth(180)
    	figur.fd(k2)
    	figur.right(90)
    	figur.fd(k1)
    	figur.penup()

    elif 270 > a > 180:
    	figur.pendown()
    	figur.seth(180)
    	figur.fd(k2)
    	figur.left(90)
    	figur.fd(k1)
    	figur.penup()

    elif 360 > a >= 270:
    	figur.pendown()
    	figur.seth(0)
    	figur.fd(k2)
    	figur.right(90)
    	figur.fd(k1)
    	figur.penup()

    figur.ht()

def show_list_data(a, k1, k2, h, sin , rad, grad):
	# --- Init attributes ---
	data.reset()
	data.color("white")
	data.penup()
	data.speed(0)
	data.ht()

	list_x = (min_x + (1/10*win_w))

	data.color("Yellow")
	data.setpos(list_x, min_y + (20/21*win_h))
	data.write(("Mot katet =  %.1f " % k1))
	data.setpos(list_x, min_y + (19/21*win_h))
	data.write(("Hos katet =  %.1f " % k2))
	data.setpos(list_x, min_y + (18/21*win_h))
	data.write(("Hypotenus =  %.1f" % h))
	data.color("red")
	data.setpos(list_x, min_y + (17/21*win_h))
	data.write(("Alfa sinus =  %.2f " % sin))
	data.setpos(list_x, min_y + (16/21*win_h))
	data.write(("Alfa radianer =  %.3f  pi" % rad))
	data.setpos(list_x, min_y + (15/21*win_h))
	data.write(("Alfa grader =  %.1f  grader" % grad))
	data.color("lightblue")
	data.setpos(list_x, min_y + (14/21*win_h))
	data.write(("Retningsvinkel =  %.1f  grader" % a))


def show_data(a, k1, k2, h, sin, rad, grad):
    show_figur_data(a, k1, k2)
    show_list_data(a, k1, k2, h, sin, rad, grad)


def on_right_click(x, y):
    
    a, k1, k2, h, v_sin, v_rad, v_grad = calculate_data(x, y)
    show_data(a, k1, k2, h, v_sin, v_rad, v_grad)
    
    p1.seth(a)
    p1.goto(x, y)


s.onclick(on_right_click)
s.listen()

s.mainloop()


#    Sessions:
#    15:30 - 
#    15:07 - 15:16       jonas
#    23:25 - 23:36       jonas
#    23:04 - 23:14       jonas   
