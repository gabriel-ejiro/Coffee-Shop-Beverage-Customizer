import tkinter as tk
from tkinter import messagebox

def launch_gui():
    # Tkinter Window
    root = tk.Tk()
    root.title("Coffee Shop Beverage Customizer")
    root.geometry("400x500")
    
    # Menu Options
    base_options = {'Espresso': Espresso, 'Tea': Tea, 'Cappuccino': Cappuccino}
    size_options = ['Small', 'Medium', 'Large']
    condiment_options = {'Milk': Milk, 'Caramel': Caramel, 'Whip': Whip, 'Chocolate': Chocolate}
    
    # User Selections
    selected_base = tk.StringVar(value='Espresso')
    selected_size = tk.StringVar(value='Medium')
    selected_toppings = {}
    
    # Functions
    def update_order():
        base_class = base_options[selected_base.get()]
        beverage = base_class(size=selected_size.get().lower())
        for topping, var in selected_toppings.items():
            if var.get():
                decorator_class = condiment_options[topping]
                beverage = decorator_class(beverage)
        
        # Update summary
        summary_text = (
            f"Description: {beverage.get_description()}\n"
            f"Total Cost: ${beverage.cost():.2f}\n"
            f"Total Calories: {beverage.calories()} kcal"
        )
        summary_label.config(text=summary_text)
    
    # Widgets
    tk.Label(root, text="Select Base Beverage").pack()
    for name in base_options:
        tk.Radiobutton(root, text=name, variable=selected_base, value=name, command=update_order).pack(anchor='w')
    
    tk.Label(root, text="Select Size").pack()
    for size in size_options:
        tk.Radiobutton(root, text=size, variable=selected_size, value=size, command=update_order).pack(anchor='w')
    
    tk.Label(root, text="Select Toppings").pack()
    for topping in condiment_options:
        var = tk.BooleanVar()
        selected_toppings[topping] = var
        tk.Checkbutton(root, text=topping, variable=var, command=update_order).pack(anchor='w')
    
    summary_label = tk.Label(root, text="Description:\nTotal Cost:\nTotal Calories:")
    summary_label.pack(pady=20)
    
    # Initialize display
    update_order()
    
    root.mainloop()

launch_gui()
