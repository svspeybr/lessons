import pygame
from pygame.locals import *

# set up color names:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# variable for game loop:
CONTINUE = True

# set up pygame
pygame.init()

# set up the window
window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

# background color:
window.fill(WHITE)

# Oefening 1:
#pygame.draw.circle(window, BLACK, (250, 200), 10, 0)
#for i in range(5):
#    pygame.draw.circle(window, BLACK, (250, 200), 10 + 20 * i, 10)


# Oefening 2: Volgende code probeert op een andere manier de bull's eye te tekenen.
# Leg uit hoe de code werkt en waarom ze foutief is.
color = WHITE
for i in range(10):
    pygame.draw.circle(window, color, (250, 200), 10 * i, 0)
    if color == BLACK:
        color = WHITE
    else:
        color = BLACK

# Oefening 3: Pas de code uit oefening 2 aan zodat ze wel het gewenste resultaat geeft.
color = WHITE
#for i in range(10):
#    pygame.draw.circle(window, color, (250, 200), 100 - 10 * i, 0)
#    if color == BLACK:
#        color = WHITE
#    else:
#        color = BLACK

# Oefening 4: Teken een schaakbord

for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0:
            pygame.draw.rect(window, BLACK, (10 * x, 10 * y, 10, 10), 0)

# game loop:
while CONTINUE:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            CONTINUE = False
            pygame.quit()
