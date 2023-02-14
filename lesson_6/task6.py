
# 1
x = {1,2,4,5,6}
y = {5,6,7,8,9}

# ---- 1.1 ----
print(y.intersection(x))

# ---- 1.2 ----
print(x.difference(y))

# 2
x = {1,2,4,5,6}
y = {5,6,7,8,9}

x.difference_update(y)
print("x =",x)
print("y =",y)

# 3
# open()  -->  default read


# 4
# ---- 4.1 ----
file_1 = "Python_Set.txt"
f_1 = open(file_1 , "w+")
f_1.write("Sets are used to store multiple items in a single variable. ")
print(f_1.read())
f_1.close()

file_2 = "Python_Files.txt"
f_2 = open(file_2 , "w+")
f_2.write("File handling is an important part of any web application. ")
print(f_2.read())
f_2.close()

# ---- 4.2 ----
with open("Python_Set.txt" , "r+") as f_1:
    f_1.read()
    f_1.write("Set is one of 4 built-in data types in Python.")

with open("Python_Files.txt" , "r+") as f_2:
    f_2.read()
    f_2.write("Python has several functions for creating, reading, updating, and deleting files.")

# ---- 4.3 ----
file_name = input('which file do you want to read?')
with open(file_name , "r") as f:
    file_name = f.read()
    print(file_name)

# 5
users = [
            {
            'first_name': 'Jorj',
            'last_name' : 'Bush',
            'age':55
            },

            {
            'first_name': 'James',
            'last_name' : 'Bond',
            'age':100
             }
    ]
user_1 = users[0]
user_2 = users[1]
x = user_1.items()
x = list(x)
y = user_2.items()
y = list(y)
user_1 = f"user 1: {x[0][0]} = {x[0][1]}, {x[1][0]} = {x[1][1]}, {x[2][0]} = {x[2][1]}"
user_2 = f"user 2: {y[0][0]} = {y[0][1]}, {y[1][0]} = {y[1][1]}, {y[2][0]} = {y[2][1]}"

file_path = "File_Users.txt"
with open(file_path , "w+") as f:
    f.write(f'{user_1}\n')
    f.write(user_2)
    print(f.read())
