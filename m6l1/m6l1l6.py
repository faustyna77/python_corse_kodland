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
mode = 'game'

# Tworzenie listy wrogów
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Rysowanie
def draw():
    # Tryb gry
    if mode == 'game':
        space.draw()
        ship.draw()
        # Rysowanie wrogów
        for i in range(len(enemies)):
            enemies[i].draw()
    # Okno Game over     
    elif mode == 'end':
        space.draw()
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36)
    
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
    global mode
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'

def update(dt):
    if mode == 'game':
        enemy_ship()
        collisions()