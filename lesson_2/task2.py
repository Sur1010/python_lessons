# 1
print(type(1 + 2.0 + 3))

# 2
print(2 * (3 + 4))

# 3
print(round(2.555 , 2))

# 4
my_string = "Hello World"
x = my_string[0:5]
y = my_string[6:]
print(y , x)

# 5
text1 = "simply"
text2 = 1500
text3 = "galley"

print("Lorem Ipsum is %s dummy text of the printing and typesetting industry." 
"Lorem Ipsum has been the industry's standard dummy text ever since the %ds, "
"when an unknown printer took a %s of type and scrambled it to make a type specimen book."%(text1 , text2 , text3))

print("Lorem Ipsum is {0} dummy text of the printing and typesetting industry." 
"Lorem Ipsum has been the industry's standard dummy text ever since the {1}s, "
"when an unknown printer took a {2} of type and scrambled it to make a type specimen book.".format(text1 , text2 , text3))

print(f"Lorem Ipsum is {text1} dummy text of the printing and typesetting industry." 
f"Lorem Ipsum has been the industry's standard dummy text ever since the {text2}s, "
f"when an unknown printer took a {text3} of type and scrambled it to make a type specimen book.")

# 6
x = 97
y = x % 10
z = (x - y) // 10
print(y , z)

# 7
num = 123
num1 = num % 10 
num2 = (num - num1) // 10 
num3 = num2 % 10 
num4 = (num2 - num3) // 10 
num_sum = num1 + num3 + num4
print(num_sum)
