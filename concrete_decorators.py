class Milk(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Milk"
    
    def cost(self):
        return self._beverage.cost() + 0.5
    
    def calories(self):
        return self._beverage.calories() + 50 if hasattr(self._beverage, 'calories') else 50

class Caramel(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Caramel"
    
    def cost(self):
        return self._beverage.cost() + 0.7
    
    def calories(self):
        return self._beverage.calories() + 80 if hasattr(self._beverage, 'calories') else 80

class Whip(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Whip"
    
    def cost(self):
        return self._beverage.cost() + 0.6
    
    def calories(self):
        return self._beverage.calories() + 60 if hasattr(self._beverage, 'calories') else 60

class Chocolate(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Chocolate"
    
    def cost(self):
        return self._beverage.cost() + 0.8
    
    def calories(self):
        return self._beverage.calories() + 100 if hasattr(self._beverage, 'calories') else 100
