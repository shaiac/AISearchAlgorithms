# Shai Acoca 315314278
import heapq
from searcher import Searcher


# Uniform Cost Search is the best algorithm for a search problem, which does not involve the use of heuristics.
# It can solve any general graph for optimal cost.
# Dequeue the maximum priority element from the queue,  If the path is ending in the goal state returns the path,
# else Insert all the children of the dequeued element, with the cumulative costs as priority.
class UCS(Searcher):

    # Runs the algorithm
    def run(self):
        starting_x = int(self.problem.starting_point[0])
        starting_y = int(self.problem.starting_point[1])
        counter = 0
        heapq.heappush(self.open_list, self.problem.board[starting_x][starting_y])
        while len(self.open_list) is not 0:
            next_node = heapq.heappop(self.open_list)
            self.closed_list.append(next_node)
            if self.check_if_goal_state(next_node.state):
                return next_node, counter
            counter += 1
            possible_moves = self.get_all_possible_moves(node=next_node)
            possible_moves.reverse()
            time = 0
            for move in possible_moves:
                neighbor = move[0]
                # if neighbor is in close list
                if self.check_if_in_close_list(neighbor):
                    continue
                self.update_node_data(move, next_node, time)
                old_node = self.find_state_in_open(state=neighbor.state)
                if old_node is not None:
                    if old_node.trail_cost > neighbor.trail_cost:
                        old_node.trail_cost = neighbor.trail_cost
                        old_node.came_from = neighbor.came_from
                        old_node.path = neighbor.path
                else:
                    heapq.heappush(self.open_list, neighbor)
                time += 1
        return "no path"
