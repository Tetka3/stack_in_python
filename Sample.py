from stack import Stack

def parentheses_checker(expr):
    s = Stack()
    lefty = '[{(' 
    righty = ']})'
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False 
            if righty.index(c) != lefty.index(s.pop()):
                return False 