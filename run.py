from math import gcd
import scipy.optimize
import numpy as np
from functools import lru_cache
import click


@lru_cache
def get_suitability_score(street, name):
    # Note: This method only handles english names. Doesn't handle non-roman characters
    if name.endswith('I') or name.endswith('X') or name.endswith('V'):
        # roman numerals shouldn't count as vowels
        name = name.rsplit(' ', 1)[0]
    num_vowels = len([c for c in name.lower() if c in 'aeiou'])
    if len(street) % 2 == 0:
        # street is even
        score = num_vowels * 1.5
    else:
        score = len(name) - num_vowels

    if gcd(len(street), len(name)) > 1:
        score *= 1.5
    return score


@click.command()
@click.option('--drivers', default='drivers.txt')
@click.option('--routes', default='routes.txt')
def run(drivers, routes):
    with open(drivers, 'r') as df:
        drivers = [l.strip() for l in df.readlines()]

    with open(routes, 'r') as rf:
        routes = [l.strip() for l in rf.readlines()]

    scores = []
    for i, address in enumerate(routes):
        scores.append([])

        # Note: This isn't a very accurate way to get the street name.
        #  Ideally a geolocation database should be used. But since this is a test exercise and
        #  will possibly be ran with fake data/test data, it will not do that currently.
        number, street_name = address.split(',', 1)[0].split(' ', 1)

        for name in drivers:
            scores[i].append(get_suitability_score(street_name, name))

    grid = np.array(scores)
    result_rows, result_cols = scipy.optimize.linear_sum_assignment(grid)
    final_results = {n: 0 for n in sorted(drivers)}
    total = 0
    for index, matrix_i in enumerate(result_rows):
        matrix_j = result_cols[index]
        total += grid[matrix_i][matrix_j]
        final_results[drivers[matrix_j]] = routes[matrix_i]

    for name, route in final_results.items():
        print(f'{name}: {route}')

    print('Total SS:', total)


if __name__ == '__main__':
    run()

