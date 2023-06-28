#pgzero

WIDTH = 600 # Szerokość okna
HEIGHT = 300 # Wysokość okna

TITLE = "Tytuł twojej gry" # Tytuł okna gry
FPS = 30 # Liczba klatek na sekundę

# Obiekty
char = Actor('stand', (50, 240))
background = Actor("background")
enemy = Actor('yellow', (250, 270))

def draw():
    background.draw()
    char.draw()
    enemy.draw()
    
def update(dt):
    # Poruszenie się wrogów
    if enemy.x > -20:
        enemy.x = enemy.x - 10
        enemy.angle = enemy.angle + 10
    else:
        enemy.x = WIDTH + 20
        
    # Sterowanie
    if keyboard.left and char.x > 20:
        char.x = char.x - 5
        char.image = 'left'
    elif keyboard.right and char.x < 280:
        char.x = char.x + 5
        char.image = 'right'
    else:
        char.image = 'stand'
        
    # Skok
    if keyboard.space:
        char.y = 180
        animate(char, tween = "bounce_end", duration=0.5, y = 240)