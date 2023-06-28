#pgzero

WIDTH = 300 # Szerokość okna
HEIGHT = 300 # Wysokość okna

TITLE = "Wynik" # Tytuł okna gry
FPS = 30 # Klatki na sekundę
count = 0

def draw():
    screen.fill("#a29bfe")
    screen.draw.text(count, center=(150, 150), color="white", fontsize = 96)
    
def on_mouse_down(button, pos):
    global count
    if button == mouse.LEFT:
        count = count + 1
      
