#pgzero
import random

WIDTH = 300
HEIGHT = 300

TITLE = "Uruchom ponownie" # Tytuł okna gry
FPS = 30 # Klatki na sekundę

fon = Actor("bg")
char = Actor("spider")
mode = 'game'

# Odradzanie się wrogów
enemies = []
def en():
    count = random.randint(1, 3)
    for i in range(count):
        x = random.randint(20, 280)
        y = random.randint(20, 280)
        enemy = Actor("block", (x, y))
        enemies.append(enemy)
en()

def draw():
    fon.draw()
    if mode == "game":
        char.draw()
        for i in range(len(enemies)):
            enemies[i].draw()
    if mode == "end":
        screen.draw.text("GAME OVER", center=(150, 150), color = 'white', fontsize = 26)
        
def update(dt):
    global mode, enemies
    if mode == "game":
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
            mode = 'end'
    if mode == "end" and keyboard.space:
        enemies = []
        en()
        char.pos = (40, 20)
        mode = 'game'