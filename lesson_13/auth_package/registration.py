with open("users.txt" , "r+") as f:
    users = []
    for i , line in enumerate(f):
        if i == 0:
            keys = line.strip().split(',')
        else:                             
            users.append(line.strip().split(','))

email = input("write your email address ")
password = input("write your password ")
first_name = input("write your first name ")
last_name = input("write your last name ")

for user in users:
    if email in user:
        raise Exception('that email address already exists')
          
new_users = []          
new_users.append(email)
new_users.append(password)
new_users.append(first_name)
new_users.append(last_name)   

u = ",".join(new_users)

with open('users.txt', 'a+') as file:
    file.write(u)