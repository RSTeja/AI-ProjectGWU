import sys
import heapq

# define the water pitcher problem class
class WaterPitcherProblem:
    def _init_(self, p1_size, p2_size, target):
        self.p1_size = p1_size
        self.p2_size = p2_size
        self.target = target
        self.start = (0, 0)
        
    def get_successors(self, state):
        p1, p2 = state
        successors = []
        # pour from p1 to p2
        if p1 > 0 and p2 < self.p2_size:
            new_p2 = min(p2 + p1, self.p2_size)
            new_p1 = p1 - (new_p2 - p2)
            successors.append(((new_p1, new_p2), 1))
        # pour from p2 to p1
        if p2 > 0 and p1 < self.p1_size:
            new_p1 = min(p1 + p2, self.p1_size)
            new_p2 = p2 - (new_p1 - p1)
            successors.append(((new_p1, new_p2), 1))
        # empty p1
        if p1 > 0:
            successors.append(((0, p2), 1))
        # empty p2
        if p2 > 0:
            successors.append(((p1, 0), 1))
        return successors
    
    def heuristic(self, state):
        p1, p2 = state
        return abs(self.target - p1) + abs(self.target - p2)

# define the A* search function
def a_star_search(problem):
    frontier = []
    heapq.heappush(frontier, (problem.heuristic(problem.start), problem.start, []))
    explored = set()
    while frontier:
        print('Frontier size:', len(frontier))
        _, state, path = heapq.heappop(frontier)
        if state in explored:
            continue
        if state[0] == problem.target or state[1] == problem.target:
            return path + [state]
        explored.add(state)
        for successor, cost in problem.get_successors(state):
            new_path = path + [state]
            heapq.heappush(frontier, (len(new_path) + problem.heuristic(successor), successor, new_path))
    return None

if __name__ == '_main_':
    # read the file name from command line arguments
    file_name = sys.argv[1]

    # solve the water pitcher problem
    with open(file_name, 'r') as f:
        p1_size, p2_size, target = map(int, f.readline().split())
    problem = WaterPitcherProblem(p1_size, p2_size, target)
    solution = a_star_search(problem)
    if solution:
        print('Solution found:')
        for state in solution:
            print(state)
    else:
        print('No solution found')
