# 1
def Contacts(name, last_name, age):
    age = int(age) 
    print(f'hello my name is {name}, my last name is {last_name}, I am {age} years old:')

Contacts("Vardan" , "Vardanyan" , 20)

# 2
def change_the_letter(text, old_character, new_chararcter):
    new_text = " "
    for x in text:
        if x == old_character:
            x = new_chararcter
        new_text = new_text + x 

    return new_text

print(change_the_letter(text = " " , old_character=" " , new_chararcter= " "))

# 3
def creat_a_file(list_of_texts , file_name = "text.txt"):
    with open(file_name , "w+") as file:
        file.write(list_of_texts)

creat_a_file(list_of_texts="Hello World")

# 4
def Prime_number(number):
    number = int(number)
    if number > 1:
        for x in range(2, number):
            if number % x == 0:
                print(f"number {number} is not prime")
                break
        else:
            print(f"number {number} is prime")

    else:
        print(f"number {number} is not prime")        

Prime_number(number = 7)

# ---- Research ----
def f1(x , y):
    """ calculates the sum of x and y """
    return x + y 

help(f1)




                




      

    

