#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Kosmiczna podróż"
FPS = 30

# Obiekty i zmienne
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []

# Dodawanie meteorów do listy
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Rysowanie
def draw():
    space.draw()
    ship.draw()
    # Rysowanie wrogów
    for i in range(len(enemies)):
        enemies[i].draw()
    
# Sterowanie
def on_mouse_move(pos):
    ship.pos = pos

# Dodawanie nowych wrogów do listy
def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Ruch wrogów
def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

# Kolizja
def collisions():
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            exit()

def update(dt):
    enemy_ship()
    collisions()