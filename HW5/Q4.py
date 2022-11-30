# Q4_graded
import random
import numpy as np
  
class Ant(object): 
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        
    def fitness(self):
        chromosome_string = self.chromosome
        
        left = int(chromosome_string[1:9],2)
        right = int(chromosome_string[9:],2)

        x = left + (right / (10 ** len(str(right))))

        if chromosome_string[0] == "1":
            x *= -1

        return x, abs((168*(x**3))-(7.22*(x**2))+(15.5*x)-13.2)

    
    def cross_over(self, parent2):

        left = list(self.chromosome)
        right = list(parent2.chromosome)
        
        left_boundry = random.randint(0,63)
        numbers = list(range(0, 64))
        numbers.remove(left_boundry) 
        right_boundry = random.choice(numbers)      
    
        temp = left
        left[min(left_boundry, right_boundry):max(left_boundry, right_boundry)] = temp[min(left_boundry, right_boundry):max(left_boundry, right_boundry)]
        right[min(left_boundry, right_boundry):max(left_boundry, right_boundry)] = left[min(left_boundry, right_boundry):max(left_boundry, right_boundry)]

        child1 = mutation(right)
        child2 = mutation(left)
        child1 = "".join(child1)
        child2 = "".join(child2)
        return Ant(child1) , Ant(child2)
  

def initilize_chromosome(): 
    chromosome = ''

    p = np.random.uniform(0, 1, 64)

    for i in range(64):
        if p[i] > 0.5:
            chromosome += '1'
        else:
            chromosome += '0'

    return chromosome


def mutation(chromosome): 
    r = np.random.uniform(0, 1, 64)

    for i in range(64):
        if r[i] < 0.01:
            if chromosome[i] == "0":
                chromosome[i] = "1"
            else:
                chromosome[i] = "0"

    return chromosome


def training():   
    generation = 0
    Ants = [] 
    number_of_population = 300


    for i in range(number_of_population): 
        Ants.append(Ant(initilize_chromosome())) 


    for i in range(500):

        generation += 1

        Ants = sorted(Ants, key = lambda x:x.fitness()[1]) 

        best_fitness = Ants[0].fitness()

        if ((i + 1) % 10 == 0):
            print(f"generation {i + 1} : best fitness = {best_fitness[1]}")

        if best_fitness[1] < 0.001:
            return best_fitness[0]

        else :
            children = [] 
    
            p = int(number_of_population*0.2)
            if p % 2 != 0:
                children.extend(Ants[:p+1])
                remaining_chromosome = int((number_of_population - int(number_of_population*0.2) - 1)/2)
            else:
                children.extend(Ants[:p]) 
                remaining_chromosome = int((number_of_population - int(number_of_population*0.2))/2)
            for i in range(remaining_chromosome): 
                parent1 = random.choice(Ants[:int(number_of_population*0.8)]) 
                parent2 = random.choice(Ants[:int(number_of_population*0.8)]) 
                child1, child2 = parent1.cross_over(parent2) 
                children.append(child1) 
                children.append(child2) 
    
            Ants = children 
    return Ants[0].fitness()[0]
    

    
x = training()
print("Answer = ", x)

