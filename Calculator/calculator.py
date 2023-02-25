import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

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

        self.create_button("sin", 1, 4)
        self.create_button("cos", 2, 4)
        self.create_button("tan", 3, 4)
        self.create_button("log", 4, 4)
        self.create_button("exp", 5, 4)

        self.create_button("pi", 1, 5)
        self.create_button("e", 2, 5)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=40, pady=20,
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                expr = self.display.get().replace('pi', str(math.pi)).replace('e', str(math.e))
                result = eval(expr)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text in ["sin", "cos", "tan", "log", "exp"]:
            try:
                expr = self.display.get().replace('pi', str(math.pi)).replace('e', str(math.e))
                if text == "sin":
                    result = math.sin(eval(expr))
                elif text == "cos":
                    result = math.cos(eval(expr))
                elif text == "tan":
                    result = math.tan(eval(expr))
                elif text == "log":
                    result = math.log10(eval(expr))
                elif text == "exp":
                    result = math.exp(eval(expr))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()

