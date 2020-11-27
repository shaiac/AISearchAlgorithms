# Shai Acoca 315314278
from searcher import Searcher
from node import Node
import math


# IDA*  is a graph traversal and path search algorithm that can find the shortest path between a designated
# start node and any member of a set of goal nodes in a weighted graph.
# the idea to use a heuristic function to evaluate the remaining cost to get to the goal.
# Since it is a depth-first search algorithm, its memory usage is lower than in A*.
class IDAStar(Searcher):
    threshold = 0
    goal_node = None
    iterations = 0

    # Returns the estimate cost from given node to the goal node (have to be lower then the real one)
    def heuristic(self, node):
        dx = abs(node.state[0] - self.goal_node.state[0])
        dy = abs(node.state[1] - self.goal_node.state[1])
        return math.sqrt(dx * dx + dy * dy)

    # Running depth first search with limit (the limit is the value of f = g+h)
    def dfs_f(self, node, f_limit):
        f = node.trail_cost + self.heuristic(node=node)
        if f > f_limit:
            self.threshold = min(self.threshold, f)
            return None, None
        if self.check_if_goal_state(node.state):
            return node.path, node.trail_cost
        self.iterations += 1
        possible_moves = self.get_all_possible_moves(node=node)
        time = 0
        for move in possible_moves:
            neighbor = move[0]
            neighbor.trail_cost = node.trail_cost + neighbor.cost
            self.update_node_data(move=move, came_from_node=node, time=time)
            path, trail_cost = self.dfs_f(neighbor, f_limit)
            if path:
                return path, trail_cost
            time += 1
        return None, None

    # Running the algorithm
    def run(self):
        starting_x = int(self.problem.starting_point[0])
        starting_y = int(self.problem.starting_point[1])
        goal_x = int(self.problem.goal[0])
        goal_y = int(self.problem.goal[1])
        self.goal_node = self.problem.board[goal_x][goal_y]
        start_node = self.problem.board[starting_x][starting_y]
        self.threshold = self.heuristic(node=start_node)
        # Loop while resources are available
        while True:
            f_limit = self.threshold
            self.threshold = float('inf')
            path, trail_cost = self.dfs_f(start_node, f_limit)
            if f_limit == self.threshold:
                return "no path"
            if path:
                solution = Node(state=self.goal_node.state, cost=1, trail_cost=trail_cost, came_from=None)
                solution.path = path
                return solution, self.iterations
