#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Kosmiczna Podróż"
FPS = 30

# Obiekty i zmienne
ship = Actor("ship", (300, 400))
space = Actor("space")
bullets = []


# Rysowanie
def draw():
    space.draw()
    ship.draw()
    for i in range(len(bullets)):
        bullets[i].draw()

# Sterowanie
def on_mouse_move(pos):
    ship.pos = pos

def update(dt):
    # Ruch pocisku
    for i in range(len(bullets)):
        if bullets[i].y < 0:
            bullets.pop(i)
            break
        else:
            bullets[i].y = bullets[i].y - 10
        
def on_mouse_down(button, pos):
    if button == mouse.LEFT:
        bullet = Actor("missiles")
        bullet.pos = ship.pos
        bullets.append(bullet)
