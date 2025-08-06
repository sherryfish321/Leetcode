class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                # Pop the two operands from the stack 
                b = stack.pop()
                a = stack.pop()
                # Apply the operator to a & b
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                # Perform integer division with truncation toward zero
                else:
                    stack.append(int(a / b))
            else:
                # Convert numeric string to integer and push onto stack
                stack.append(int(token))
        return stack[0]

