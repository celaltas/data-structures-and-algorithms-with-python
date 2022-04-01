


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


"""
Question: Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

"""

class StackWithMins(Stack):

    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        

    def pop(self):
        if not self.is_empty():
            if self.min() == self.items.pop():
                self.stack.pop()


    def push(self, item):
        self.items.append(item)
        if item<self.min():
            self.stack.push(item)
    
    def min(self):
        if self.stack.size()>0:
            return self.stack.items[-1]
        else:
            return float("inf")


stack = Stack()
stack_with_mins = StackWithMins(stack=stack)


stack_with_mins.push(6)
print("min:", stack_with_mins.min())
print("stack:", stack_with_mins.items)
stack_with_mins.push(7)
print("min:", stack_with_mins.min())
print("stack:", stack_with_mins.items)
stack_with_mins.push(5)
print("min:", stack_with_mins.min())
print("stack:", stack_with_mins.items)
stack_with_mins.push(4)
print("min:", stack_with_mins.min())
print("stack:", stack_with_mins.items)
stack_with_mins.pop()
print("min:", stack_with_mins.min())
print("stack:", stack_with_mins.items)
stack_with_mins.pop()
print("min:", stack_with_mins.min())
print("stack:", stack_with_mins.items)
stack_with_mins.pop()
print("min:", stack_with_mins.min())
print("stack:", stack_with_mins.items)
