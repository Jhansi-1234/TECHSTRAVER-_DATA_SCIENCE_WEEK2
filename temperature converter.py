import tkinter as tk
from tkinter import Label, Entry, Button, OptionMenu

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        temperature = float(entry_temp.get())
        if conversion_var.get() == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature} Celsius = {result:.2f} Fahrenheit")
        elif conversion_var.get() == "Fahrenheit to Celsius":
            result = fahrenheit_to_celsius(temperature)
            result_label.config(text=f"{temperature} Fahrenheit = {result:.2f} Celsius")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Create the main tkinter window
root = tk.Tk()
root.title("Temperature Converter")

# Labels and entry for temperature input
Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = Entry(root, width=50)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

# OptionMenu for temperature conversion direction
conversion_var = tk.StringVar(root)
conversion_var.set("Celsius to Fahrenheit")
conversion_menu = OptionMenu(root, conversion_var, "Celsius to Fahrenheit", "Fahrenheit to Celsius")
conversion_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Button to trigger conversion
convert_button = Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Label to display result
result_label = Label(root, text="", padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
