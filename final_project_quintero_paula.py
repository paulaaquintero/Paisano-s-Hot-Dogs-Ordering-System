# final project
# author: pq
# created: 2024-09-17
# create a gui application for Paisano's Hot Dogs ordering system
# include three labels and three buttons


# import tkinter
import tkinter as tk
from tkinter import messagebox

# Function used in order to validate the order
def validate_order():
    if not drink_var.get() or not hotdog_var.get():
        messagebox.showerror("Input Error", "Please select a hot dog combo and a drink")
        return False
    return True

# Function for order submission
def submit_order():
    if validate_order():
        confirmation_window()


# Function used for the confirmation window
def confirmation_window():
    confirm_win = tk.Toplevel(root)
    confirm_win.title("Order Confirmation")
    
    lbl_confirm = tk.Label(confirm_win, text=f"Order Confirmed!\nHot Dog: {hotdog_var.get()}\nDrink: {drink_var.get()}\nToppings: {', '.join([var.get() for var in toppings_vars if var.get()])}")
    lbl_confirm.pack()

    btn_exit = tk.Button(confirm_win, text="Exit", command=exit_app)
    btn_exit.pack()

# Function to exit the application
def exit_app():
    root.quit()




# Main window
root = tk.Tk()
root.title("Paisano's Hot Dogs")



# Labels
label1 = tk.Label(root, text="Hot Dog Order Form")
label1.pack()

# Hot Dog Options 
hotdog_var = tk.StringVar()
tk.Radiobutton(root, text="2 Hot Dogs + Soda ($8)", variable=hotdog_var, value="2 Hot Dogs").pack()
tk.Radiobutton(root, text="Jumbo Hot Dog + Soda ($8)", variable=hotdog_var, value="Jumbo Hot Dog").pack()
tk.Radiobutton(root, text="Kielbasa Sausage + Soda ($10)", variable=hotdog_var, value="Kielbasa Sausage").pack()
tk.Radiobutton(root, text="Spicy Sausage + Soda ($6)", variable=hotdog_var, value="Spicy Sausage").pack()



# Toppings Options
toppings_label = tk.Label(root, text="Choose Toppings:")
toppings_label.pack()

toppings = ["Relish", "Sauerkraut", "Onions", "Corn", "Mozzarella Cheese", "Pineapple", "Potato Chips", "Ketchup", "Mustard", "Mayo", "Pink Sauce"]
toppings_vars = [tk.StringVar(value="") for _ in toppings]
for i, topping in enumerate(toppings):
    tk.Checkbutton(root, text=topping, variable=toppings_vars[i], onvalue=topping, offvalue="").pack()

# Drink Options
drink_var = tk.StringVar()
drink_label = tk.Label(root, text="Choose a drink:")
drink_label.pack()

tk.Radiobutton(root, text="Pepsi", variable=drink_var, value="Pepsi").pack()
tk.Radiobutton(root, text="Coke", variable=drink_var, value="Coke").pack()



# Buttons
btn_submit = tk.Button(root, text="Submit Order", command=submit_order)
btn_submit.pack()

btn_exit = tk.Button(root, text="Exit", command=exit_app)
btn_exit.pack()

# Run the application
root.mainloop()
