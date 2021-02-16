from random import shuffle

genes = "I use a genetic algorithm to solve an optimization problem"


class Individual():

    def __init__(self):
        self.genes = genes
        self.genes = self.shuffle_str(self.genes)
        fitness = 0

    def getFitness(self):
        list_correctG = list(genes)
        list_genes = list(self.genes)

        numWrong = 0
        for i in range(len(list_correctG)):
            if (list_correctG[i] != list_genes[i]):
                numWrong += 1
        self.fitness = numWrong / len(list_correctG)
        return self.fitness  # ratio fitness

    def shuffle_str(self, genes):
        str_list = list(genes)
        shuffle(str_list)
        return "".join(str_list)


class Iteration():
    def __init__(self, number_individual, selection_rate):
        ind = [Individual() for i in range(number_individual)]
        # sort ind
        for i in range(len(ind)):
            ind[i].getFitness()
        ind.sort(key=lambda data: data.fitness, reverse=True)

        print(len(genes)/2)
        print(int(len(genes)/2))
        print(genes[0: 29])
        print(genes[0: int(len(genes)/2)])



        # TODO: use selection_rate to select the first (selection_rate*len(ind)) of the population
        # print(ind[0])
        # print(ind[0].getFitness())
        # print(ind[0].genes)
        # print(selection_rate)
        # print(ind[0].fitness)

    # TODO: crossover function
    def crossover(self, parent1=Individual(), parent2=Individual()):
        parent1.genes[0: len(genes)/2]
        pass



    # TODO: mutation function
    def mutation(self):
        pass


if __name__ == "__main__":
    ite = Iteration(500, 0.5)
