import random
import matplotlib.pyplot as plt
import numpy as np


class Person:
    def __init__(self):
        self.luck = random.randint(0, 100)
        self.skill = random.randint(0, 100)

    def worth(self):
        return self.luck * 0.1 + self.skill * 0.9


persons = [Person() for _ in range(100000)]
persons.sort(key=lambda x: x.worth(), reverse=True)

top_1_percent = persons[:1000]
luck_values = [person.luck for person in top_1_percent]

# Calculate mean and standard deviation of luck values
luck_mean = np.mean(luck_values)
luck_std = np.std(luck_values)

# Print mean and standard deviation
print(f"Luck Mean: {luck_mean:.2f}")
print(f"STD Luck: {luck_std:.2f}")

## show but I am using fucking WSL so I can't
# plt.plot(range(1, len(luck_values) + 1), luck_values)
# plt.title("Top 10% luck Distribution")
# plt.xlabel("Rank")
# plt.ylabel("Luck")
# plt.grid(True)
# plt.show()
