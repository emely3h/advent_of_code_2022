input = open('_1/input.txt', 'r')
lines = input.readlines()

most_calories = 0
second_most_calories = 0
third_most_calories = 0

current_most_calories = 0
for line in lines:
    if line.strip():
        current_most_calories = current_most_calories + int(line)
    else:
        if current_most_calories >= most_calories:
            third_most_calories = second_most_calories
            second_most_calories = most_calories
            most_calories = current_most_calories
        elif current_most_calories >= second_most_calories:
            third_most_calories = second_most_calories
            second_most_calories = current_most_calories
        elif current_most_calories >= third_most_calories:
            third_most_calories = current_most_calories
        current_most_calories = 0

print(f'Most calories: {most_calories}')
print(f'Second ost calories: {second_most_calories}')
print(f'Third most calories: {third_most_calories}')
print(f'Total amount of calories: {third_most_calories + second_most_calories + most_calories}') 
    