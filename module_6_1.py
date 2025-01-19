class Animal():
    def __init__(self, name:str):
        self.alive = True
        self.fed = False
        self.name = name

class Plant():
    def __init__(self, name:str):
        self.name = name
        
class Mammal(Animal): 
    def eat(self,food):
        Plant.self = food
        if food.edible == True:
            self.fed = True
            return print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            return print(f'{self.name} не стал есть {food.name}')

class Predator(Animal):
    def eat(self,food):
        Plant.self = food
        if food.edible == True:
            self.fed = False
            self.alive = False
            return print(f'{self.name} съел {food.name}')    
        else:
            self.fed = False
            self.alive = False
            return print(f'{self.name} не стал есть {food.name}')
    
class Flower(Plant):
    edible = False
    pass
   
class Fruit(Plant):
    edible = True
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
print(a1.alive)
print(a2.fed)
    
