import turtle as t

# Configuraciones iniciales
t.speed(15)
t.width(5)
t.bgcolor("white")

# Función para dibujar un círculo
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Función para dibujar una línea curva (para la sonrisa)
def draw_curve(x, y, radius, heading):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.setheading(heading)
    t.circle(radius, 180)

# Dibujar cara
draw_circle("yellow", 100, 0, 0)

# Dibujar ojos
draw_circle("black", 15, -35, 50)
draw_circle("black", 15, 35, 50)

# Dibujar boca (sonrisa)
t.left(90)
draw_curve(0, -25, 60, -50)

# Ocultar la tortuga al final
t.hideturtle()

# Mantener la ventana abierta
t.done()
