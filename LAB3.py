import random
import math

class GeneticAlgo:
    def __init__(self,problem,goal):
        self.problem=problem
        self.goal=goal
        self.population=None
        self.maxFitness=-math.inf
        self.score=0
        self.generation=1
        self.iterationThreshold=200
        self.populationSize=16
        self.fittestIndividual=False

    def run(self):
        self.population=[[random.randint(0,1) for j in range(len(self.problem))] for i in
                           range(self.populationSize)]

        while self.generation<self.iterationThreshold:
            self.__select()
            if self.fittestIndividual:
                print([self.problem[i][0] for i in range(len(self.problem))])
                print(f"FITTEST COMBO: {self.fittestIndividual}")
                return

            l, r = 0, len(self.population) - 1
            while l < r:
                offsprings = self.__crossover(
                    self.population[l], self.population[r])
                self.population[l], self.population[r]=offsprings[0], offsprings[1]
                l +=1
                r -=1

            self.__mutate()
            self.generation += 1
        print([self.problem[i][0] for i in range(len(self.problem))])
        print(f"FAILURE: {-1}")

    def __select(self):
        fitness_list = self.__fitness()
        population_based_on_fitness = [i for _, i in sorted(zip(fitness_list, self.population))]
        population_based_on_fitness.reverse()
        self.population = population_based_on_fitness

    def __crossover(self, p1, p2):
        new_chromosome_set = [[], []]
        start = random.randint(0, len(p1) // 2)
        end = start + len(p1) // 2
        for i in range(len(p1)):
            if start <= i < end:
                new_chromosome_set[0].append(p1[i])
                new_chromosome_set[1].append(p2[i])
            else:
                new_chromosome_set[0].append(p2[i])
                new_chromosome_set[1].append(p1[i])

        return new_chromosome_set

    def __mutate(self):
        mutation_indices = [random.randint(0, len(self.population) - 1) for _ in range(2)]
        for index in mutation_indices:
            mutation_spot = random.randint(0, len(self.problem) - 1)
            self.population[index][mutation_spot]=1 if self.population[index][mutation_spot] == 0 else 0

    def __fitness(self):
        fitnessList = []
        xd = [0] * len(self.problem)
        for chromosome in self.population:
            if chromosome != xd:
                totalRun = 0
                for i in range(len(chromosome)):
                    totalRun += chromosome[i]*self.problem[i][1]
                if totalRun == 0:
                    print(chromosome)
                    self.maxFitness=math.inf
                    self.fittestIndividual=chromosome
                    fitnessList.append(math.inf)
                else:
                    try:
                        fitnessList.append(1/totalRun)
                    except Exception:
                        fitnessList.append(9999999999999999999)
            else:
                fitnessList.append(9999999999999)
        return fitnessList

def PROBTARGET():
    n = int(input())
    target = 0
    info1 = []
    for _ in range(n):
        info2, amount = input().split()
        if info2 == 'l':
            info1.append((info2, int(amount)))
        elif info2 == 'd':
            info1.append((info2,-1 * int(amount)))
    print(info1)
    return info1, target


problem, target = PROBTARGET()
genetic_algorithm = GeneticAlgo(problem, target)
genetic_algorithm.run()



# /Users/aviroy/PycharmProjects/CSE422/venv/bin/python /Users/aviroy/PycharmProjects/CSE422/lab3.py
# 7
# l 120
# l 289
# d 475
# l 195
# d 6482
# l 160
# d 935
# [('l', 120), ('l', 289), ('d', -475), ('l', 195), ('d', -6482), ('l', 160), ('d', -935)]
# [1, 0, 1, 1, 0, 1, 0]
# ['l', 'l', 'd', 'l', 'd', 'l', 'd']
# FITTEST COMBO: [1, 0, 1, 1, 0, 1, 0]