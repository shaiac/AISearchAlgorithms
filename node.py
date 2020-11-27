# Shai Acoca 315314278


# The node class has all the information about a node that we need
class Node:
    def __init__(self, state, cost, trail_cost, came_from):
        self.state = state
        self.cost = cost
        self.trail_cost = trail_cost
        self.path = ""
        self.came_from = came_from
        self.f_estimated_cost = 0
        self.depth = 0
        self.time = 0

    # operator overloading '>'
    def __lt__(self, other):
        if self.came_from == other.came_from and self.trail_cost == other.trail_cost:
            return self.time < other.time
        return self.trail_cost < other.trail_cost
