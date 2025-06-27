import random

print("Rolling dice...")

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2

print(f"Die 1: {dice1}")
print(f"Die 2: {dice2}")
print(f"Total value: {total}")
