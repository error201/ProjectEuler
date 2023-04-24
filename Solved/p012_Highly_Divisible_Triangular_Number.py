#!/usr/bin/python

import euler as eu

if __name__ == '__main__':
    seed = 10082
    tri = eu.n_gonal_number(3, seed)
    while True:
        num_facts = len(eu.big_factors(tri))
        print("{0} : {1} : {2}".format(str(seed), str(tri), str(num_facts)))
        if num_facts >= 500:
            break
        seed += 1
        tri += seed
