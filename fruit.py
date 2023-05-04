class Fruit:
    def __init__(self,edible,flavor,nutrition):
     self.edible=edible
     self.flavor=flavor
     self.nutrition=nutrition
    def best_fruit(self):
     return f"{self.edible},fruit has the best {self.flavor} which adds {self.nutrition} to our bodies"
    