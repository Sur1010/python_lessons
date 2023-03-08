# 1
# generatory hishoxutyan mej aveli qich tex e zbaxecnum ev amen angam kancheluc hertov veradracnum e bolor element-nery   

# 2
# ete function-i mej return-i poxaren yield e grvac uremn function generator e 

# 3
def Fibonacci():
    num_1 = 1
    num_2 = 1
   
    while True:
        yield num_1
        num = num_1
        num_1 = num_2
        num_2 = num + num_1

number = int(input("Number "))
fib_num = Fibonacci()
for i in range(number):
    print(next(fib_num))

# 4
def my_range(start,stop,step = 1):
    start = int(start)
    stop = int(stop)
    step = int(step)
    while start < stop:
        yield start
        start += step 
        
for i in my_range(0,10,2):
    print(i)

# 5
any_str = input("write any strings ")
new_str = ""
for x in any_str[::-1]:
    new_str += x
if any_str == new_str:
    print("string is a palindrome")
else:
    print("string is not a palindrome")    

# 6
def is_palindrome(any_str):
    new_str = ""
    for x in any_str[::-1]:
        new_str += x
    if any_str == new_str:
        return True
    else:
        return False

x = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']
y = {i:is_palindrome(i) for i in x}
print(y)

# ---- Research ----
# __iter__() veradarcnum e iterator object, vorn ancnum e object-i bolor element-neri vrayov
# iterable data types (List, Strings, Tuple, Dict)
# sequence data types (List, Strings, Tuple)
# sequence data typery iterable en bayc voch bolor iterablenern en sequence 