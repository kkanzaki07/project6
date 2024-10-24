import random
import tkinter as tk

class WeightedRNG:
    def __init__(self, items_with_weights):
        self.items = []
        self.cumulative_weights = []
        total_weight = 0

        # Convert items and weights into cumulative distribution
        for item, weight in items_with_weights:
            total_weight += weight
            self.items.append(item)
            self.cumulative_weights.append(total_weight)

        self.total_weight = total_weight

    def get_random_item(self):
        # Generate a random number between 0 and total_weight
        rand_num = random.uniform(0, self.total_weight)

        # Find where this random number falls within the cumulative weights
        for i, cum_weight in enumerate(self.cumulative_weights):
            if rand_num <= cum_weight:
                return self.items[i]

rarities = [
        ("Common", 80),  # 80% chance
        ("Uncommon", 10),  # 10% chance
        ("Rare", 5),  # 5% chance
        ("Epic", 4),  # 4% chance
        ("Legendary", 2), #2% chance
        ("Mythical", 1) #1% chance
    ]

rng = WeightedRNG(rarities)

inventory = {
    "Common": 0,
    "Uncommon": 0,
    "Rare": 0,
    "Epic": 0,
    "Legendary": 0,
    "Mythical": 0
}

def spin():
    result = rng.get_random_item()  # Get a random rarity
    inventory[result] += 1  # Update inventory count for the pulled item
    display_roll.config(text=f"{result}")  # Update the label with the result
    update_inventory()  # Refresh inventory display

def update_inventory():
    inventory_text = ""
    for rarity, count in inventory.items():
        inventory_text += f"{rarity}: {count}\n"
    inventory_label.config(text=inventory_text)  # Update inventory label


window = tk.Tk()
window.title("Tkinter RNG")
window.geometry('800x400')


inventory_label = tk.Label(window, text="Inventory:")
inventory_label.grid(row=0, column=0, padx=10, pady=10)

title = tk.Label(window, text="Roll some Rarities!", font=("Arial", 16, "bold"))
title.grid(row=0, column=1, padx=220, pady=10)

display_roll = tk.Label(window, font=("Arial", 30, "bold"))
display_roll.grid(row=1, column=1, padx=220, pady=10)

roll = tk.Button(window, text="ROLL", height=1, width=20, command=spin)
roll.grid(row=2, column=1, padx=220, pady=10)

update_inventory()

window.mainloop()

