# 1
users_list = ['Vardan', 'Vazgen', 'Jarviz']

# ---- 1.1 ----
print(users_list)

# ---- 1.2 ----
new_users_list = users_list
new_users_list[1] = "Aram"

print(new_users_list)

# 2
x = [1,2,3,4,5,6]
z = [7,8,9,10,11]

print(len(x+z))

# 4
first_input = int(input("how many words do you want to type?"))
second_input = input("write a word")

print(first_input * second_input)

# 5
users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
old_users_list = users_list[:]
new_name = input("Name ?")
users_list.append(new_name)
print(old_users_list , users_list)

# 6
users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
del_user = input(f'Your users.{users_list} who do you want to remove ?')
x = users_list.remove(del_user)
print(f'User {del_user.upper()} is removed')
print(f'Your users {users_list}')

# 7
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list = numbers_list[1::2]
print(sum(numbers_list))


