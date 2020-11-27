# Shai Acoca 315314278
import heapq
import math
from searcher import Searcher


# A* is an optimality, and optimal efficiency path search algorithm, time complexity of O(b^d).
# the algorithm using priority queue to pop the node with the lowest cost, heuristic function to estimate the cost
# to the goal. the class inherit from the searcher class
class AStar(Searcher):
    goal_node = None

    # Returns the estimate cost from given node to the goal node (have to be lower then the real one)
    def heuristic(self, node):
        dx = abs(node.state[0] - self.goal_node.state[0])
        dy = abs(node.state[1] - self.goal_node.state[1])
        return math.sqrt(dx * dx + dy * dy)

    # Runs the algorithm
    def run(self):
        starting_x = int(self.problem.starting_point[0])
        starting_y = int(self.problem.starting_point[1])
        goal_x = int(self.problem.goal[0])
        goal_y = int(self.problem.goal[1])
        counter = 0
        self.goal_node = self.problem.board[goal_x][goal_y]
        start_node = self.problem.board[starting_x][starting_y]
        # Pushing the stating node to the priority queue
        heapq.heappush(self.open_list, start_node)
        while len(self.open_list) is not 0:
            next_node = heapq.heappop(self.open_list)
            self.closed_list.append(next_node)
            # Found the goal node return the solution
            if self.check_if_goal_state(next_node.state):
                return next_node, counter
            # Getting all the node neighbors
            possible_moves = self.get_all_possible_moves(node=next_node)
            for move in possible_moves:
                neighbor = move[0]
                # if neighbor is in close list
                if self.check_if_in_close_list(neighbor):
                    continue
                # Cal f = g + h (the cost from the start + the estimated cost to the goal)
                neighbor.trail_cost = next_node.trail_cost + neighbor.cost
                neighbor.f_estimated_cost = neighbor.trail_cost + self.heuristic(neighbor)
                neighbor.path = next_node.path + move[1] + "-"
                old_node = self.find_state_in_open(state=neighbor.state)
                if old_node is not None:
                    # updating existing node value to the better path we found
                    if old_node.f_estimated_cost > neighbor.f_estimated_cost:
                        old_node.f_estimated_cost = neighbor.f_estimated_cost
                        old_node.came_from = neighbor.came_from
                        old_node.trail_cost = neighbor.trail_cost
                        old_node.path = neighbor.path
                else:
                    heapq.heappush(self.open_list, neighbor)
            counter += 1
        return "no path"
