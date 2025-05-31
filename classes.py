class Espresso(Beverage):
    def get_description(self):
        return "Espresso"
    
    def cost(self):
        return 2.0

class Tea(Beverage):
    def get_description(self):
        return "Tea"
    
    def cost(self):
        return 1.5

class Cappuccino(Beverage):
    def get_description(self):
        return "Cappuccino"
    
    def cost(self):
        return 3.0
