import os
import random
import sys
import time


class Maze:
    def __init__(self, x, y):
        self.stack = []
        self.x = x
        self.y = y
        self.rows = 9
        self.cols = 20
        self.found = False
        self.maze = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', 'g', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]

    def printCustomMaze(self):
        self.maze = [['#'] * self.rows for _ in range(self.cols)]
        for i in range(1, self.cols - 1, 2):
            for j in range(1, self.rows - 1, 2):
                self.maze[i][j] = 3
        self.create_random_paths(self.maze)
        rand_goal = random.randint(0, len(self.stack) - 1)
        self.maze[self.stack[rand_goal][0]][self.stack[rand_goal][1]] = 'g'
        return self.maze

    def create_random_paths(self, maze, x=1, y=1):
        maze[x][y] = ' '
        self.stack.append((x, y))
        neighbors = [[x - 2, y], [x + 2, y], [x, y - 2], [x, y + 2]]
        random.shuffle(neighbors)
        for newx, newy in neighbors:
            if newx in range(1, len(maze)) and newy in range(1, len(maze[0])):
                if maze[newx][newy] == 3:
                    maze[int((newx + x) / 2)][int((newy + y) / 2)] = ' '
                    self.stack.append((int((newx + x) / 2), int((newy + y) / 2)))
                    self.create_random_paths(maze, newx, newy)

    def printMaze(self):
        os.system('cls')
        for row in self.maze:
            # for ch in row:
            #     print(ch, end='')
            # print()
            print(row)
        time.sleep(0.4)

    def __iter__(self):
        return self

    def __next__(self):
        self.x, self.y = self.stack[-1]
        return self.x, self.y

    def solveMaze(self):
        if 0 > x or x > (len(self.maze) - 1) or 0 > y or y > (len(self.maze[0]) - 1) or self.maze[x][y] == '#':
            return 'wrong start coordinates'
        if len(self.stack) == 0:
            self.maze[self.x][self.y] = '.'
            self.stack.append((self.x, self.y))
            return self.x, self.y
        elif self.maze[self.x][self.y] == '.':
            index_n = 0
            neighbours = [[self.x, self.y - 1], [self.x, self.y + 1], [self.x - 1, self.y], [self.x + 1, self.y]]
            for newx, newy in neighbours:
                index_n += 1
                if newx in range(1, len(self.maze) - 1) and newy in range(1, len(self.maze[0]) - 1):
                    if self.maze[newx][newy] == 'g':
                        self.found = True
                        return newx, newy
                    elif self.maze[newx][newy] == ' ':
                        index_n -= 1
                        self.maze[newx][newy] = '.'
                        self.stack.append((newx, newy))
                        return newx, newy
            if index_n == 4:
                self.maze[self.x][self.y] = 'x'
                self.stack.pop()
                return self.stack[-1][0], self.stack[-1][1]


x, y = [1, 1]
# args = sys.argv[1:]
# x, y = int(args[0]), int(args[1])
m = Maze(x, y)

while not m.found:
    m.x, m.y = m.solveMaze()
    m.printMaze()

