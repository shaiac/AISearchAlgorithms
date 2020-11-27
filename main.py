# Shai Acoca 315314278
import sys
from UCS import UCS
from A_star import AStar
from IDS import IDS
from IDA_star import IDAStar
from problem import Problem


# Getting string of a line in the board and returning array of strings with the nodes costs
def get_line_as_array(line):
    split_line = line.split(',')
    return [int(i) for i in split_line]


# Reading the file (getting the name as an argument) and returning all the problem data
def read_file(file_name):
    board = []
    # f = open(sys.argv[1], "r")
    f = open(file_name, "r")
    algorithm_name = f.readline().strip('\n')
    starting_point = f.readline().strip('\n')
    ending_point = f.readline().strip('\n')
    board_size = f.readline().strip('\n')
    for line in f:
        board.append(get_line_as_array(line.strip('\n')))
    return algorithm_name, starting_point, ending_point, board_size, board


# Writing the solution into file output.txt
def write_output(output):
    if output == "no path":
        solution = output
    else:
        solution = output[0].path.strip('-') + " " + str(output[0].trail_cost) + " " + str(output[1])
    f = open("output.txt", "w")
    f.write(solution)
    f.close()


# Running the requested algorithm with the given problem
def run_requested_algorithm(problem):
    output = None
    algorithm_name = problem[0]
    if algorithm_name == 'UCS':
        output = UCS(Problem(problem)).run()
    if algorithm_name == "ASTAR":
        output = AStar(Problem(problem)).run()
    if algorithm_name == "IDS":
        output = IDS(Problem(problem), 20).run()
    if algorithm_name == "IDASTAR":
        output = IDAStar(Problem(problem)).run()
    write_output(output)


# The main function
if __name__ == "__main__":
    run_requested_algorithm(problem=read_file("input.txt"))
    run_requested_algorithm(problem=read_file("input2.txt"))
    run_requested_algorithm(problem=read_file("input3.txt"))
    run_requested_algorithm(problem=read_file("input4.txt"))
