# This file generates fake data for testing purposes
from faker import Faker
fake = Faker(['en_US'])  # Use only english names


def generate():
    number_of_routes = 10_000
    number_of_drivers = 2_000

    routes = [fake.address().replace('\n', ',') for i in range(number_of_routes)]
    drivers = [fake.name() for i in range(number_of_drivers)]

    with open('drivers.txt', 'w') as f:
        f.writelines('\n'.join(drivers))

    with open('routes.txt', 'w') as f:
        f.writelines('\n'.join(routes))


if __name__ == '__main__':
    generate()
