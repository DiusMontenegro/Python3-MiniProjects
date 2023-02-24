#import tkinter and math modules
import tkinter as tk
import math

#Calculator class definition
class Calculator:
    # initialization function
    def __init__(self, master):
        # initialize the master window and title
        self.master = master
    master.title("Scientific Calculator")

    # create an entry widget for the calculator display
    self.display = tk.Entry(master, width=30, borderwidth=5)
    self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    # create the number and operator buttons for the calculator
    self.create_button("1", 1, 0)
    self.create_button("2", 1, 1)
    self.create_button("3", 1, 2)
    self.create_button("4", 2, 0)
    self.create_button("5", 2, 1)
    self.create_button("6", 2, 2)
    self.create_button("7", 3, 0)
    self.create_button("8", 3, 1)
    self.create_button("9", 3, 2)
    self.create_button("0", 4, 1)
    self.create_button("+", 1, 3)
    self.create_button("-", 2, 3)
    self.create_button("*", 3, 3)
    self.create_button("/", 4, 3)
    self.create_button("C", 4, 0)
    self.create_button("=", 5, 2)

    # create the trigonometric, logarithmic, and exponential function buttons for the calculator
    self.create_button("sin", 1, 4)
    self.create_button("cos", 2, 4)
    self.create_button("tan", 3, 4)
    self.create_button("log", 4, 4)
    self.create_button("exp", 5, 4)

    # create the pi and e constant buttons for the calculator
    self.create_button("pi", 1, 5)
    self.create_button("e", 2, 5)

# function to create calculator buttons
def create_button(self, text, row, col):
    button = tk.Button(self.master, text=text, padx=40, pady=20,
                       command=lambda: self.button_click(text))
    button.grid(row=row, column=col)

# function to handle button click events
def button_click(self, text):
    # if C button is pressed, clear the calculator display
    if text == "C":
        self.display.delete(0, tk.END)
    # if = button is pressed, evaluate the expression and display the result
    elif text == "=":
        try:
            # replace pi and e constants in the expression with their respective values
            expr = self.display.get().replace('pi', str(math.pi)).replace('e', str(math.e))
            # evaluate the expression using Python's built-in eval function
            result = eval(expr)
            # clear the calculator display and insert the result
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        # catch any exceptions that occur during evaluation and display an error message
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
    # if trigonometric, logarithmic, or exponential function button is pressed, evaluate the expression and display the result
    elif text in ["sin", "cos", "tan", "log", "exp"]:
        try:
            # replace pi and e constants in the expression with their respective values
