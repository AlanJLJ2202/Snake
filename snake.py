
import turtle
import time
import random

posponer = 0.1

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego de Alan")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#txtCorreoCabeza serpiente
comida = turtle.Turtle()
comida.speed(100)
comida.shape("triangle")
comida.color("red")
comida.penup()
comida.goto(0,100)


#Comida

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"


#Funciones

def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def izquierda():
	cabeza.direction = "right"
def derecha():
	cabeza.direction = "left"



def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)	
	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)	
	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)	

#Teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Left")
wn.onkeypress(izquierda, "Right")



while True:
	wn.update()
	mov()
	if comida.distance(cabeza) < 20:
			x = random.randint(-280,280)
			y = random.randint(-280,280)
			comida.goto(x,y)
			cabeza.color("Yellow")	
			
	else:
			cabeza.color("Blue")		
    
	time.sleep(posponer)