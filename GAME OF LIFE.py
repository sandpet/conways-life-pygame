import pygame as pg
clock = pg.time.Clock()
from random import randint
start_mesh = [[randint(0,1) for x in range(101)] for x in range(101)]

VINDU_BREDDE = 1000
VINDU_HOYDE = 1000


pg.init()
 
# Initializing surface
surface = pg.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))
 


def display_grid(mesh):
    for y in range(len(mesh)):
        for x in range(len(mesh[0])):
            if mesh[x][y] == 1:
                xstart = x*VINDU_BREDDE/len(mesh[0])
                x_len = VINDU_BREDDE/len(mesh[0])
                ystart = y*VINDU_HOYDE/len(mesh)
                y_len =  VINDU_HOYDE/len(mesh)
                pg.draw.rect(surface, (255,255,255), pg.Rect(ystart, xstart, x_len, y_len))

def update_grid(mesh):
    new_grid = []
    for row in range(len(mesh)):
        hold = []
        for col in range(len(mesh[0])):
            num_cells  =0
            for x in range(-1, 2, 1):
                for y in range(-1, 2, 1):
                    try:
                        if mesh[row + x][col + y] == 1:
                            if x != 0 or y != 0:
                                num_cells += 1
                    except IndexError:
                        continue
            if mesh[row][col] == 1:
                if num_cells < 2:
                    hold.append(0)
                elif num_cells == 2 or num_cells == 3:
                    hold.append(1)
                else:
                    hold.append(0)
            else:
                if num_cells == 3:
                    hold.append(1)
                else:
                    hold.append(0)
        new_grid.append(hold)
    return new_grid
            
# Drawing Rectangle

fortsett = True
while fortsett:
    #reset vindu
    surface.fill((0, 0, 0))

    display_grid(start_mesh)
    start_mesh = update_grid(start_mesh)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
         # Oppdaterer alt innholdet i vinduet
    pg.display.flip()
    clock.tick(10)



