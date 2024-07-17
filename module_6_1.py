class Animal:# РОДИТЕЛЬСКИЙ
    def __init__(self, name):
        self.alive = True  # Живой по умолчанию
        self.fed = False   # Не накормлен по умолчанию
        self.name = name   # Индивидуальное название каждого животного

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def eat(self, food: Plant):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            food.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
            return

class Predator(Animal):
    def eat(self, food: Plant):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            food.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
            return


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True
class Flower(Plant):
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(p1.edible)
print(p2.edible)
