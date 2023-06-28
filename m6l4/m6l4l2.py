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
play = Actor("gra", (300, 100))
cross = Actor("cross", (580, 20))
shop = Actor("sklep", (300, 200))
collection = Actor("kolekcja", (300, 300))
crocodile = Actor('crocodile', (120, 200))
hippo = Actor('hippo', (300, 200))

# Zmienne
count = 0
click = 1
mode = 'menu'
price_1 = 15
price_2 = 200
price_3 = 600

def draw():
    if mode == 'menu':
        background.draw()
        play.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        shop.draw()
        collection.draw()
   
    elif mode == 'game':    
        background.draw()
        animal.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("+1$ co 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text(price_1, center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+15$ co 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(price_2, center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("+50$ co 2s", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(price_3, center=(450, 310), color="black", fontsize = 20)
        cross.draw()
    
    elif mode == 'shop':
        background.draw()
        crocodile.draw()
        screen.draw.text("500$", center= (120, 300), color="white", fontsize = 36)
        hippo.draw()
        screen.draw.text("2500$", center= (300, 300), color="white", fontsize = 36)
        cross.draw()
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36)
        
def for_bonus_1():
    global count
    count += 1

def for_bonus_2():
    global count
    count += 5

def for_bonus_3():
    global count
    count += 15

def on_mouse_down(button, pos):
    global count
    global mode
    global price_1, price_2, price_3
    global click
    if button == mouse.LEFT and mode == 'game':
        # Kliknij na obiekt zwierzęcia
        if animal.collidepoint(pos):
            count += click
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)
        # Kliknij przycisk bonus_1  
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if count >= price_1:
                schedule_interval(for_bonus_1, 2)
                count -= price_1
                price_1 *= 2
        # Kliknij przycisk bonus_2 
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if count >= price_2:
                schedule_interval(for_bonus_2, 2)
                count -= price_2
                price_2 *= 2
        # Kliknij przycisk bonus_3 
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if count >= price_3:
                schedule_interval(for_bonus_3, 2)
                count -= price_3
                price_3 *= 2
        elif cross.collidepoint(pos):
            mode = 'menu'
    # Tryb Menu 
    elif mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'
        elif shop.collidepoint(pos):
            mode = 'shop'
    # Sklep        
    elif  mode == 'shop' and button == mouse.LEFT:
        if cross.collidepoint(pos):
            mode = 'menu'
        # Wybór krokodyla
        elif crocodile.collidepoint(pos):
            if count >= 500:
                count -= 500
                click = 2
                animal.image = 'crocodile'
        # Wybór hipopotama
        elif hippo.collidepoint(pos):
            if count >= 2500:
                count -= 2500
                click = 3
                animal.image = 'hippo'