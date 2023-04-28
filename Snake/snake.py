import turtle
import time
import random

delay = 0.005
body_segments = []
score = 0
high_score = 0

wn = turtle.Screen()

#TITULO
wn.title("Snake Game")

#Windows size
wn.setup(width=600, height=600)

#background color
wn.bgcolor("DarkSlateBlue")

#head settings

#Turtle object
head = turtle.Turtle()
#para que se quede fijo
head.speed(0)
#shape
head.shape("circle")
#head color
head.color("OliveDrab4")
#no dejar rastro de animacion
head.penup()

#center
head.goto(0,0)


#food config
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red3")
food.penup()
food.goto(0,100)
food.direction = "Stop"

#score
text = turtle.Turtle()
text.color("Azure")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write(f"Score 0        High Score 0", align = "center", font=("firacode"))


#mover
head.direction="Stop"

def mov():
    if head.direction=="up":
        #almacenar el valor actual de la coordenada Y
        y = head.ycor()
        head.sety(y + 10)

    if head.direction=="down":
        y = head.ycor()
        head.sety(y - 10)

        #almacenar el valor actual de la coordenada X
    if head.direction=="left":
        y = head.xcor()
        head.setx(y - 10)

    if head.direction=="right":
        y = head.xcor()
        head.setx(y + 10)

def dirUp():
    head.direction = "up"

def dirDown():
    head.direction = "down"
def dirLeft():
    head.direction = "left"
def dirRight():
    head.direction = "right"

#conectar con el teclado
wn.listen()
turtle.onkeypress(dirUp, "Up")
turtle.onkeypress(dirDown, "Down")
turtle.onkeypress(dirRight, "Right")
turtle.onkeypress(dirLeft, "Left")

while True:
    wn.update()

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #esconder segmentos
        for segment in body_segments:
            segment.goto(1000, 1000)

        #limpiar segmentos post game
        body_segments.clear()
        score = 0
        text.clear()
        text.write(f"Score {score}        High Score {high_score}", align = "center", font=("firacode"))

    #head colision food
    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x,y)

        #newsegment config
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("OliveDrab3")
        new_segment.penup()
        body_segments.append(new_segment)

        score += 17
        if score > high_score:
            high_score = score

        text.clear()
        text.write(f"Score {score}        High Score {high_score}", align = "center", font=("firacode"))

    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x,y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x,y)

    mov()

    #colision con el propio cuerpo
    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            for segment in body_segments:
                segment.goto(1000, 1000)  

            body_segments.clear()
        
            score = 0
            text.clear()
            text.write(f"Score {score}        High Score {high_score}", align = "center", font=("firacode"))

    time.sleep(delay)




turtle.done()