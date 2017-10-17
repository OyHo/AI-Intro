from New_Board import Board

class A_star:
    current = None
    child = None
    goal = None
    start = None

    def __init__(self, board):  # initialisation to get current node
        self.board = board
        self.start = self.board.start
        self.current = self.board.start
        self.goal = self.board.goal
        self.walls = []

    def neighbors(self, id): # checks 8 adjacent nodes to current
        results = [(self.current.row + 1, self.current.col), (self.current.row, self.current.col - 1), (self.current.row - 1, self.current.col), (self.current.row, self.current.col + 1)]
        for x,y in results:
            if (x,y) == (id.row, id.col):
                return True

    def a_star(self):
        for id in self.board.list:  # find current node
            if self.neighbors(id):  # find current node neighbors
                new_cost = id.val + id.G
                if self.child is None or new_cost < self.child.val + self.child.G:  # check new vs. old cost
                    self.child = id
                id.tried = True
                if id.visited is False:  # check if node visited. If not parents become current
                    id.parent = self.current
                id.G = id.cost + self.current.G  # update successors total cost
                self.current.children.append(id)
                if id.val == 0:  # finished if zero value
                    print("Cost:"+str(id.G))
                    global finished
                    finished = True
                if id.visited is False and id != self.goal and id != self.start:  # Nodes tried are purple
                    self.board.init_canvas(id.col, id.row,'purple', id.val)
        if self.start != self.current and self.goal != self.current:  # Nodes visited are black
            self.board.init_canvas(self.current.col, self.current.row, 'black', self.current.val)
        self.current.visited = True
        if self.child:
            self.current = self.child
        tested = None
        for id in self.board.list:  # find child if there is no more child to the parent
            if id.tried is True and id.visited is False:
                if tested is None:
                    tested = id
                    continue
                if id.val + id.G < tested.val + tested.G:
                    tested = id
        if tested:
            self.child = tested
        self.current = self.child

    def path(self):  # show shortest path
        former_parent = self.board.goal.parent
        for id in self.board.list:
            self.board.init_canvas(id.col, id.row, Board.colors[id.token],  id.val)
        while former_parent.parent:
            self.board.init_canvas(former_parent.col, former_parent.row, 'black', former_parent.val)
            former_parent = former_parent.parent

finished = False
if __name__ == "__main__":
    # CHOOSE BOARD
    B = Board(open("Boards/board-1-1.txt").readlines())
    A = A_star(B)
    count = 0
    while True:
        if finished is False:
            count = count + 1
            print(count)
            A.a_star()
        else:
            A.path()
        B.get_board().update()