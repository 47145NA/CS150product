# life.py
# This program implements the Game of Life!
#
# Partner allowed (and encouraged).
#
# Name(s): Nam Anh Nguyen
# Date: 2-April-2021

import picture
import time
import sys

# define Cell class
class Cell():
  
  # define __init__
  def __init__(self, x, y, alive=False, time = 0):
    self.x = x
    self.y = y
    self.alive = False
    self.time = 0

  # return value of alive
  def getStatus(self):
    return self.alive

  # return value of age
  def getTime(self):
    return self.time

  # change the alive value
  def update(self, i):
    if (i == 3) or (i == 2 and self.alive == True):
      self.alive = True
      self.time += 1
    elif i < 2 or i > 3:
      self.alive = False
      self.time = 0

# define class Board
class Board():
  # define __init__
  def __init__(self, w, h):
    self.w = w
    self.h = h

    # setup picture
    global pic 
    pic = picture.Picture(self.w*25, self.h*25)

    # store lists of Cell in the Board in 2D array
    global cellList
    cellList = []
    for i in range(self.w):
      cell = []
      for j in range(self.h):
        cell.append(Cell(i,j))
      cellList.append(cell)
    # store the time of loop in program
    global cnt
    cnt = 0

    # store the alive status of all Cell in the Board
    global statusMap
    statusMap = []
    for i in range(self.w):
      cell = []
      for j in range(self.h):
        cell.append(0)
      statusMap.append(cell)

    # store the previous alive status of all Cell in the Board
    global temp
    temp = []
    for i in range(self.w):
      cell = []
      for j in range(self.h):
        cell.append(0)
      temp.append(cell)

  # display Cells
  def createCell(self):
    global pic
    global cellList
    for i in range(self.w):
      for j in range(self.h):
        if cellList[i][j].getStatus():
          youth = cellList[i][j].getTime()
          if youth*51 > 255:
            youth = 5
          pic.setFillColor(255-youth*51, 0, youth*51)
        else:
          pic.setFillColor(255, 255, 255)
        pic.drawSquare(i*25, j*25, 25)
    pic.display()

  # Count the neighbor Cells
  def neighborCnt(self, x, y):
    global cellList
    global statusMap
    arr = list()
    for i in range(x, x + 3):
      for j in range(y, y +3):
        arr.append(cellList[(i-1)%self.w][(j-1)%self.h])
    arr.pop(4)
    cnt = 0
    for i in range(len(arr)):
      if arr[i].getStatus():
        cnt += 1
    statusMap[x][y] = cnt

  # Determine if the program is ended
  def doomDay(self, num):
    global statusMap
    global temp
    doom = True
    global cnt
    cnt += 1
    for i in range(self.w):
      for j in range(self.h):
        if temp[i][j] != statusMap[i][j]:
          temp[i][j] = statusMap[i][j]
          doom = False
    if (doom or cnt == num):
      print('Your world is doom!')
      input()
      sys.exit()

  # Create models for the game
  def pattern(self, pattern):
    global cellList
    if pattern == 1:
      for i in range(self.w):
        for j in range(self.h):
          if (j%4 == 2 or i%7 == 2 or j == i or i == 3*j):
            cellList[i][j].alive = True
    if pattern == 2:
      for i in range(self.w):
        for j in range(self.h):
          if (i%(j+1) == 0 or j%(i+1) == 0 or i == 2*j):
            cellList[i][j].alive = True
    if pattern == 3:
      for i in range(self.w):
        for j in range(self.h):
          if ((i*j > 80 and i*j < 90) or i*j < 10 or i == 5*j or j == 3*i):
            cellList[i][j].alive = True
    self.createCell()

  # Custom build for the game
  def design(self, pattern):
    global cellList
    if pattern == 1:
      pointX = input('Please implement the point you want to setup:\nx: ')
      pointY = input('y: ')
      pointX = checkType(pointX, self.w+1)
      pointY = checkType(pointY, self.h+1)
      cellList[pointX-1][pointY-1].alive = True
    if pattern == 2:
      line = input('Please implement the line you want to draw:\nx: ')
      line = checkType(line, self.w+1)
      start = input('From: ')
      start = checkType(start, self.h+1)
      des = input('To: ')
      des = checkType(des, self.h+1)
      if des < start:
        tem = start
        start = des
        des = tem
      for i in range(start, des+1):
        cellList[line-1][i-1].alive = True
    if pattern == 3:
      line = input('Please implement the line you want to draw:\nx: ')
      line = checkType(line, self.h+1)
      start = input('From: ')
      start = checkType(start, self.w+1)
      des = input('To: ')
      des = checkType(des, self.w+1)
      if des < start:
        tem = start
        start = des
        des = tem
      for i in range(start, des+1):
        cellList[i-1][line-1].alive = True
    self.createCell()

  # Running loop in the game
  def lastingUntil(self, num):
    global cellList
    global statusMap
    for i in range(self.w):
      for j in range(self.h):
        self.neighborCnt(i, j)
    for i in range(self.w):
      for j in range(self.h):
        cellList[i][j].update(statusMap[i][j])
    self.createCell()
    self.doomDay(num)


# Check the input type and range
def checkType(num, limit:int):
  while True:
    try:
      num = int(num)
      if num < limit and num > 0:
        return num
      else:
        num = input(f'Please choose 1 in {limit-1} option!')
    except ValueError:
      num = input(f'Please choose 1 in {limit-1} option!')

# Main programming
def main():
  print("Hello to the game of life. You can degisn your own game in here.\nPlease select your boardsize:")
  while True:
    try:
      inputX = int(input('x: '))
      inputY = int(input('y: '))
      if inputX > 0 and inputY > 0:
        break
      else:
        print('Please indicate the positive value!')
    except Error:
      print('Please try to indicate the integer value!')

  print('Your board is here!')
  board = Board(inputX, inputY)
  board.createCell()
  
  while True:
    pat = input('Please select the edit option, you can also choose some built models.\n1. Models\n2. Draw\n3. Run\n')
    pat = checkType(pat, 4)
    if pat == 1:
      choice = input('Please choose a model:\n1. Model 1\n2. Model 2\n3. Model 3\n')
      choice = checkType(choice, 4)
      board.pattern(choice)
    if pat == 2:
      choice = input('Please choose:\n1. Point\n2. Vertical\n3. Horizontal\n')
      choice = checkType(choice, 4)
      board.design(choice)
    if pat == 3:
      while True:
        time.sleep(1)
        board.lastingUntil(10000)

main()