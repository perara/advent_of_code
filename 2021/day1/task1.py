"""
1. Create a function named "read_advent_code" that reads a file with name "./task1_data.txt" of integers.
2. Create a variable with the name measurement from calling read_advent_code
3. loop over measurements and increment counter by 1 if current is greater than previous.
"""


def read_advent_code():
    with open("./task1_data.txt", "r") as f:
        return [int(line) for line in f]


measurement = read_advent_code()
counter = 0
for i in range(len(measurement) - 1):
    if measurement[i] < measurement[i + 1]:
        counter += 1

print(counter)