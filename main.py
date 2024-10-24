import random
import tkinter as tk

class WeightedRNG:
    def __init__(self, items_with_weights):
        # Initialize the WeightedRNG class with a list of items and their corresponding weights
        self.items = []  # List to hold the items
        self.cumulative_weights = []  # List to hold cumulative weights
        total_weight = 0  # Variable to track the total weight

        # Convert items and weights into a cumulative distribution
        for item, weight in items_with_weights:
            total_weight += weight  # Increment total weight by the current item's weight
            self.items.append(item)  # Add the item to the items list
            self.cumulative_weights.append(total_weight)  # Add the cumulative weight

        self.total_weight = total_weight  # Store the total weight

    def get_random_item(self):
        # Generate a random number between 0 and the total weight
        rand_num = random.uniform(0, self.total_weight)

        # Determine which item corresponds to the random number based on cumulative weights
        for i, cum_weight in enumerate(self.cumulative_weights):
            if rand_num <= cum_weight:  # Check if the random number is less than or equal to the cumulative weight
                return self.items[i]  # Return the corresponding item

# Define a list of rarities with their respective weights
rarities = [
    ("Common", 80),  # 80% chance
    ("Uncommon", 10),  # 10% chance
    ("Rare", 5),  # 5% chance
    ("Epic", 4),  # 4% chance
    ("Legendary", 2),  # 2% chance
    ("Mythical", 1)  # 1% chance
]

# Create an instance of WeightedRNG with the defined rarities
rng = WeightedRNG(rarities)

# Initialize an inventory dictionary to keep track of item counts
inventory = {
    "Common": 0,
    "Uncommon": 0,
    "Rare": 0,
    "Epic": 0,
    "Legendary": 0,
    "Mythical": 0
}

def spin():
    # Function to simulate a spin and update inventory
    result = rng.get_random_item()  # Get a random rarity from the RNG
    inventory[result] += 1  # Increment the inventory count for the pulled item
    display_roll.config(text=f"{result}")  # Update the label with the result of the spin
    update_inventory()  # Refresh the inventory display

def update_inventory():
    # Function to update the inventory display on the GUI
    inventory_text = ""  # Initialize an empty string to hold inventory text
    for rarity, count in inventory.items():
        inventory_text += f"{rarity}: {count}\n"  # Append each rarity and its count to the text
    inventory_label.config(text=inventory_text)  # Update the inventory label with the new text

# Create the main window for the Tkinter application
window = tk.Tk()
window.title("Tkinter RNG")  # Set the window title
window.geometry('800x400')  # Set the window size

# Create and place the inventory label on the grid
inventory_label = tk.Label(window, text="Inventory:")
inventory_label.grid(row=0, column=0, padx=10, pady=10)

# Create and place the title label on the grid
title = tk.Label(window, text="Roll some Rarities!", font=("Arial", 16, "bold"))
title.grid(row=0, column=1, padx=220, pady=10)

# Create and place the display label for the result of the spin
display_roll = tk.Label(window, font=("Arial", 30, "bold"))
display_roll.grid(row=1, column=1, padx=220, pady=10)

# Create and place the roll button that triggers the spin function
roll = tk.Button(window, text="ROLL", height=1, width=20, command=spin)
roll.grid(row=2, column=1, padx=220, pady=10)

update_inventory()  # Initial call to display the inventory

# Start the Tkinter event loop to run the application
window.mainloop()