"""
1. Create a function named "counting" that input a list and loop over a list and increments counter by 1 if current is greater than previous.
2. Create a function name "sliding_window" that computes the sum of the sliding window.
3. Create a function named "read_advent_code" that reads a file with name "./task2_data.txt" of integers.
4. Create a variable with the name measurement from calling read_advent_code.
5. Create a variable with the name "sliding_windows" from calling sliding_window with the measurement and window_size=3.
6. Create a variable with the name result from calling counting with the sliding_windows
"""


def counting(lst):
    counter = 0
    for i in range(len(lst)):
        if lst[i] > lst[i-1]:
            counter += 1
    return counter


def sliding_window(lst, window_size):
    result = []
    for i in range(len(lst) - window_size + 1):
        result.append(sum(lst[i:i+window_size]))
    return result


def read_advent_code():
    with open("./task2_data.txt", "r") as f:
        measurement = [int(line) for line in f]
    return measurement


measurement = read_advent_code()
sliding_windows = sliding_window(measurement, 3)
result = counting(sliding_windows)
print(result)