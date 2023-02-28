def digits(number):
    number = int(number)
    initial_number = 0 
    while number:
        if number > 0 :
            initial_number = initial_number + (number % 10)
            number = (number // 10 )
    return initial_number