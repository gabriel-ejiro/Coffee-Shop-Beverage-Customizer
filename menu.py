class Menu:
    def __init__(self):
        self.base_drinks = ['Espresso', 'Tea', 'Cappuccino']
        self.sizes = ['Small', 'Medium', 'Large']
        self.condiments = ['Milk', 'Caramel', 'Whip', 'Chocolate']
    
    def display_menu(self):
        print("📋 Coffee Shop Menu")
        print("Base Beverages:")
        for drink in self.base_drinks:
            print(f" - {drink}")
        print("\nSizes:")
        for size in self.sizes:
            print(f" - {size}")
        print("\nCondiments:")
        for condiment in self.condiments:
            print(f" - {condiment}")
