class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = 0
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}'
        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}'

    def get_animals_count(self):
        return self.__animals

zoo = Zoo(input())
n = int(input())

for i in range(n):
    species, name = input().split(' ')

    zoo.add_animal(species, name)


species_required = input()

print(zoo.get_info(species_required))
print(f'Total animals: {zoo.get_animals_count()}')