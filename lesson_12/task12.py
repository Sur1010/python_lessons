import prime_numbers
from my_package import sum_of_digits
# 1
# help("modules")

# 2
# You don't know exactly what is imported and can't easily find from which module a certain thing was imported (readability).

# 3
# The __init__.py files are required to make Python treat directories containing the file as packages. 
# This prevents directories with a common name, such as string , unintentionally hiding valid modules that occur later on the module search path.

# 4
# It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module. 
# For most practical purposes, you can think of the conditional block that you open with if __name__ == "__main__" as a way to store code that should only run when your file is executed as a script.

# 5
# get_users.py

# 6
print(prime_numbers.is_prime(5))

# 7
print(sum_of_digits.digits(123))

