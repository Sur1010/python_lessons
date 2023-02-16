# 1
last_names = ['Adams','Allen','Brooks','Davidson','Sargsyan','Jenkins',]
armenian_last_names = []
counter = 0 
while counter < len(last_names):
    if last_names[counter][-3:]=="yan":     
        armenian_last_names.append(last_names[counter])
    counter+=1  
print(armenian_last_names)

# 2
long_word = 'arevachachapaylatakum'
count = 0
for word in long_word:
    if word == "a":
        count = count + 1 
print(f"a = {count}") 

# 3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counter = 0
odd_numbers = 1
alphabet_dict = {}
while counter<len(alphabet):
    alphabet_dict[alphabet[counter]] = odd_numbers
    counter = counter + 1
    odd_numbers = odd_numbers + 2
print(alphabet_dict )

# 4
factorial = 1
number = 10
for i in range(1, number + 1):
    factorial = factorial * i 
print(factorial)

# 5
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse_alpabet = []
while alpabet:
    reverse_alpabet.append(alpabet.pop())
print(reverse_alpabet)
        
# ---- Research ----
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
# Example
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))

       
        
    
     







    
       
         
    
   