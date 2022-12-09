import string
max_calories = []

with open('day1_input.txt') as file:
    current_calories = 0
    for line in file.readlines():
        line = line.strip()
        if line == '':
            max_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)

print("Part 1 Solution", max(max_calories))

max_calories = sorted(max_calories)

print("Part 2 Solution", max_calories[-1] + max_calories[-2] + max_calories[-3])