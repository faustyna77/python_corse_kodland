#pgzero
import random

WIDTH = 300
HEIGHT = 300

TITLE = "Wrogowie odradzają się" # Tytuł okna gry
FPS = 30 # Klatki na sekundę

fon = Actor("bg")

# Wrogowie odradzają się
enemies = []
count = random.randint(2, 7)
for i in range(count):
    x = random.randint(20, 280)
    y = random.randint(20, 280)
    enemy = Actor("block", (x, y))
    enemies.append(enemy)

def draw():
    fon.draw()
    for i in range(len(enemies)):
        enemies[i].draw()