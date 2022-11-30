# Q5_graded
import numpy as np

class ACO:
    def __init__(self, time_matrix):
        self.time_matrix = time_matrix
        self.pheromone = np.zeros(self.time_matrix.shape) / len(time_matrix)
        self.job_num = len(time_matrix)
        self.ant_num = 100
        self.epsillon = 0.001
        self.decay = 0.99

    def create_paths(self):
        generation_path = []
        for _ in range(self.ant_num):
            path = self.find_path()
            generation_path.append((path, sum([self.time_matrix[edge] for edge in path])))
        return generation_path

    def find_path(self):
        path = []
        visited = []
        visited.append(0)
        prev = 0
        for i in range(len(self.time_matrix) - 1):
            next = self.next_step(self.pheromone[prev], self.time_matrix[prev], visited)
            path.append((prev, next))
            prev = next
            if next not in visited:
                visited.append(next)
        path.append((prev, 0)) 
        return path

    def next_step(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[visited] = 0
        row = (pheromone * ((1.0 / dist)) + self.epsillon)
        p = row / row.sum()
        next = np.random.choice(range(self.job_num), 1, p=p)[0]
        return next

def print_path(path):
    if path != "None":
        path_sequence = "0 "
        for item in path:
            path_sequence += f"-> {item[1]} "
        return path_sequence

time_matrix = np.array([[7, 4, 7, 5, 2, 15],
                        [1, 5, 3, 8, 14, 3],
                        [2, 7, 5, 1, 9, 11],
                        [3, 11, 5, 6, 8, 2],
                        [5, 8, 2, 9, 1, 4],
                        [15, 2, 7, 3, 9, 5]])

ant_colony = ACO(time_matrix)
best_shortest_path = ("None", np.inf)

for i in range(10):
    generation_path = ant_colony.create_paths()
    shortest_path = min(generation_path, key=lambda x: x[1])
    print("the shortest path of generation = ", print_path(best_shortest_path[0]))
    print(f"The best execution time of generation {i + 1} = {best_shortest_path[1]}")
    print("---------------------------------")
    if shortest_path[1] < best_shortest_path[1]:
        best_shortest_path = shortest_path
    ant_colony.pheromone = ant_colony.pheromone * ant_colony.decay

print("===========================================")
print("The best results : ")
print("The shortest path = ", print_path(best_shortest_path[0]))
print("The best execution time = ", best_shortest_path[1])

