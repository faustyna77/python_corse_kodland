#pgzero
import random

# Okno gry
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("crack")
cell3 = Actor("bones")
size_w = 9 # Szerokość pola w komórkach
size_h = 10 # Wysokość pola w komórkach
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "Podziemia" # Tytuł okna gry
FPS = 30 # Liczba klatek na sekundę
my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]]# Wiersz siły ataku i zdrowia

# Protagonista
char = Actor('stand')
char.top = cell.height
char.left = cell.width
char.health = 100
char.attack = 5

# Generowanie wrogów
enemies = []
for i in range(5):
    x = random.randint(1, 7) * cell.width
    y = random.randint(1, 7) * cell.height
    enemy = Actor("enemy", topleft = (x, y))
    enemy.health = random.randint(10, 20)
    enemy.attack = random.randint(5, 10)
    enemy.bonus = random.randint(0, 2)
    enemies.append(enemy)

# Bonusy
hearts = []
swords = []

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 

def draw():
    screen.fill("#2f3542")
    map_draw()
    char.draw()
    screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
    screen.draw.text(char.health, center=(75, 475), color = 'white', fontsize = 20)
    screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
    screen.draw.text(char.attack, center=(425, 475), color = 'white', fontsize = 20)
    for i in range(len(enemies)):
        enemies[i].draw()
    for i in range(len(hearts)):
        hearts[i].draw()
    for i in range(len(swords)):
        swords[i].draw()
    
def on_key_down(key):
    old_x = char.x
    old_y = char.y
    if keyboard.right and char.x + cell.width < WIDTH - cell.width:
        char.x += cell.width
        char.image = 'stand'
    elif keyboard.left and char.x - cell.width > cell.width:
        char.x -= cell.width
        char.image = 'left'
    elif keyboard.down and char.y + cell.height < HEIGHT - cell.height*2:
        char.y += cell.height
    elif keyboard.up and char.y - cell.height > cell.height:
        char.y -= cell.height
    
    enemy_index = char.collidelist(enemies)
    if enemy_index != -1:
        char.x = old_x
        char.y = old_y
        enemy = enemies[enemy_index]
        enemy.health -= char.attack
        char.health -= enemy.attack
        if enemy.health <= 0:
            if enemy.bonus == 1:
                heart = Actor('heart')
                heart.pos = enemy.pos
                hearts.append(heart)
            elif enemy.bonus == 2:
                sword = Actor('sword')
                sword.pos = enemy.pos
                swords.append(sword)
            enemies.pop(enemy_index)

def update(dt):
    for i in range(len(hearts)):
        if char.colliderect(hearts[i]):
            char.health += 5
            hearts.pop(i)
            break
        
    for i in range(len(swords)):
        if char.colliderect(swords[i]):
            char.attack += 5
            swords.pop(i)
            break