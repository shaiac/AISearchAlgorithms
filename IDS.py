# Shai Acoca 315314278
import copy
from searcher import Searcher


class IDS(Searcher):
    iterations = 0

    # Constructor, calling the searcher class constructor, and getting another arg the max depth to search.
    def __init__(self, problem, max_depth):
        super().__init__(problem)
        self.max_depth = max_depth

    # Pushing all the nodes that came from all possible moves into the stack
    def push_all_successors(self, stack, moves, parent):
        time = 0
        for move in moves:
            self.update_node_data(move, parent, time)
            stack.append(move[0])
            time += 1

    # Running dfs, going down until some given limit. each iteration popping node from the stack, checking if it is
    # the goal and pushing all his neighbors.
    def dfs_l(self, start, limit):
        counter = 0
        clone_board = copy.deepcopy(self.problem.board)
        stack = [clone_board[int(start[0])][int(start[1])]]
        while len(stack) is not 0:
            next_node = stack.pop()
            if self.check_if_goal_state(next_node.state):
                return next_node, self.iterations
            self.iterations += 1
            if next_node.depth < limit:
                self.push_all_successors(stack=stack, moves=self.get_all_possible_moves(next_node), parent=next_node)
                counter += 1
        return False

    # Running the algorithm
    def run(self):
        for limit in range(self.max_depth):
            dfs_l_output = self.dfs_l(start=self.problem.starting_point, limit=limit)
            if dfs_l_output is not False:
                return dfs_l_output
        return "no path"
