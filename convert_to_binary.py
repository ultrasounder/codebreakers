def convert_to_binary(decimal_number):
    remainder_stack = []#empty stack to hold the reminders

    while decimal_number > 0:
        remainder = decimal_number % 2 
        remainder_stack.append(remainder)
        decimal_number // 2
    
    binary_digits = [] #create another list to create a strinfg
    while remainder_stack:
        binary_digits.append(str(remainder_stack.pop()))

return ' '.join()
