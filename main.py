import heapq
class Project:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.parent = None
        self.cost = 0
    def __lt__(self, other):
        return self.cost < other.cost
    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2
    def __hash__(self):
        return hash((self.p1, self.p2))

def get_neighbors(state, max1, max2):
    neighbors = []
    neighbors.append(Project(0, state.p2))
    neighbors.append(Project(state.p1, 0))
    neighbors.append(Project(max1, state.p2))
    neighbors.append(Project(state.p1, max2))
    transfer = min(state.p1, max2 - state.p2)
    neighbors.append(Project(state.p1 - transfer, state.p2 + transfer))
    transfer = min(state.p2, max1 - state.p1)
    neighbors.append(Project(state.p1 + transfer, state.p2 - transfer))
    return neighbors

def heuristic(state, goal):
    return abs(state.p1 - goal.p1) + abs(state.p2 - goal.p2)

def A_star(start, goal, max1, max2):
    frontier = []
    heapq.heappush(frontier, start)
    visited = set()
    steps = 0
    while frontier:
        state = heapq.heappop(frontier)
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = state.parent
            return path[::-1], steps
        visited.add(state)
        for neighbor in get_neighbors(state, max1, max2):
            if neighbor in visited:
                continue
            neighbor.cost = state.cost + 1
            neighbor.parent = state
            neighbor_cost = neighbor.cost + heuristic(neighbor, goal)
            heapq.heappush(frontier, neighbor)
            steps += 1

    return None, steps
with open('input.txt', 'r') as file:
    max1, max2 = map(int, file.readline().split())
    goal1, goal2 = map(int, file.readline().split())

start = Project(0, 0)
goal = Project(goal1, goal2)

path, steps = A_star(start, goal, max1, max2)

if path:
    for state in path:
        print(f'{state.p1} {state.p2}')
    print(f'Count:{steps - 8}')
else:
    print('No solution')
