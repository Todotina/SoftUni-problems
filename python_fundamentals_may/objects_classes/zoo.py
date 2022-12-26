class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fish)}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"
        return f"Total animals: {Zoo.__animals}"

name = input()
zoo = Zoo(name)
number = int(input())
for animal in range(number):
    animal_info = input().split(" ")
    species = animal_info[0]
    name = animal_info[1]
    zoo.add_animal(species, name)

animal = input()
print(zoo.get_info(animal))
print(f"Total animals: {number}")