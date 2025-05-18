import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10132313)
print(f"Random number: {random_number}")

ramdom_list = [random.randint(1, 100) for i in range(10)]
print(f"Random list: {ramdom_list}")

colors = ["red", "blue", "green", "yellow", "purple"]
random_color = random.choice(colors)
print(f"Random color: {random_color}")

# Barajar una lista de cartas
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)
print(f"Shuffled cards: {cards}")