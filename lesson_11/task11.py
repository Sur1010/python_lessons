# 1
with open("db.txt" , "r+") as file:
    users = []
    for i , line in enumerate(file):
        if i == 0:
            keys = line.strip().split(',')
        else:                             
            users.append(line.strip().split(','))

list_of_users = []
for user in users:
    users_dict = {}
    for key , value in enumerate(user):
        users_dict[keys[key]] = value
    list_of_users.append(users_dict)

print(list_of_users)
                                                  
# ---- 1.2 ----                    
def new_values(list_of_users, **kwargs):
    for user in list_of_users:
        for new_key , new_value in kwargs.items():
            user[new_key] = new_value


    return list_of_users
  
print(new_values(list_of_users , height = "170" , weight = "75"))

# 2
numbers = [[[[[10]]]]]

def get_number(n):
    if type(n) == int:
        print(n)
    else:
        get_number(n[0])

get_number(numbers)

# 3
numbers  = [1, 2, [3, 4], [5, 6, [10, 19]]]
def get_sum_of_list(n):
    count = 0
    for x in range(len(n)):
        if type(n[x]) == list:
            count = count + get_sum_of_list(n[x])
        else:
            count = count + n[x]

    return count 

print(get_sum_of_list(numbers))   

# ---- Research ----
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Example
x = lambda a : a + 10
print(x(5))