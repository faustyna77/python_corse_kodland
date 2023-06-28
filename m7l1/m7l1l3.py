#pgzero

# Okno gry wykonane z komórek
cell = Actor('border')
size_w = 7 # Szerokość pola w komórkach
size_h = 7 # # Wysokość pola w komórkach
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "Podziemia" # Tytuł okna gry
FPS = 30 # Liczba klatek na sekundę
my_map = [[0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 2, 1, 3, 1, 0], 
          [0, 1, 1, 2, 1, 1, 0], 
          [0, 3, 2, 1, 1, 3, 0], 
          [0, 1, 1, 1, 3, 1, 0], 
          [0, 1, 3, 1, 1, 2, 0], 
          [0, 0, 0, 0, 0, 0, 0]]

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            cell.left = cell.width*j
            cell.top = cell.height*i
            cell.draw()

def draw():
    map_draw()
    



