from Tkinter import *
from Node import Node

class Board:
    screen = 'black'
    list = []
    start = None
    goal = None
    colors = { # tokens given in task description
        '.': 'white', # none
        '#': 'grey',  # obstacle
        'A': 'red',  # start
        'B': 'red',  # finish
        'w': 'blue',  # water
        'm': 'grey',  # mountains
        'f': 'darkgreen',  # forest
        'g': 'lawngreen',  # grass
        'r': 'brown'  # roads
    }
    cost = { # Part 2 adds terrain cost
        '.': 0, # none
        '#': 0,  # obstacle
        'A': 0,  # start
        'B': 0,  # finish
        'w': 100,  # water
        'm': 50,  # mountain
        'f': 10,  # forest
        'g': 5,  # grass
        'r': 1  # roads
    }
    def __init__(self, file):
        self.file = file
        self.screen = Tk()
        self.init_board(file)
        self.make_board(file)

    def init_board(self,file):# initializes the board
        for row, line in enumerate(file):
            for col, token in enumerate(line):
                if token == '\n':
                    continue
                Can1 = Canvas(self.screen, width=20, height=20)
                Can1.grid(column=col, row=row)
                node = Node(row, col, None, 0, token)
                self.check_if_start_goal(token,node)

    def make_board(self,file):  # creates the actual colored board
        for row, line in enumerate(self.file):
            for col, token in enumerate(line):
                if token == '\n':
                    continue
                if token != '#':
                    Can2 = Canvas(self.screen, width=20, height=20, bg=self.colors[token])
                    Can2.grid(column=col, row=row)
                    val = self.heuristic(row,col)
                    node = Node(row, col, val, token, self.cost[token])
                    self.check_if_start_goal(token,node)
                    self.list.append(node)

    def heuristic(self, row, col): #method for heuristic funtion
        return abs(self.goal.col-col) + abs(self.goal.row-row)

    def check_if_start_goal(self, token, node): # Method to check if node is start or goal
        if token == 'A':
            self.start = node
        elif token == 'B':
            self.goal = node

    def update(self): # method for update
        self.screen.update()

    def init_canvas(self, col, row, color, cost): #initializes color to the grid
        c = Canvas(self.screen, width=20, height=20, bg=color)
        c.grid(column=col, row=row)

    def get_board(self): # gets the board
        return self.screen