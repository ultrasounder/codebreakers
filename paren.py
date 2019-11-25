opening = '('

# def is_balanced(parantheses):
#     stack = [] # initialize stack; constrcutor in Java
#     for paren in parantheses:
#         if paren == opening:
#             stack.append(paren)
#         else:
#             try:
#                 stack.pop()
#             except IndexError:
#                 return False
#     return len(stack) == 0

# print(is_balanced('((()))'))

PAIRINGS = {
    '(':')',
    '{':'}',
    '[':']'
}

def is_balanced(parantheses):
    stack = []#initialize an empty stack
    for paren in parantheses:
        if paren == PAIRINGS:
            stack.append(paren)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:
            return False
        if paren != PAIRINGS[expected_opening_symbol]:
            return False
    return len(stack) == 0#reached the end of the stack and no more parens to process

print(is_balanced('{{([][])}()})'))
print(is_balanced('{[]))'))
print(is_balanced('((()))')) 
        
    

