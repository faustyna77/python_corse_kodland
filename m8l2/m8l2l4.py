#pgzero
import random

WIDTH = 300
HEIGHT = 300

TITLE = "Poziomy" # Tytuł okna gry
FPS = 30 # Klatki na sekundę

fon = Actor("bg1", (150,150))
char = Actor("snail")
# Skórki
snail = Actor("snail", (50, 150))
snake = Actor("snake", (150, 150))
mouse = Actor("mouse", (250, 150))
# Przyciski
play = Actor("play", (150, 100))
settings = Actor("settings", (150, 200))
cross = Actor("cross", (280, 20))

mode = "menu"
speed = 2 # Prędkość głównego bohatera

def draw():
    fon.draw()
    if mode == "menu":
        play.draw()
        screen.draw.text("Gra", center =(150, 95), color = 'white', fontsize = 24)
        settings.draw()
        screen.draw.text("Poziomy", center =(150, 195), color = 'white', fontsize = 24)
    elif mode == "settings":
        snail.draw()
        snake.draw()
        mouse.draw()
        cross.draw()
    elif mode == "game":
        char.draw()
        cross.draw()

def update(dt):
    if mode == "game":
        if keyboard.left:
            char.x -= speed
        elif keyboard.right:
            char.x += speed
        elif keyboard.up:
            char.y -= speed
        elif keyboard.down:
            char.y += speed
        
def on_mouse_down(button, pos):
    global mode, speed
    if mode == "menu":
        if play.collidepoint(pos):
            mode = "game"
        elif settings.collidepoint(pos):
            mode = "settings"
    # Ustawienia
    elif mode == "settings":
        if snail.collidepoint(pos): # Snail skin is selected
            char.image = "snail"
            snail.y = 130
            animate(snail, tween='bounce_end', duration=0.5, y = 150)
            speed = 2
            
        elif snake.collidepoint(pos): # Snake skin is selected
            char.image = "snake"
            snake.y = 130
            animate(snake, tween='bounce_end', duration=0.5, y = 150)
            speed = 4
            
        elif mouse.collidepoint(pos): # Mouse skin is selected
            char.image = "mouse"
            mouse.y = 130
            animate(mouse, tween='bounce_end', duration=0.5, y = 150)
            speed = 6
            
        elif cross.collidepoint(pos):
            mode = "menu"
            
    elif mode == "game":
        if cross.collidepoint(pos):
            mode = "menu"