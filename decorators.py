
class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

class Milk(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Milk"
    
    def cost(self):
        return self._beverage.cost() + 0.5

class Caramel(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Caramel"
    
    def cost(self):
        return self._beverage.cost() + 0.7

class Whip(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Whip"
    
    def cost(self):
        return self._beverage.cost() + 0.6

class Chocolate(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Chocolate"
    
    def cost(self):
        return self._beverage.cost() + 0.8
