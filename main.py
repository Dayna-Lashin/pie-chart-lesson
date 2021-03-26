# Import matplotlib library here
import matplotlib.pyplot as plt

# Let's rank some of our favorite snacks
snack_scores = [200, 100, 50]
slice_labels = ["Hummus", "Oyster Crackers", "Bananas"]
colors = ["#37123C", "#71677C", "#A99F96"]

# Let's make a pie chart!
plt.pie(snack_scores, labels=slice_labels, colors=colors)

# Give your pie chart a title in the quotes
plt.title("Dayna's Fave Snacks", fontsize=22)

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("my-fave-snacks.png")
