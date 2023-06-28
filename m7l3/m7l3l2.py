#pgzero

WIDTH = 600 # Szerokość okna
HEIGHT = 300 # Wysokość okna

TITLE = "Tytuł twojej gry" # Tytuł okna gry
FPS = 30 # Liczba klatek na sekundę

# Obiekty
char = Actor('giraffe', (300, 150))
background = Actor("background")

def draw():
    background.draw()
    char.draw()