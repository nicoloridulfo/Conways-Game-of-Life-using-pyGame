import pygame as pg
import numpy as np
import time

class Life:
    """
    The game of life
    """
    def __init__(self, ROWS, COLUMNS):
        self.ROWS = ROWS
        self.COLUMNS = COLUMNS
        self.grid = np.zeros((self.COLUMNS, self.ROWS))
    
    def __str__(self):
        return str(self.grid)

    def _countNeighbours(self, x, y):
        """
        Counts the neighbours around the given cell.
        If the cell is on the edge, only the neighbours on the grid will be counted.
        """
        count = 0
        for dx in range(x-1, (x+1)+1):
            if dx<0 or dx>self.COLUMNS-1: continue

            for dy in range(y-1, (y+1)+1):
                if dy<0 or dy>self.ROWS-1: continue
                if dx == x and dy == y: continue

                if self.grid[dy][dx]==1:
                    count += 1
        return count

    def nextGeneration(self):
        """
        Generates a new generation from the current one given the standard game rules.
        """
        newGrid = np.zeros((self.COLUMNS, self.ROWS))
        for y in range(self.COLUMNS):
            for x in range(self.ROWS):
                count = self._countNeighbours(x,y)
                if self.grid[y][x]==1:
                    if count==2 or count == 3:
                        newGrid[y][x] = 1
                else: #dead but can come alive
                    if count ==3:
                        newGrid[y][x] = 1
        self.grid = newGrid

    def randomize(self):
        """
        Creates a random grid.
        """
        self.grid = np.random.randint(0,2,(self.COLUMNS, self.ROWS))

if __name__ == "__main__":
    ROWS = 100
    COLUMNS = 100
    squareSide = 1000/ROWS
    life = Life(ROWS, COLUMNS)
    life.randomize()

    pg.init()
    pg.font.init()
    font = pg.font.SysFont('Comic Sans MS', 30)

    display: pg.display = pg.display.set_mode((1000, 1000))
    
    running = True
    lastTime = time.time()
    while running:
        display.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        for row in range(ROWS):
            for column in range(COLUMNS):
                if life.grid[column][row]==1:
                    pg.draw.rect(display, (255, 255, 255), (squareSide*column, squareSide*row, squareSide, squareSide))
        
        text = font.render(f"FPS: {round(1/(time.time()-lastTime))}",True, (255,255,255))
        lastTime = time.time()
        display.blit(text, (0,0))
        pg.display.update()
        life.nextGeneration()

