import tkinter as tk
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('house_prices.csv')

# Select features and target
X = data[['sqft_living', 'grade']]
y = data['price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Create a GUI
class HousePricePredictorGUI:
    def __init__(self, master):
        self.master = master
        master.title("House Price Predictor")

        # Create input fields for square footage and grade
        self.sqft_label = tk.Label(master, text="Square Footage:")
        self.sqft_label.grid(row=0, column=0)
        self.sqft_entry = tk.Entry(master)
        self.sqft_entry.grid(row=0, column=1)

        self.grade_label = tk.Label(master, text="Grade:")
        self.grade_label.grid(row=1, column=0)
        self.grade_entry = tk.Entry(master)
        self.grade_entry.grid(row=1, column=1)

        # Create button to predict house price
        self.predict_button = tk.Button(master, text="Predict Price", command=self.predict_price)
        self.predict_button.grid(row=2, column=0, columnspan=2)

        # Create label to display predicted house price
        self.price_label = tk.Label(master, text="")
        self.price_label.grid(row=3, column=0, columnspan=2)

    def predict_price(self):
        # Get input values from user
        sqft = float(self.sqft_entry.get())
        grade = int(self.grade_entry.get())

        # Make a prediction using the trained model
        price = model.predict([[sqft, grade]])

        # Update the price label
        self.price_label.configure(text="Predicted Price: $%.2f" % price)

root = tk.Tk()
my_gui = HousePricePredictorGUI(root)
root.mainloop()
