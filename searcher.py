# Shai Acoca 315314278
import copy


# The searcher class all the algorithms inherit from it.
# This class implements all the methods that common to all the algorithms.
class Searcher:
    closed_list = []
    open_list = []

    # Constructor, init the search problem
    def __init__(self, problem):
        self.problem = problem

    # returning it a state is the goal state
    def check_if_goal_state(self, state):
        return state == self.problem.goal

    # Checking if which neighbors are cliffs (has cost of -1)
    def check_if_cliffs(self, x, y):
        board_size = self.problem.size
        board = self.problem.board
        is_cliffs = {}
        # checking if right movement is possible
        if y + 1 < board_size:
            is_cliffs["R"] = board[x][y + 1].cost == -1
        # checking if left movement is possible
        if y - 1 >= 0:
            is_cliffs["L"] = board[x][y - 1].cost == -1
        # checking if top, top right, top left movement are possible
        if x - 1 >= 0:
            is_cliffs["U"] = board[x - 1][y].cost == -1
            if y + 1 < board_size:
                is_cliffs["RU"] = board[x - 1][y + 1].cost == -1
            if y - 1 >= 0:
                is_cliffs["LU"] = board[x - 1][y - 1].cost == -1
        # checking if bottom, bottom right, bottom left movement are possible
        if x + 1 < board_size:
            is_cliffs["D"] = board[x + 1][y].cost == -1
            if y + 1 < board_size:
                is_cliffs["RD"] = board[x + 1][y + 1].cost == -1
            if y - 1 >= 0:
                is_cliffs["LD"] = board[x + 1][y - 1].cost == -1
        return is_cliffs

    # Returns all the possible moves from given node (all the neighbors and the directions)
    def get_all_possible_moves(self, node):
        board_size = self.problem.size
        board = copy.deepcopy(self.problem.board)
        neighbors = []
        x = node.state[0]
        y = node.state[1]
        is_cliffs = self.check_if_cliffs(x=x, y=y)
        # checking if right up movement is possible
        if x - 1 >= 0 and y + 1 < board_size and is_cliffs["U"] is False and is_cliffs["R"] is False \
                and is_cliffs["RU"] is False:
            neighbors.append((board[x - 1][y + 1], 'RU'))
        # checking if up movement is possible
        if x - 1 >= 0 and is_cliffs["U"] is False:
            neighbors.append((board[x-1][y], 'U'))
        # checking if left up movement is possible
        if x - 1 >= 0 and y - 1 >= 0 and is_cliffs["U"] is False and is_cliffs["L"] is False \
                and is_cliffs["LU"] is False:
            neighbors.append((board[x - 1][y - 1], 'LU'))
        # checking if left movement is possible
        if y - 1 >= 0 and is_cliffs["L"] is False:
            neighbors.append((board[x][y - 1], 'L'))
        # checking if left down movement is possible
        if y - 1 >= 0 and x + 1 < board_size and is_cliffs["D"] is False and is_cliffs["L"] is False \
                and is_cliffs["LD"] is False:
            neighbors.append((board[x + 1][y - 1], 'LD'))
        # checking if down movement is possible
        if x + 1 < board_size and is_cliffs["D"] is False:
            neighbors.append((board[x + 1][y], 'D'))
        # checking if right down movement is possible
        if y + 1 < board_size and x + 1 < board_size and is_cliffs["D"] is False and is_cliffs["R"] is False \
                and is_cliffs["RD"] is False:
            neighbors.append((board[x + 1][y + 1], 'RD'))
        # checking if right movement is possible
        if y + 1 < board_size and is_cliffs["R"] is False:
            neighbors.append((board[x][y + 1], 'R'))
        return neighbors

    # Updating a given node
    @staticmethod
    def update_node_data(move, came_from_node, time):
        neighbor = move[0]
        move_str = move[1]
        neighbor.path = came_from_node.path + move_str + "-"
        neighbor.trail_cost = came_from_node.trail_cost + neighbor.cost
        neighbor.came_from = came_from_node.state
        neighbor.depth = came_from_node.depth + 1
        neighbor.time = time

    # Returning if a node is in the close list
    def check_if_in_close_list(self, new_node):
        for node in self.closed_list:
            if node.state == new_node.state:
                return True
        return False

    # Finding a node in the open list (if not exist there returns False).
    def find_state_in_open(self, state):
        for node in self.open_list:
            if node.state == state:
                return node
        return None
