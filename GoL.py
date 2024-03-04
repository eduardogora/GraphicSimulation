"""
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

"""
    In order to run this program you need to have a txt file called "input"
    in the same folder as the py code.
    The input must have the next format:

    10 10 //width and height of the grid
    10    //Number of generations
    2 2   //x and y coordinates of living points
    5 5
    ...
    ...
    7 7

    Its important to say that each numbesr must be separated by an space
    you can choose all the live points you may want
    
    In order to advance the animation, is necessary to press a key in the keyboard

"""


import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button


with open('input.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()

splite = contents.split("\n")

n = int(splite[0].split(" ")[0])
m = int(splite[0].split(" ")[1])
generationsNumber = int(splite[1])
dots = []

for i in range(2, len(splite)):
    dotX = int(splite[i].split(" ")[0])
    dotY = int(splite[i].split(" ")[1])
    dots.append({"x": dotX, "y": dotY})




ON = 1
OFF = 0
vals = [ON, OFF]
imgs = []
current_image = 0

#FIGURES
#---Glider---
glider1_1 = np.array([[0, 1, 0],
                   [0, 0, 1],
                   [1, 1, 1]])

glider1_2 = np.array([[1, 0, 0],
                      [1, 0, 1],
                      [1, 1, 0]])

glider1_3 = np.array([[1, 1, 1],
                      [1, 0, 0],
                      [0, 1, 0]])

glider1_4 = np.array([[0, 1, 1],
                      [1, 0, 1],
                      [0, 0, 1]])

glider2_1 = np.array([[1, 0, 1],
                      [0, 1, 1],
                      [0, 1, 0]])

glider2_2 = np.array([[0, 0, 1],
                      [1, 1, 0],
                      [0, 1, 1]])

glider2_3 = np.array([[0, 1, 0],
                      [1, 1, 0],
                      [1, 0, 1]])

glider2_4 = np.array([[1, 1, 0],
                      [0, 1, 1],
                      [1, 0, 0]])

glider3_1 = np.array([[0, 0, 1],
                      [1, 0, 1],
                      [0, 1, 1]])

glider3_2 = np.array([[0, 1, 0],
                      [1, 0, 0],
                      [1, 1, 1]])

glider3_3 = np.array([[1, 1, 0],
                      [1, 0, 1],
                      [1, 0, 1]])

glider3_4 = np.array([[1, 1, 1],
                      [0, 0, 1],
                      [0, 1, 0]])

glider4_1 = np.array([[1, 0, 0],
                      [0, 1, 1],
                      [1, 1, 0]])

glider4_2 = np.array([[1, 0, 1],
                      [1, 1, 0],
                      [0, 1, 0]])

glider4_3 = np.array([[0, 1, 1],
                      [1, 1, 0],
                      [0, 0, 1]])

glider4_4 = np.array([[0, 1, 0],
                      [0, 1, 1],
                      [1, 0, 1]])

#---Block---
block = np.array([[1, 1],
                 [1, 1]])
#---Beehive---
beehive1 = np.array([[0, 1, 1, 0],
                     [1, 0, 0, 1],
                     [0, 1, 1, 0]])

beehive2 = np.array([[0, 1, 0],
                     [1, 0, 1],
                     [1, 0, 1],
                     [0, 1, 0]])

#---Loaf---
loaf1 = np.array([[0, 1, 1, 0],
                  [1, 0, 0, 1],
                  [0, 1, 0, 1],
                  [0, 0, 1, 0]])

loaf2 = np.array([[0, 0, 1, 0],
                  [0, 1, 0, 1],
                  [1, 0, 0, 1],
                  [0, 1, 1, 0]])

loaf3 = np.array([[0, 1, 0, 0],
                  [1, 0, 1, 0],
                  [1, 0, 0, 1],
                  [0, 1, 1, 0]])

loaf4 = np.array([[0, 1, 1, 0],
                  [1, 0, 0, 1],
                  [1, 0, 1, 0],
                  [0, 1, 0, 0]])

#---Boat---
boat1 = np.array([[1, 1, 0],
                  [1, 0, 1],
                  [0, 1, 0]])

boat2 = np.array([[0, 1, 1],
                  [1, 0, 1],
                  [0, 1, 0]])

boat3 = np.array([[0, 1, 0],
                  [1, 0, 1],
                  [0, 1, 1]])

boat4 = np.array([[0, 1, 0],
                  [1, 0, 1],
                  [1, 1, 0]])

#---Tub---
tub = np.array([[0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]])

#---Blinker---
blinker1 = np.array([[1],
                     [1],
                     [1]])

blinker2 = np.array([[1, 1, 1]])

#---Toad---
toad1 = np.array([[0, 0, 1, 0],
                  [1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [0, 1, 0, 1],])

toad2 = np.array([[0, 1, 1, 0],
                  [1, 0, 0, 0],
                  [0, 0, 0, 1],
                  [0, 1, 1, 0],])

toad3 = np.array([[0, 1, 1, 1],
                  [1, 1, 1, 0]])

toad4 = np.array([[1, 0],
                  [1, 1],
                  [1, 1],
                  [0, 1]])

#---Beacon---
beacon1 = np.array([[1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1]])

beacon2 = np.array([[0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [1, 1, 0, 0],
                    [1, 1, 0, 0]])

beacon3 = np.array([[1, 1, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 1, 1]])

beacon4 = np.array([[0, 0, 1, 1],
                    [0, 0, 0, 1],
                    [1, 0, 0, 0],
                    [1, 1, 0, 0]])

#---Lightweight Spaceships---

lws1_1 = np.array([[1, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1],
                   [0, 1, 1, 1, 1]])

lws1_2 = np.array([[0, 1, 0, 1],
                   [1, 0, 0, 0],
                   [1, 0, 0, 0],
                   [1, 0, 0, 1],
                   [1, 1, 1, 0]])

lws1_3 = np.array([[1, 1, 1, 1, 0],
                   [1, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 1]])

lws1_4 = np.array([[0, 1, 1, 1],
                   [1, 0, 0, 1],
                   [0, 0, 0, 1],
                   [0, 0, 0, 1],
                   [1, 0, 1, 0]])

lws2_1 = np.array([[0, 0, 1, 1, 0],
                   [1, 1, 0, 1, 1],
                   [1, 1, 1, 1, 0],
                   [0, 1, 1, 0, 0]])

lws2_2 = np.array([[0, 1, 1, 0],
                   [1, 1, 1, 0],
                   [1, 1, 0, 1],
                   [0, 1, 1, 1],
                   [0, 0, 1, 0]])

lws2_3 = np.array([[0, 0, 1, 1, 0],
                   [0, 1, 1, 1, 1],
                   [1, 1, 0, 1, 1],
                   [0, 1, 1, 0, 0]])

# print(numGliderTotal  = funcion(grid, figure) + funcion(grid, figure2)+ ... + funcion(grid, figure n))
lws2_4 = np.array([[0, 1, 0, 0],
                   [1, 1, 1, 0],
                   [1, 0, 1, 1],
                   [0, 1, 1, 1],
                   [0, 1, 1, 0]])

lws3_1 = np.array([[0, 1, 1, 1, 1],
                   [1, 0, 0, 0, 1],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0]])

lws3_2 = np.array([[1, 0, 1, 0],
                   [0, 0, 0, 1],
                   [0, 0, 0, 1],
                   [1, 0, 0, 1],
                   [0, 1, 1, 1]])

lws3_3 = np.array([[0, 1, 0, 0, 1],
                   [1, 0, 0, 0, 0],
                   [1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 0]])

lws3_4 = np.array([[1, 1, 1, 0],
                   [1, 0, 0, 1],
                   [1, 0, 0, 0],
                   [1, 0, 0, 0],
                   [0, 1, 0, 1]])


lws4_1 = np.array([[0, 1, 1, 0, 0],
                   [1, 1, 1, 1, 0],
                   [1, 1, 0, 1, 1],
                   [0, 0, 1, 1, 0]])

lws4_2 = np.array([[0, 1, 1, 0],
                   [0, 1, 1, 1],
                   [1, 0, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 0, 0]])

lws4_3 = np.array([[0, 1, 1, 0, 0],
                   [1, 1, 0, 1, 1],
                   [0, 1, 1, 1, 1],
                   [0, 0, 1, 1, 0]])

lws4_4 = np.array([[0, 0, 1, 0],
                   [0, 1, 1, 1],
                   [1, 1, 0, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0]])





class Iteration:
    def __init__(self, v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
        self.numBlock = v0
        self.numBeehive = v1
        self.numLoaf = v2
        self.numBoat = v3
        self.numTub = v4
        self.numBlinker = v5
        self.numToad = v6
        self.numBeacon = v7
        self.numGlider = v8
        self.numLightweightSpaceships = v9
        self.numTotal = v10

data = []


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def getVecinos(grid, x, y):
    numVecinos = 0

    #Vecinos de Arriba
    if(grid[x - 1][y - 1] == 1):
        numVecinos += 1

    if(grid[  x  ][y - 1] == 1):
        numVecinos += 1

    if(grid[x + 1][y - 1] == 1):
        numVecinos += 1

    #Vecinos de Enmedio
    if(grid[x - 1][y] == 1):
        numVecinos += 1

    if(grid[x + 1][y] == 1):
        numVecinos += 1

    #Vecinos de Abajo
    if(grid[x - 1][y + 1] == 1):
        numVecinos += 1

    if(grid[  x  ][y + 1] == 1):
        numVecinos += 1

    if(grid[x + 1][y + 1] == 1):
        numVecinos += 1

    return numVecinos

def getNextGrid(grid, N):
    newGrid = np.array([])

    #Hacemos el upgrade de nuestra matriz
    originalGrid = upgradeMatriz(N, N, grid)
    newGrid = upgradeMatriz(N, N, grid)

    #Validamos las reglas
    for i in range(1, N):
        for j in range(1, N):
            if(originalGrid[i][j] == 1):
                if getVecinos(originalGrid, i, j) == 2 or getVecinos(originalGrid, i, j) == 3:
                    newGrid[i][j] = 1
                else:
                    newGrid[i][j] = 0
            else:
                if getVecinos(originalGrid, i, j) == 3:
                    newGrid[i][j] = 1
                else:
                    newGrid[i][j] = 0


    #print("-------------------------")
    matrix = returnMatrix(N, N, newGrid)

    #Revision
    #iteration.numSpaceships = checkGlider(matrix, glider3_1)
    #print(iteration.numSpaceships)

    return matrix

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 1],
                       [1, 0, 1],
                       [0, 1, 1]])
    grid[i:i+3, j:j+3] = glider


def checkGlider(grid, figure):
    numFigure = 0
   # print("Este es el grid que entró:")
    # #print(grid)

    for i in range(0, len(grid) - len(figure)-1):
        for j in range(0, len(grid[0]) - len(figure)-1):
            coincidencia = True
            for k in range(len(figure)):
                for l in range(len(figure[0])):
                    if int(grid[i + k][j + l]) != int(figure[k][l]):
                        coincidencia = False
                        break
                if not coincidencia:
                    break
            if coincidencia:
                numFigure += 1

    return numFigure
"""def checkGlider(grid, N):
    print(grid)
    glider = np.array([[0, 0, 1],
                       [1, 0, 1],
                       [0, 1, 1]])
    numGlider = 0
    for i in range(N - 2):
        for j in range(N - 2):
            submatrix = grid  # Obteniendo solo los primeros dos valores de las primeras dos filas

            if np.array_equal(submatrix, glider[:2, :2]):  # Comprobando con los primeros dos valores de las primeras dos filas del glider
                numGlider += 1

    return numGlider"""

def upgradeMatriz(n, m, matrix):
    newMatrix = []
    firstLine = []
    for i in range(0, m+2):
        firstLine.append(0)

    newMatrix.append(firstLine)

    for i in range(0, n):
        line = []
        line.append(0)
        for j in range(0, m):
            line.append(matrix[i][j])
        line.append(0)
        newMatrix.append(line)


    newMatrix.append(firstLine)
    return newMatrix

def returnMatrix(n, m, matrix):
    nm = matrix
    nm.pop(0)
    nm.pop(-1)
    for i in range(0, n):
        nm[i].pop(0)
        nm[i].pop(-1)
    return nm

"""def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    
    newGrid = getNextGrid(grid, N)
    # TODO: Implement the rules of Conway's Game of Life

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return (img,)"""
    
# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    global m, n, generationsNumber, dots
    # set grid size
    M = m
    N = n


    generations = generationsNumber

    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on


    # Uncomment lines to see the "glider" demo
    grid = np.zeros(N*N).reshape(N, M)
    #addGlider(1, 1, grid)
    for dot in dots:
        grid[dot.get("x"), dot.get("y")] = 1
    nextGrid = getNextGrid(grid, N)

    print("Grid \n", grid)
    print("Next \n", nextGrid)


    #Pruebas
    image1 = np.uint8(255 * grid)
    imgs = [image1]
    numBlock = checkGlider(grid, block)
    numBeehive = checkGlider(grid, beehive1) + checkGlider(grid, beehive2)
    numLoaf = checkGlider(grid, loaf1) + checkGlider(grid, loaf2) + checkGlider(grid, loaf3) + checkGlider(grid, loaf4)
    numBoat = checkGlider(grid, boat1) + checkGlider(grid, boat2) + checkGlider(grid, boat3) + checkGlider(grid, boat4)
    numTub = checkGlider(grid, tub)
    numBlinker = checkGlider(grid, blinker1) + checkGlider(grid, blinker2)
    numToad = checkGlider(grid, toad1) + checkGlider(grid, toad2) + checkGlider(grid, toad3) + checkGlider(grid, toad4)
    numBeacon = checkGlider(grid, beacon1) + checkGlider(grid, beacon2) + checkGlider(grid, beacon3) + checkGlider(grid, beacon4)
    numGlider = checkGlider(grid, glider1_1) + checkGlider(grid, glider1_2) + checkGlider(grid, glider1_3) + checkGlider(grid, glider2_1) + checkGlider(grid, glider2_2) + checkGlider(grid, glider2_3) + checkGlider(grid, glider2_4) + checkGlider(grid, glider3_1) + checkGlider(grid, glider3_2) + checkGlider(grid, glider3_3) + checkGlider(grid, glider3_4) + checkGlider(grid, glider4_1) + checkGlider(grid, glider4_2) + checkGlider(grid, glider4_3) + checkGlider(grid, glider4_4)
    numLightweightSpaceships = checkGlider(grid, lws1_1) + checkGlider(grid, lws1_2) + checkGlider(grid,lws1_3) + checkGlider(grid, lws1_4) + checkGlider(grid, lws2_1) + checkGlider(grid, lws2_2) + checkGlider(grid, lws2_3) + checkGlider(grid, lws2_4) + checkGlider(grid, lws3_1) + checkGlider(grid, lws3_2) + checkGlider(grid, lws3_3) + checkGlider(grid, lws3_4) + checkGlider(grid, lws4_1) + checkGlider(grid, lws4_2) + checkGlider(grid, lws4_3) + checkGlider(grid, lws4_4)

    numTotal = numBlock + numBeehive + numLoaf + numBoat + numTub + numBlinker + numToad + numBeacon + numGlider + numLightweightSpaceships
    if (numTotal == 0):
        numTotal = 1
    
    it = Iteration(numBlock, numBeehive, numLoaf, numBoat, numTub, numBlinker, numToad, numBeacon, numGlider, numLightweightSpaceships, numTotal)
    data.append(it)

    for i in range(2, generations + 1):
        nextGrid = getNextGrid(grid, N)
        newImage = np.uint8(255 * nextGrid)
        grid = nextGrid
        imgs.append(newImage)
        numBlock = checkGlider(grid, block)
        numBeehive = checkGlider(grid, beehive1) + checkGlider(grid, beehive2)
        numLoaf = checkGlider(grid, loaf1) + checkGlider(grid, loaf2) + checkGlider(grid, loaf3) + checkGlider(grid, loaf4)
        numBoat = checkGlider(grid, boat1) + checkGlider(grid, boat2) + checkGlider(grid, boat3) + checkGlider(grid, boat4)
        numTub = checkGlider(grid, tub)
        numBlinker = checkGlider(grid, blinker1) + checkGlider(grid, blinker2)
        numToad = checkGlider(grid, toad1) + checkGlider(grid, toad2) + checkGlider(grid, toad3) + checkGlider(grid, toad4)
        numBeacon = checkGlider(grid, beacon1) + checkGlider(grid, beacon2) + checkGlider(grid, beacon3) + checkGlider(grid, beacon4)
        numGlider = checkGlider(grid, glider1_1) + checkGlider(grid, glider1_2) + checkGlider(grid, glider1_3) + checkGlider(grid, glider1_4) + checkGlider(grid, glider2_1) + checkGlider(grid, glider2_2) + checkGlider(grid, glider2_3) + checkGlider(grid, glider2_4)+ checkGlider(grid, glider3_1) + checkGlider(grid, glider3_2) + checkGlider(grid, glider3_3) + checkGlider(grid, glider3_4) + checkGlider(grid, glider4_1) + checkGlider(grid, glider4_2) + checkGlider(grid, glider4_3) + checkGlider(grid, glider4_4)
        numLightweightSpaceships = checkGlider(grid, lws1_1) + checkGlider(grid, lws1_2) + checkGlider(grid, lws1_3) + checkGlider(grid, lws1_4) + checkGlider(grid, lws2_1) + checkGlider(grid, lws2_2) + checkGlider(grid, lws2_3) + checkGlider(grid, lws2_4) + checkGlider(grid, lws3_1) + checkGlider(grid, lws3_2) + checkGlider(grid, lws3_3) + checkGlider(grid, lws3_4) + checkGlider(grid, lws4_1) + checkGlider(grid, lws4_2) + checkGlider(grid, lws4_3) + checkGlider(grid, lws4_4)

        numTotal = numBlock + numBeehive + numLoaf + numBoat + numTub + numBlinker + numToad + numBeacon + numGlider + numLightweightSpaceships
        if (numTotal == 0):
            numTotal = 1
        
        it = Iteration(numBlock, numBeehive, numLoaf, numBoat, numTub, numBlinker, numToad, numBeacon, numGlider, numLightweightSpaceships, numTotal)
        data.append(it)

        
       



    # Create a figure and a set of subplots that share the same axes
    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    ax.set_xlim(0, N)
    ax.set_ylim(N, 0)

    # Display the first image
    ax.imshow(image1, cmap='Blues')
    ax.set_title('Generation 1')

    # Flag to keep track of which image is currently displayed


    # Function to toggle the visibility of the images
    def toggle_images(event):
        global current_image

        # Update the data displayed in the subplot with the other image
        current_image = (current_image + 1) % generations
        ax.imshow(imgs[current_image], cmap='Blues')
        ax.set_title('Generation ' + str(current_image + 1))

        plt.draw()

    # Connect the toggle_images function to a key press event
    cid = fig.canvas.mpl_connect('key_press_event', toggle_images)
    plt.show()
    #End pruebas

    #fig, ax = plt.subplots()
    #img = ax.imshow(grid, interpolation='nearest')

    plt.show()


grid = np.array([])
# call main
if __name__ == '__main__':
    main()

with open('output.txt', 'w') as f:
    for i in range(0, len(data)):
            f.write('|---------------------------------------------------|\n')
            f.write('|                  ITERATION {i}                      |\n'.format(i=i+1))
            f.write('|---------------------------------------------------|\n')
            f.write('|                        |   COUNT    |   PERCENT   |\n')
            f.write('|------------------------+------------+-------------|\n')
            f.write('|   BLOCK                |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numBlock, (data[i].numBlock * 100) / data[i].numTotal))
            f.write('|   BEEHIVE              |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numBeehive, (data[i].numBeehive * 100) / data[i].numTotal))
            f.write('|   LOAF                 |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numLoaf, (data[i].numLoaf * 100) / data[i].numTotal))
            f.write('|   BOAT                 |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numBoat, (data[i].numBoat * 100) / data[i].numTotal))
            f.write('|   TUB                  |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numTub, (data[i].numTub * 100) / data[i].numTotal))
            f.write('|   BLINKER              |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numBlinker, (data[i].numBlinker * 100) / data[i].numTotal))
            f.write('|   TOAD                 |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numToad, (data[i].numToad * 100) / data[i].numTotal))
            f.write('|   BEACON               |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numBeacon, (data[i].numBeacon * 100) / data[i].numTotal))
            f.write('|   GLIDER               |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numGlider, (data[i].numGlider * 100) / data[i].numTotal))
            f.write('|   LW SPACESHIP         |   {:4d}    |  {:5.2f}%      |\n'.format(data[i].numLightweightSpaceships, (data[i].numLightweightSpaceships * 100) / data[i].numTotal))
            f.write('|------------------------+------------+-------------|\n')
            f.write('|   TOTAL                |   {:4d}    |              |\n'.format(data[i].numTotal))
            f.write('|---------------------------------------------------|\n')
            f.write('\n')