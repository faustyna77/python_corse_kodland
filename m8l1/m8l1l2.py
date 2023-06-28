#pgzero
import random

WIDTH = 300
HEIGHT = 300

TITLE = "Przykład listy kolizji" # Tytuł okna gry
FPS = 30 # Klatki na sekundę

fon = Actor("bg")
char = Actor("spider")

# Wrogowie pojawiają się
enemies = []
count = random.randint(2, 7)
for i in range(count):
    x = random.randint(20, 280)
    y = random.randint(20, 280)
    enemy = Actor("block", (x, y))
    enemies.append(enemy)

def draw():
    fon.draw()
    char.draw()
    for i in range(len(enemies)):
        enemies[i].draw()
        
def update(dt):
    if keyboard.left:
        char.x -= 5
    elif keyboard.right:
        char.x += 5
    elif keyboard.up:
        char.y -= 5
    elif keyboard.down:
        char.y += 5

    num = char.collidelist(enemies)
    if num != -1:
        enemies.pop(num)