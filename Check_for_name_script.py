name = ['MESHAL', 'MESHO', 'MESH', 'MSHOO']
user_name = input('type your name --> ')
user_name.capitalize()
age = [30]

for my_age in age:
    if my_age <= 35:
        print('your age under 35')
    elif my_age > 35:
        print('your age above 35')
    else:
        print('your age is not any of my record ')

for my_name in name:
    if user_name in name:
        print(f'your name {user_name} is good to go ')
    else:
        print(f'your name {user_name} is not good ')

    break
