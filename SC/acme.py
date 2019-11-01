"""Imported to use random numbers"""
import random


class Product:
    """A method to initialize teh default values of products"""
    def __init__(self, name="", price=10, weight=20, flammability=0.5,
                 identifier=round(random.uniform(1000000, 9999999), 0)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Method for determing that chances a item can be stolen"""
        chance_of_steal = (self.price/self.weight)
        if (chance_of_steal < 0.5):
            return "Not so stealable..."
        if (chance_of_steal < 1.0) & (chance_of_steal >= 0.5):
            return "kinda stealable"
        else:
            return "Very Stealable!"

    def explode(self):
        """Method for determining the chances an item will explode"""
        chance_of_explode = (self.flammability*self.weight)
        if (chance_of_explode < 10):
            return "...fizzle"
        if (chance_of_explode >= 10) & (chance_of_explode < 50):
            return "...boom!"
        else:
            return "...BABOOM!"


class BoxingGlove(Product):
    """Boxing glove subclass that wont explode, but will punch instead"""
    def __init__(self, name="", price=10, weight=10, flammability=0.5,
                 identifier=round(random.uniform(1000000, 9999999))):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        """Over riding the parent method to return a different value"""
        return "...its a glove"

    def punch(self):
        """Method to punch, with values dependant on weight"""
        if (self.weight < 5):
            return "That tickles."
        if (self.weight >= 5) & (self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH"
