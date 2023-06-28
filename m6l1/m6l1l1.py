#pgzero

WIDTH = 600
HEIGHT = 450

TITLE = "Kosmiczna podróż"
FPS = 30

# Obiekty i zmienne
ship = Actor("ship", (300, 400))
space = Actor("space")

# Rysowanie
def draw():
    space.draw()
    ship.draw()