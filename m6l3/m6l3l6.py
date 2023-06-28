#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Klikanie zwierząt"
FPS = 30

# Obiekty
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
play = Actor("play", (300, 100))

# Zmienne
count = 0
click = 1
mode = 'menu'

def draw():
    if mode == 'menu':
        background.draw()
        play.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
   
    elif mode == 'game':    
        background.draw()
        animal.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("+1$ co 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text("cena: 15$", center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+15$ co 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text("cena: 200$", center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("+50$ co 2s", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text("cena: 600$", center=(450, 310), color="black", fontsize = 20)

def for_bonus_1():
    global count
    count += 1

def for_bonus_2():
    global count
    count += 15

def for_bonus_3():
    global count
    count += 50

def on_mouse_down(button, pos):
    global count
    global mode
    # Tryb gry
    if button == mouse.LEFT and mode == 'game':
        # Kliknij przycisk ze zwierzęciem
        if animal.collidepoint(pos):
            count += click
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)
        # Kliknij przycisk bonus_1  
        elif bonus_1.collidepoint(pos):
            if count >= 15:
                schedule_interval(for_bonus_1, 2)
                count -= 15
        # Kliknij przycisk bonus_2 
        elif bonus_2.collidepoint(pos):
            if count >= 200:
                schedule_interval(for_bonus_2, 2)
                count -= 200
        # Kliknij przycisk bonus_3 
        elif bonus_3.collidepoint(pos):
            if count >= 600:
                schedule_interval(for_bonus_3, 2)
                count -= 600
    # Tryb menu
    elif mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'