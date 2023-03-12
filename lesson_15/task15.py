from functools import reduce 
# 1
def is_palindrome(any_str):
    new_str = ""
    for x in any_str[::-1]:
        new_str += x
    if any_str == new_str:
        return True
    else:
        return False

any_list = ['abcba', 'abcbca', 'abcbt', '121', '123454321', '5551555']

filtered = filter(is_palindrome ,any_list)
print(list(filtered))

# 2
def my_map(func, *iterable):
    mapped =  (func(i) for i in iterable)
    return mapped

# 3
# ---- 3.1 ----
number_list = [1, 2, 5, 70, 4, 8, 50, 44]
max_number = number_list[0]
for i in number_list:
    if i > max_number:
        max_number = i

print(max_number)

# ---- 3.2 ----
number_list = [1, 2, 5, 70, 4, 8, 50, 44,]
print(reduce(max , number_list))