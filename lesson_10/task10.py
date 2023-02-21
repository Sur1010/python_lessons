# 1
my_name = "name"
def f1():
    global my_name
    my_name = "My real name"

f1()
print(my_name)

# 2
users = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Luiza", "Janna", "Armen", "Lilit"]
long_word = 'dzaynaskavarakavacharanoc'
last_names = ("Watson", "Richards", "Richardson", "Saunders", "Watson", "Young", "Saunders")           

def recurring_members(sequence_object):
    result = {}
    duplicate = []
    for x in sequence_object:
        if x not in result:
            result[x] = 0
        else:
            result[x] = result[x] + 1
    for key,value in result.items():
        if value > 0:
            duplicate.append(key)
    return duplicate 

print(recurring_members(sequence_object = users))

# 3
def sum_of_digits(number):
    number = int(number)
    initial_number = 0 
    while number:
        if number > 0 :
            initial_number = initial_number + (number % 10)
            number = (number // 10 )
    return initial_number

print(sum_of_digits(123))

# 4
def prime_numbers(number):
    list_of_prime_numbers = []
    for x in range(2, number + 1):
        for y in range(2, number + 1):
            if x % y == 0:
                break
        if x == y:
            list_of_prime_numbers.append(x)
    return list_of_prime_numbers

print(prime_numbers(number = 100))    

# 5
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(4))

# ---- Research ----
# 1. If you do not know how many arguments that will be passed into your function, add a *args before the parameter name in the function definition.
# Example
def my_function1(*args):
  print("This phone is " + args[1] + " in color")

my_function1("black", "red", "green")

# 2. If you do not know how many keyword arguments that will be passed into your function, add two asterisk: **kwargs before the parameter name in the function definition.
# Example
def my_function2(**kwargs):
  print("My name is " + kwargs["name_1"])

my_function2(name_1 = "Vardan" , name_2 = "Hayk")