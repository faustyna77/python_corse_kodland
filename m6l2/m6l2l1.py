#pgzero

WIDTH = 300 # Szerokość okna
HEIGHT = 300 # Wysokość okna

TITLE = "Clicker" # Tytuł okna gry
FPS = 30 # Klatki na sekundę
count = 0

def draw():
    screen.fill((32, 191, 107))
    screen.draw.text(count, center=(150, 150), color="white", fontsize = 96)
    
def on_mouse_down(button, pos):
    global count
    if button == mouse.LEFT:
        count = count + 1
      
