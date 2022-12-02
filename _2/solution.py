def read_file():
    input = open('_2/input.txt', 'r')
    return input.readlines()
   

def problem_1():
    lines = read_file()
    total_points = 0
    for l in lines:
        total_points += calculate_points_1(l[0], l[2])
    print(f'Total points: {total_points}')

def calculate_points_1(opp, you):
    points = 0
    if opp == 'A' and you == 'X' or opp == 'B' and you == 'Y' or opp == 'C' and you =='Z':
        points += 3
    elif opp == 'A' and you == 'Y' or opp == 'C' and you == 'X' or opp == 'B' and you == 'Z':
        points += 6
    points += get_bonus(you)
    return points

def get_bonus(you):
    if you == 'X':
        return 1
    elif you == 'Y':
        return 2
    else:
        return 3    

def problem_2():
    lines = read_file()
    total_points = 0
    for l in lines:
        total_points += calculate_points_2(l[0], l[2])
    print(f'Total points: {total_points}')

def calculate_points_2(opp, result):
    points = 0
    if result == 'Y':
        # draw
        points += 3
    elif result == 'Z':
        # win
        points += 6
    points += get_bonus(calculate_hand(opp,result))
    return points

def calculate_hand(opp, result):
    if opp == 'A' and result == 'Y' or opp == 'B' and result == 'X' or opp == 'C' and result =='Z':
        return 'X'
    elif opp == 'A' and result == 'Z' or opp == 'B' and result == 'Y' or opp == 'C' and result == 'X':
        return 'Y'
    else:
        return 'Z'


problem_2()
problem_2()