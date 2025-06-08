class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        return self.data.append(item)
    
    def pop(self):
        return self.data.pop()
    
    def is_empty(self):
        return len(self.data) == 0
    
    def peek(self):
        return self.data[-1]
    
    def len(self):
        return len(self.data) 