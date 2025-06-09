from stack import Stack

def parentheses_checker(expr):
    s = Stack()
    lefty = '[{(' 
    righty = ']})'
    for c in expr:
        if c in lefty:
            s.push(c)
            