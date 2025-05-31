class Espresso(Beverage):
    def get_description(self):
        return f"Espresso ({self.size.capitalize()})"
    
    def cost(self):
        base_cost = 2.0
        return base_cost * self.get_size_multiplier()

class Tea(Beverage):
    def get_description(self):
        return f"Tea ({self.size.capitalize()})"
    
    def cost(self):
        base_cost = 1.5
        return base_cost * self.get_size_multiplier()

class Cappuccino(Beverage):
    def get_description(self):
        return f"Cappuccino ({self.size.capitalize()})"
    
    def cost(self):
        base_cost = 3.0
        return base_cost * self.get_size_multiplier()
