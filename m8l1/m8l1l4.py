#pgzero
import random

WIDTH = 300
HEIGHT = 300

TITLE = "Menu" # Tytuł okna gry
FPS = 30 # Klatki na sekundę

fon = Actor("fon")
char = Actor("ghost")
mode = 'menu'
gra = Actor("gra", (150, 150))

# Odradzanie się wrogów
enemies = []
count = random.randint(2, 7)
for i in range(count):
    x = random.randint(20, 280)
    y = random.randint(20, 280)
    enemy = Actor("red", (x, y))
    enemies.append(enemy)

def draw():
    fon.draw()
    if mode == 'menu':
        gra.draw()

    elif mode == 'game':
        char.draw()
        for i in range(len(enemies)):
            enemies[i].draw()
        
def update(dt):
    if mode == 'game':
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
            
def on_mouse_down(button, pos):
    global mode
    if mode == 'menu':
        if gra.collidepoint(pos):
            mode = 'game'
            