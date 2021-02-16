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
            if (list_correctG[i] == list_genes[i]):
                numCorrect += 1
        self.fitness = numCorrect / len(list_correctG)
        return self.fitness  # ratio fitness

    def shuffle_str(self, genes):
        str_list = list(genes)
        shuffle(str_list)
        return "".join(str_list)


class Iteration():
    def __init__(self, number_individual, selection_rate):
        ind = [Individual(genes) for i in range(number_individual)]
        # sort ind
        for i in range(len(ind)):
            ind[i].shuffleGenes()
            ind[i].getFitness()
            # print(ind[i].genes)
        ind.sort(key=lambda data: data.fitness, reverse=True)

        for i in range(len(ind)):
            print(ind[i].genes)
            print(ind[i].fitness)


        # TODO: use selection_rate to select the first (selection_rate*len(ind)) of the population
        ind = ind[0:int(len(ind)*selection_rate)]

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for i in range(len(ind)):
            print(ind[i].fitness)


        self.crossover(ind[0], ind[1])




        # print(ind[0])
        # print(ind[0].getFitness())
        # print(ind[0].genes)
        # print(selection_rate)
        # print(ind[0].fitness)

    def crossover(self, parent1, parent2):
        newGenes1 = parent1.genes[0: int(len(genes)/2)] + parent2.genes[int(len(genes)/2):len(genes)]
        newGenes2 = parent2.genes[0: int(len(genes)/2)] + parent1.genes[int(len(genes)/2):len(genes)]
        children = Individual(newGenes1), Individual(newGenes2)
        return children



    # TODO: mutation function
    def mutation(self):
        pass


if __name__ == "__main__":
    ite = Iteration(500, 0.5)
