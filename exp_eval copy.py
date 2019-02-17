## Name: Allie Blaising

from stack_array import * 

# You should not change this Exception class
class PostfixFormatException(Exception): # setting up exception class 
    pass


def precedence(operator): # Function that returns the value associated with an operator; number is used to compare between two operators to 
# determine which should be popped first 
    if operator == ">>" or operator == "<<": 
        return 5 
    elif operator == "**": 
        return 4
    elif operator == "*" or operator == "/": 
        return 3
    elif operator == "+" or operator == "-": 
        return 2 
    elif operator == "(" or operator == ")": 
        return 1 
    else: 
        return 0 


def post_fix_valid(input_str): # Function that checks if each char in input_str is valid, i.e. either a number or pre-defined operator, and  
# returns a corresponding boolean 
    input_str_split = input_str.split()
    valid_operators = ["**", "*", "/", "+", "-", ">>", "<<"] 
    for char in input_str_split: 
        if is_number(char) or char in valid_operators: 
            return True 
        return False 


def math_eval(operator, operant_1, operant_2):  
    try: 
        operant_1 = int(operant_1) # Try converting to an integer, if value error then we know it's a float
        operant_2 = int(operant_2)
    except ValueError: 
        operant_1 = float(operant_1) # Operant 1 and 2 are feed into function as a character strings, but need to be converted before applying math 
        operant_2 = float(operant_2)
    if operator == "*": # Series of conditions checking what the operator feed into the function was, and performing associated 
        # math to the operants 
        return operant_1 * operant_2 # Because we are moving left --> right, e.g. 12 ** -> 1 ** 2, not 2 ** 1, operant_1 represents the first operand, 
            # in the stack; thus, because it's the first and we perform operations left --> right, we will always start with operant_1 as our base 
    elif operator == "/":
        if operant_2 == 0: 
            raise ValueError 
        return operant_1 / operant_2 
    elif operator == "+": 
        return operant_1 + operant_2 
    elif operator == "**": 
        return operant_1 ** operant_2
    elif operator == "-": 
        return operant_1 - operant_2
    elif operator == ">>": 
        return (operant_1 // (2 ** operant_2)) # Equation to convert to bitwise 
    elif operator == "<<": 
        return (operant_1 * (2 ** operant_2)) # Equation to convert to bitwise
    else: 
        raise ValueError



def is_number(n): # Function to check if a number is either a float OR integer using try, except blocks and returning boolean: 
    try:
        float(n)  
    except ValueError:
        return False
    else: 
        return True 



def postfix_eval(input_str):
    if input_str == "":  # Check to make sure that input_str isn't empty; if it is we can't evaluate and need to raise exception
        PostfixFormatException("Insufficent operands") 
    input_str_split = input_str.split()
    valid_operators = ["**", "*", "/", "+", "-", "<<", ">>"] 
    operands = 0 # Initialize variables to keep tally of operands (e.g. 123) and operators (e.g. / **)
    operators = 0 
    for char in input_str_split: # Loop through every char in input_str_split 
        if not is_number(char) and char not in valid_operators: # If it's not a number or valid operator, raise exception 
            raise PostfixFormatException("Invalid token")
        if is_number(char): # If it's a number then we know it's an operand, so we increment this variable 
            operands += 1 
        elif char in valid_operators:  # If it's included in the valid_operators list, then we know it's an operator, so we can incremement this  
        # variable 
            operators += 1 
    if operands - operators < 1: # The number of operands in a postfix should always be 
    # one greater than the numbe of operators, so if operands - operators is < 1, then we know 
    # there are not enough operands to evaluate expression and we raise an exception 
        raise PostfixFormatException("Insufficient operands")
    if operands - operators > 1: # Similarly, if the number is greater than the needed ratio of 
    # n (operands + 1) and operators, then there are too many operands 
        raise PostfixFormatException("Too many operands")
    else: 
        stack = Stack(30) # Baseline capacity for stack specified as 30 
        for char in input_str_split: # Traverse through string, if we find a char that is an 
        # operand, then we push to the stack 
            if is_number(char):
                stack.push(char) 
            else:
                # If we find an operator, then we now pop the last two operands in the stack 
                # and feed those two numbers into our math evaluation function along with operator 
                # that determines how they should be evaluated 
                operant_2 = stack.pop() 
                operant_1 = stack.pop() 
                result = math_eval(char, operant_1, operant_2)
                stack.push(result) # Once we've evaluated the two numbers, we push result 
        return stack.pop() # Once we've reached the end of our for loop, we want to pop the last 
        # (and only) element in our fully evaluated stack 



def infix_to_postfix(input_str):
    if input_str == "": # Checks same condition as in postfix 
        PostfixFormatException("Insufficent operands")
    else: 
        capacity = 30
        stack = Stack(capacity)
        output_list = [] # Create new list where we will store our list of operands and operators until we reach a condition that 
        # warrants us to push it to the list 
        input_str_split = input_str.split() # Split for iteration step 
        for i in input_str_split: 
            if is_number(i): # If it's a number, i.e. operant, then we want to store in output_list 
                output_list.append(i)
            elif i == "(": 
                stack.push(i) # If we encounter a ( that's the start of an expression that needs to be evaluated in a different order than the other 
                # numbers included 
            elif i == ")": # If we encounter a ) we know we've reached the end of the (expression) 
                top = stack.pop() # The first top 
                while top != "(": 
                    output_list.append(top)
                    top = stack.pop() 
            else: # Conditional block to evaluate all other operators 
                while (not stack.is_empty()) and (precedence(stack.peek()) >= precedence(i)): # If the stack is not empty and 
                # the precedence of the operator currently in the stack (i.e. stack.peek() is greater than the current operator, we 
                # append the operator currently at the top of the stack to our output_list 
                    if i == "**": 
                        break 
                    output_list.append(stack.pop())
                stack.push(i) # If the operator is not <= the current operator in the stack, then we push it to the stack as well 
        while not stack.is_empty(): # After we've looped through all operands and operators in the loop, we want pop all the elements currently in 
        # the stack, and append them to the output list 
            pop = stack.pop()
            output_list.append(pop)
        return " ".join(output_list) # Join to return string format 

'''

def order_priority(operator, peek_stack):
    low_precedence = ["+", "-"]
    medium_precedence = ["*", "/"]
    high_precedence = ["**"]
    if operator in operator_list_1 and peek_stack in operator_list_2: 
        return True 
    elif operator in operator_list_1 and peek_stack in operator_list_1: 
        return True 
    elif operator in operator_list_2 and peek_stack in operator_list_2: 
        return True 
    return False 

'''
"""Converts an infix expression to an equivalent postfix expression"""


def prefix_to_postfix(input_str):
    reversed_prefix = input_str[::-1] # Start by reversing input_str 
    capacity = 30
    stack = Stack(capacity) 
    output_list = [] 
    valid_operators = ["**", "*", "/", "+", "-", "<<", ">>"] 
    for char in reversed_prefix: 
        if is_number(char): 
            stack.push(char) 
        elif char in valid_operators: 
            operator = char
            operant_2 = stack.pop() 
            operant_1 = stack.pop()
            string = (operant_2 + " " + operant_1 + " " + operator) 
            stack.push(string) 
    while not stack.is_empty(): 
        pop = stack.pop()
        output_list.append(pop)
    return " ".join(str(item) for item in output_list) 

    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    


