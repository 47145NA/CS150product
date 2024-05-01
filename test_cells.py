# test_cells.py
# A program for testing whether the Cell class in life.py is implemented correctly.
#
# Names: Cynthia Taylor and Adam Eck

from life import Cell

WIDTH = 10
HEIGHT = 10

#create grid of cells
cells = []
for x in range(WIDTH):
  cells.append([])

  for y in range(HEIGHT):
    cells[x].append(Cell(x, y))

#initialize some cells to alive
cells[5][5].alive = True
cells[5][6].alive = True
cells[5][7].alive = True

cells[5][5].last = True
cells[5][6].last = True
cells[5][7].last = True

#test countNeighbors method.  Should return 2.
print("Cell 5,6 has", cells[5][6].countNeighbors(cells), " alive neighbors")

#update 3 times and print to the screen (like the prelab)
for i in range(3):
  for x in range(WIDTH):
    for y in range(HEIGHT):
      if cells[x][y].alive:
        print("x",end="")
      else:
        print(".",end="")
    print()
  print()

  for x in range(WIDTH):
    for y in range(HEIGHT):
      cells[x][y].last = cells[x][y].alive

  for x in range(WIDTH):
    for y in range(HEIGHT):
      cells[x][y].update(cells)
