📘 Domain Story

A coffee shop offers various base beverages such as espresso, cappuccino, and tea.
Customers can add custom ingredients like milk, soy, caramel, whipped cream, or chocolate.
Each additional ingredient affects the total cost and description.
Instead of creating subclasses for every combination, your task is to implement a decorator-based system where additional features (toppings) can be dynamically "wrapped" around base drinks.



📋 Functional Requirements

   - Implement a base Beverage interface with methods get_description() and cost().

   - Create concrete classes like Espresso, Tea, Cappuccino.

   - Create decorators like Milk, Caramel, Whip, etc., that wrap beverages and modify behavior.
 
   - Compose decorated beverages dynamically in a main() method.

   - Print description and total cost.


 Possible Extensions
 
 - Add calorie count for each decorator and display total calories.

 - Introduce support for sizes (small, medium, large) and adjust prices accordingly.

 -  Implement a Menu class that dynamically generates available options.

 - Build a simple GUI or web app version using Flask or Tkinter.
