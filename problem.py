# Shai Acoca 315314278
from node import Node


# The problem class has all the information about that search problem that the algorithm need.
# the board, starting node, goal node, the board size.
class Problem:

    # Getting board only with the costs of the nodes and returning board of nodes
    @staticmethod
    def create_board(ints_board):
        board = []
        i = 0
        for row in ints_board:
            j = 0
            nodes_row = []
            for cell in row:
                nodes_row.append(Node(state=(i, j), cost=ints_board[i][j], trail_cost=0, came_from=None))
                j += 1
            board.append(nodes_row)
            i += 1
        return board

    # Converts tuple of strings to ints.
    @staticmethod
    def goal_in_int(str_goal):
        split = str_goal.split(',')
        return int(split[0]), int(split[1])

    # Constructor
    def __init__(self, problem_data):
        self.starting_point = problem_data[1].split(',')
        self.goal = self.goal_in_int(problem_data[2])
        self.size = int(problem_data[3])
        self.board = self.create_board(problem_data[4])
