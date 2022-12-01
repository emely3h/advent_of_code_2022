input = open('_1/input.txt', 'r')
lines = input.readlines()

most_calories = 0

current_most_calories = 0
for line in lines:
    if line.strip():
        current_most_calories = current_most_calories + int(line)
    else:
        if current_most_calories > most_calories:
            most_calories = current_most_calories
        current_most_calories = 0

print('Most calories')
print(most_calories) 
    