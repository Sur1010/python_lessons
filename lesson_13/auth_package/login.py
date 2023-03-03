with open("users.txt" , "r+") as f:
    users = []
    for i , line in enumerate(f):
        if i == 0:
            keys = line.strip().split(',')
        else:                             
            users.append(line.strip().split(','))

email = input("write your email address ")
password = input("write your password ")
    
for user in users:
    if email in user:
        if password in user:
            print(f"Hello {user[2]} {user[3]}")
            break
else:
     raise Exception('wrong email or password')