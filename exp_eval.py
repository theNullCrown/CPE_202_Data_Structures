## Name: Allie Blaising

from stack_array import Stack

# You should not change this Exception class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    if input_str == "": 
        PostfixFormatException("Insufficent operands")
    else: 
        stack = Stack() 
        split = input_str.split()
        for i in input_str: 
            if i.is_number(): 
                stack.push(int(i)) 
        else: 
            operator = i 
            operant_1 = stack.pop() 
            operant_2 = stack.pop()
            result = math_eval(operator, operant_1, operant_2)
            stack.push(result)
        return stack.pop() 



def math_eval(operator, operant_1, operant_2):  
    if operator == "*": 
        return operant_1 * operant_2
    elif operator == "/": 
        return operant_2 / operant_1 
    elif operator == "+": 
        return operant_1 + operant_2 
    elif operator == "**": 
        return operant_2 ** operant_1 
    else: 
        return operant_2 - operant_1 
    

def is_number(n):
    try:
        float(n)  
    except ValueError:
        return False
    else: 
        return True 



def infix_to_postfix(input_str):
    if input_str == "": 
        PostfixFormatException("Insufficent operands")
    else: 
        stack = Stack()
        operators = ["+", "-", "*", "/", "**" , "<<", ">>"]
        output_list = [] 
        input_str_split = input_str.split()
        for i in input_str_split: 
            if i.isalpha() or is_number(i): 
                output_list.append(i)
            elif i == "(": 
                stack.push(i)
            elif i == ")": 
                top = stack.pop()
                while top != "(": 
                    output_list.append(top)
                    top = stack.pop() 
            else: 
                peek_stack = stack.peek() 
                while not stack.is_empty() and order_priority(i, peek_stack): 
                    output_list.append(stack.pop())
                stack.push(i)
        while not stack.is_empty(): 
            pop = stack.pop()
            output_list.append(pop)
        return " ".join(output_list)



def order_priority(operator, peek_stack):
    operator_list_1 = ["+", "-"]
    operator_list_2 = ["*", "/", "**"]
    if operator in operator_list_1 and peek_stack in operator_list_2: 
        return True 
    elif operator in operator_list_1 and peek_stack in operator_list_1: 
        return True 
    elif operator in operator_list_2 and peek_stack in operator_list_2: 
        return True 
    return False 


    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """




def prefix_to_postfix(input_str):
    pass 
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    


