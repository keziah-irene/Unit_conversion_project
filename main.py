# Dep number - 24/PCSA/106 KEZIAH IRENE A 
# Title of project - UNIVERSAL UNIT CONVERSION
# two files - main.py, conversions.py

import tkinter as tk
from tkinter import ttk, messagebox
from conversions import length, mass, temperature, speed, time, data

# Function to update the unit options upon user selection of category
def update_units(*args): 
    category = category_var.get()
    if category == 'Length':
        from_menu['values'] = ['Kilometer', 'Meter','Centimeter', 'Millimeter', 'Foot', 'Inch']
        to_menu['values'] = ['Kilometer', 'Meter','Centimeter', 'Millimeter', 'Foot', 'Inch']
    elif category == 'Mass':
        from_menu['values'] = ['Kilograms', 'Grams','Milligrams', 'Pounds', 'Ounce']
        to_menu['values'] = ['Kilograms', 'Grams','Milligrams', 'Pounds', 'Ounce']
    elif category == 'Temperature':
        from_menu['values'] = ['Celsius', 'Fahrenheit', 'Kelvin']
        to_menu['values'] = ['Celsius', 'Fahrenheit', 'Kelvin']
    elif category == 'Speed':
        from_menu['values'] = ['Meter per second', 'Kilometer per hour', 'Kilometer per second', 'Miles per hour']
        to_menu['values'] = ['Meter per second', 'Kilometer per hour', 'Kilometer per second', 'Miles per hour']
    elif category == 'Time':
        from_menu['values'] = ['Year', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds', 'Milliseconds']
        to_menu['values'] = ['Year', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds', 'Milliseconds']
    elif category == 'Data':
        from_menu['values'] = ['Terabyte', 'Gigabyte', 'Megabyte', 'Kilobyte', 'Byte']
        to_menu['values'] = ['Terabyte', 'Gigabyte', 'Megabyte', 'Kilobyte', 'Byte']
    else:
        from_menu['values'] = []
        to_menu['values'] = []

# Function to perform error handling
def validation(value):   
    # for all categories to take only positive and decimals
    if category_var.get() != 'Temperature':
        if value == "":
            return False
        if value.isdigit() or (value.count('.') == 1 and all(char.isdigit() or char == '.' for char in value)):
            return True 
        return False
    
    # for temperature validation to take all positive, negative and decimals
    else:
        if value == "":
            return False
        if (value.isdigit() or 
            (len(value) > 1 and value[0] == '-' and value[1:].count('.') <= 1 and all(char.isdigit() or char == '.' for char in value[1:])) or 
            (value[0] == '.' and all(char.isdigit() for char in value[1:])) or 
            (value.count('.') == 1 and all(char.isdigit() or char == '.' for char in value))):
            return True  
        return False

# Function to perform conversion
def convert_units():
    from_value = input_from.get()
    # Validating input before conversion
    if not validation(from_value):
        messagebox.showerror("Error", "Invalid input. Please enter a number")
        return  # Stops further execution
    # Getting all 4 inputs
    from_value = float(from_value)
    category = category_var.get()
    from_unit = from_menu.get()
    to_unit = to_menu.get()

    # Perform conversion by function call and passing arguments
    if category == 'Length':
        result = length(from_value, from_unit, to_unit)
    elif category == 'Mass':
        result = mass(from_value, from_unit, to_unit)
    elif category == 'Temperature':
        result = temperature(from_value, from_unit, to_unit)
    elif category == 'Speed':
        result = speed(from_value, from_unit, to_unit)
    elif category == 'Time':
        result = time(from_value, from_unit, to_unit)
    elif category == 'Data':
        result = data(from_value, from_unit, to_unit)
    else:
        result = "Unknown Category"

    result_label.config(text=f"Result - {from_value} {from_unit} to {to_unit} = {result}")

# Tkinter window setup
root = tk.Tk()
root.title("Unit Converter")
root.configure(bg="#e0f7fa") 
root.geometry("500x500")
# Border for the units
border_width = 2
border_color = "black"
border_frame = tk.Frame(root, bg="#b2ebf2", highlightthickness=border_width, highlightbackground=border_color)
border_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

# Category label and dropdown
category_label = tk.Label(border_frame, text="Category:", bg="#b2ebf2") 
category_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
category_var = tk.StringVar()
category_menu = ttk.Combobox(border_frame, textvariable=category_var) 
category_menu['values'] = ['Length', 'Mass', 'Temperature', 'Speed', 'Time', 'Data']
category_menu.grid(row=1, column=2, padx=20, pady=10, sticky="e")
category_menu.bind('<<ComboboxSelected>>', update_units)

# From and to unit labels
from_label = tk.Label(border_frame, text="From:", bg="#b2ebf2") 
from_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
from_menu = ttk.Combobox(border_frame)
from_menu.grid(row=2, column=2, padx=20, pady=10, sticky="e")

to_label = tk.Label(border_frame, text="To:", bg="#b2ebf2") 
to_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
to_menu = ttk.Combobox(border_frame)
to_menu.grid(row=3, column=2, padx=20, pady=10, sticky="e")

# Input value label
input_label = tk.Label(border_frame, text="Value:", bg="#b2ebf2")
input_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
input_from = tk.Entry(border_frame)
input_from.grid(row=4, column=2, padx=20, pady=10, sticky="e")

# Submit button
submit_button = tk.Button(border_frame, text="Convert", command=convert_units, bg="green", fg="white")
submit_button.grid(row=5, column=1, pady=10, sticky="ew")

# Result label
result_label = tk.Label(root, text="Result: ", fg="blue", justify="left", bg="#e0f7fa") 
result_label.grid(row=1, column=0, rowspan=5, padx=20, pady=10, sticky="w")

root.mainloop()
