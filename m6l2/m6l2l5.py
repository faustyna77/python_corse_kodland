#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Space Journey"
FPS = 30

# Obiekty i zmienne
ship = Actor("ship1", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
bullets = []
mode = 'menu'
type1 = Actor("ship1", (100, 200))
type2 = Actor("ship2", (300, 200))
type3 = Actor("ship3", (500, 200))

# Tworzenie listy wrogów
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)
    
# Tworzenie listy meteorów
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

# Rysowanie
def draw():
    # Okno menu Startu
    if mode == 'menu':
        space.draw()
        screen.draw.text('Wybierz statek', center = (300, 100), color = "white", fontsize = 36)
        type1.draw()
        type2.draw()
        type3.draw()
    # Tryb gry
    if mode == 'game':
        space.draw()
        planets[0].draw()
        # Rysowanie meteorów
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        # Rysowanie wrogów  
        for i in range(len(enemies)):
            enemies[i].draw()
        # Rysowanie pocisków  
        for i in range(len(bullets)):
            bullets[i].draw()
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

# Ruch planet
def planet():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

# Ruch meteorów
def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)

# Kolizja
def collisions():
    global mode
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        # Kolizja pocisków
        for j in range(len(bullets)):
            if bullets[j].colliderect(enemies[i]):
                enemies.pop(i)
                bullets.pop(j)
                new_enemy()
                break

def update(dt):
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        # Ruch pocisku
        for i in range(len(bullets)):
            if bullets[i].y < 0:
                bullets.pop(i)
                break
            else:
                bullets[i].y = bullets[i].y - 10
        
def on_mouse_down(button, pos):
    global mode, ship
    if mode == 'menu' and type1.collidepoint(pos):
        ship.image = "ship1"
        mode = 'game'
    elif mode == 'menu' and type2.collidepoint(pos):
        ship.image = "ship2"
        mode = 'game'
    elif mode == 'menu' and type3.collidepoint(pos):
        ship.image = "ship3"
        mode = 'game'
    # Strzelanie 
    elif mode == 'game' and button == mouse.LEFT:
        bullet = Actor("missiles")
        bullet.pos = ship.pos
        bullets.append(bullet)