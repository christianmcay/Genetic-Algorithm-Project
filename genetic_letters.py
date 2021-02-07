gene_set = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?\'":;,.'
target = input('What word would you like the computer to make\n')

import random
import datetime


def display(guess):
    time_diff = datetime.datetime.now() - start_time
    fitness = get_fitness(guess)
    print(f'{guess}, {fitness}, {time_diff}')


def generate_parent(length):
    genes = []  # empty to take in values from gene set

    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sample_size))
        # random imported to create sample extending the gene set and size parameters
        # list.extend appends multiple items to a list
        # list.join creates a new string with values joined

    return ''.join(genes)
    # returns the genes into a formatted string


def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)


"""  
fitness for this genetic algorithm is total number of letters in the guess
that match the letter in the same position of the target defined

zip functions allows iteration over two lists at the same time
"""


def mutate(parent):
    index = random.randrange(0, len(parent))
    child_genes = list(parent)
    new_gene, alternate = random.sample(gene_set, 2)
    child_genes[index] = alternate \
        if new_gene == child_genes[index] \
        else new_gene
    return ''.join(child_genes)


random.seed()
start_time = datetime.datetime.now()
best_parent = generate_parent(len(target))
best_fitness = get_fitness(best_parent)
display(best_parent)

while True:
    child = mutate(best_parent)
    child_fitness = get_fitness(child)
    if best_fitness >= child_fitness:
        continue
    display(child)
    if child_fitness >= len(best_parent):
        break
    best_fitness = child_fitness
    best_parent = child
