import turtle
from PIL import Image, ImageDraw, ImageFont

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title(" Para mandar para a pessoa amada")

heart = turtle.Turtle()
heart.color("red")
heart.fillcolor("red")
heart.begin_fill()

heart.left(140)
heart.forward(224)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range (200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end.fill()

heart.hideturtle()

ts = turtle.getcanvas()
ts.postscript(file="heart.ps")

turtle.bye()

img = Image.open("heart.ps")
img.save("heart.png")

def add_flowers(image_path):
    img =Image.open(image_path)
    
    flower = Image.open("coração/flower.png.png")

    flower_positions = [(100, 450), (200, 450), (300, 450), (400,450)]
    for pos in flower_positions:
        img.paste(flower, pos, flower)
    img.save("heart_with_flowers.png")
add_flowers("heart.png")

print("Imagem criada com sucesso: heart_with_flower.png")