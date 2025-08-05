class MinStack:

    def __init__(self):
        self.stack = []
        # To track the minimum value at each time
        self.minstack = []

    def push(self, val: int) -> None:
        # Always push to the stack
        self.stack.append(val)
        # If the minstack is empty or the value is smaller than or equal to the current minimum value, push it into the minstack 
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        # If the top element being popped is also the current min, remove it from minstack, too
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop() # remove from main stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
