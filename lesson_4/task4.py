# 2
x = [1,2,5, [8,9,10]]
y = x.copy()
z = x[3]
n = z[:]
y[3] = n
x[3][0]= 5

print(x)
print(y)

# 3
days_tuple = ('Erk','Ereq','Choreq','Hing','Urb',['Shb'])
days_tuple[5].append('kiraki')
print(days_tuple)

# 4
t1 = 'My name' , 'My last name' , 'My father name'
name, last_name, patronymic = t1
print(t1)
print(name , last_name , patronymic)

# 5
users_tuple = ("Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza")
users_tuple = list(users_tuple)
users_tuple[0] = "Ani"
users_tuple = tuple(users_tuple)
print(users_tuple)

# 6
users_list = [
        "Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
        [[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]]
]
only_useres = users_list[0],users_list[1],users_list[2],users_list[3],users_list[4],users_list[5],users_list[6]
num1 = tuple(users_list[7][0])
num2 = tuple(users_list[7][1])
num3 = tuple(users_list[7][2])

users_zip = zip(only_useres , num1 , num2 , num3)

print(list(users_zip))
