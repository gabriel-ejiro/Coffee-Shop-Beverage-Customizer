def main():
   
    beverage = Espresso()
    print(f"Base: {beverage.get_description()} = ${beverage.cost():.2f}")

    beverage = Milk(beverage)

    beverage = Caramel(beverage)

    beverage = Whip(beverage)
    

    print(f"Final Order: {beverage.get_description()} = ${beverage.cost():.2f}")

main()
