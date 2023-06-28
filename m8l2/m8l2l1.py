#pgzero
import random

WIDTH = 300
HEIGHT = 300

TITLE = "Poziomy" #Tytuł okna gry
FPS = 30 # Klatki na sekundę

fon = Actor("bg", (150,150))
char = Actor("ghost")

count = 0 # Wynik
bonus = 1 # Wartość, o którą zwiększa się wynik
level = 1 # Poziom
speed = 5 # Prędkość głównego bohatera
mode = "game"

# Odradzanie się wrogów
enemies = []
def new_enemy():
    global mode
    char.pos = (30, 40)
    en = random.randint(2, 7)
    if level == 1:
        for i in range(en):
            x = random.randint(20, 280)
            y = random.randint(20, 280)
            enemy = Actor("green", (x, y))
            enemies.append(enemy)
    elif level == 2:
        fon.image = "bg1"
        for i in range(en):
            x = random.randint(20, 280)
            y = random.randint(20, 280)
            enemy = Actor("yellow", (x, y))
            enemies.append(enemy)
    elif level == 3:
        fon.image = "bg2"
        for i in range(en):
            x = random.randint(20, 280)
            y = random.randint(20, 280)
            enemy = Actor("red", (x, y))
            enemies.append(enemy)
    elif level == 4:
        fon.image = "bg3"
        for i in range(en):
            x = random.randint(20, 280)
            y = random.randint(20, 280)
            enemy = Actor("blue", (x, y))
            enemies.append(enemy)
new_enemy()

def draw():
    if mode == "game":
        fon.draw()
        char.draw()
        screen.draw.text(count, (10, 10), color = 'white', fontsize = 20)
        screen.draw.text(level, (280, 10), color = 'white', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
    elif mode == "pause":
        fon.draw()
        screen.draw.text("Wygrana!", center=(150, 100), color = 'white', fontsize = 42)
        screen.draw.text("Przenieś się na poziom:", center=(150, 150), color = 'white', fontsize = 24)
        screen.draw.text(level, center=(150, 180), color = 'white', fontsize = 36)
        screen.draw.text("Naciśnij spację", center=(150, 220), color = 'black', fontsize = 24)
    elif mode == "end":
        fon.draw()
        screen.draw.text(count, center=(150, 150), color = 'white', fontsize = 46)
        
def update(dt):
    global count, level, bonus, mode, speed
    if keyboard.left:
        char.x -= speed
    elif keyboard.right:
        char.x += speed
    elif keyboard.up:
        char.y -= speed
    elif keyboard.down:
        char.y += speed
    
    num = char.collidelist(enemies)
    if num != -1:
        enemies.pop(num)
        count += bonus
    # Zmiana poziomu   
    if mode != 'pause' and enemies == []:
        level += 1 # Przejście na wyższy poziom
        bonus += 1 # Gracz zdobędzie więcej punktów
        speed += 2 # Szybkość zmian postaci
        new_enemy()
        mode = "pause"
    if level == 5:
        mode = "end" # Jak tylko poziomy się skończą, gra się zatrzymuje
    if mode == "pause" and keyboard.space:
        mode = "game"
        