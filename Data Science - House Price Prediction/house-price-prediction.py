import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import tkinter as tk

class HousePricePredictor:
    def __init__(self, master):
        self.master = master
        master.title("House Price Predictor")

        self.beds_label = tk.Label(master, text="Number of Bedrooms:")
        self.beds_label.grid(row=0, column=0)
        self.beds_entry = tk.Entry(master)
        self.beds_entry.grid(row=0, column=1)

        self.baths_label = tk.Label(master, text="Number of Bathrooms:")
        self.baths_label.grid(row=1, column=0)
        self.baths_entry = tk.Entry(master)
        self.baths_entry.grid(row=1, column=1)

        self.sqft_label = tk.Label(master, text="Square Footage:")
        self.sqft_label.grid(row=2, column=0)
        self.sqft_entry = tk.Entry(master)
        self.sqft_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(master, text="Predict Price", command=self.predict_price)
        self.submit_button.grid(row=3, column=1)

        self.price_label = tk.Label(master, text="")
        self.price_label.grid(row=4, column=0, columnspan=2)

        self.model = LinearRegression()
        self.df = pd.read_csv("house_prices.csv")

        X = self.df[['bedrooms', 'bathrooms', 'sqft_living']]
        y = self.df['price']
        self.model.fit(X, y)

    def predict_price(self):
        bedrooms = float(self.beds_entry.get())
        bathrooms = float(self.baths_entry.get())
        sqft_living = float(self.sqft_entry.get())

        price = self.model.predict([[bedrooms, bathrooms, sqft_living]])

        self.price_label.config(text="Predicted Price: ${:,.2f}".format(price[0]))

root = tk.Tk()
my_predictor = HousePricePredictor(root)
root.mainloop()
