import random
from random import shuffle

genes = "I use a genetic algorithm to solve an optimization problem"


class Individual():

    def __init__(self, genes):
        self.genes = genes

    def shuffleGenes(self):
        self.genes = self.shuffle_str(self.genes)

    def getFitness(self):
        list_correctG = list(genes)
        list_genes = list(self.genes)

        numCorrect = 0
        for i in range(len(list_correctG)):
            if list_correctG[i] == list_genes[i]:
                numCorrect += 1
        self.fitness = numCorrect / len(list_correctG)
        return self.fitness  # ratio fitness

    def shuffle_str(self, genes):
        str_list = list(genes)
        shuffle(str_list)
        return "".join(str_list)


class Iteration():
    def __init__(self, ind, selection_rate):

        # sort ind
        for i in range(len(ind)):
            ind[i].getFitness()

        # use selection_rate to select the first (selection_rate*len(ind)) of the population
        ind.sort(key=lambda data: data.fitness, reverse=True)
        ind = ind[0:int(len(ind) * selection_rate)]

        pop = len(ind)
        for i in range(pop - 1):
            children = self.crossover(ind[i], ind[i + 1])
            for j in range(len(children)):
                self.mutation(children[j], 0.1)
                children[j].getFitness
                ind.extend(children)
        print(ind[0].getFitness())


    def crossover(self, parent1, parent2):
        newGenes1 = parent1.genes[0: int(len(genes) / 2)] + parent2.genes[int(len(genes) / 2):len(genes)]
        newGenes2 = parent2.genes[0: int(len(genes) / 2)] + parent1.genes[int(len(genes) / 2):len(genes)]
        children = [Individual(newGenes1), Individual(newGenes2)]
        return children

    # mutation function
    def mutation(self, child, mutation_rate):
        if random.randint(0, 1000000) <= mutation_rate * 1000000:
            a = random.randint(0, len(genes) - 1)
            b = random.randint(0, len(genes) - 1)
            list_ChildG = list(child.genes)
            list_G = list(genes)
            list_ChildG[a] = list_G[b]
            child.genes = "".join(list_ChildG)
            return child.genes


if __name__ == "__main__":
    number_individual = 500
    ind = [Individual(genes) for i in range(number_individual)]

    for i in range(len(ind)):
        ind[i].shuffleGenes()

    for i in range(20):
        ite = Iteration(ind, 0.5)
print("-----------------------final-----------------------")
print(len(ind))
print("++++++++++++++++++++++++++++++++++++++++++++")
print(ind[0].getFitness())
