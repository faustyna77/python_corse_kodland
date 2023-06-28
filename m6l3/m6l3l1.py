#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Klikanie zwierząt"
FPS = 30

# Obiekty
animal = Actor("giraffe", (150, 250))
background = Actor("background")

# Zmienne
count = 0

def draw():
    background.draw()
    animal.draw()
    screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)