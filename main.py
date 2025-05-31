def main():
   
    beverage = Espresso()
    print(f"Base: {beverage.get_description()} = ${beverage.cost():.2f}")

    beverage = Milk(beverage)

    beverage = Caramel(beverage)

    beverage = Whip(beverage)
    

    print(f"Final Order: {beverage.get_description()} = ${beverage.cost():.2f}")

main()


def main():
    menu = Menu()
    menu.display_menu()
    
    # Example Order: Large Cappuccino with Milk, Caramel, and Chocolate
    beverage = Cappuccino(size='large')
    beverage = Milk(beverage)
    beverage = Caramel(beverage)
    beverage = Chocolate(beverage)
    
    print("\n🧾 Final Order Summary")
    print(f"Description: {beverage.get_description()}")
    print(f"Total Cost: ${beverage.cost():.2f}")
    print(f"Total Calories: {beverage.calories()} kcal")

main()

