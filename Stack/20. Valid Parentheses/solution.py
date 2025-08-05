class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                # If it is a closing bracket, and the stack is empty
                if stack == []:
                    return False
                elif char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
# Alternative method                 
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        # Dictionary to map each opening bracket to its corresponding closing bracket
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                # If the c is a closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # Top of the stack matches -> pop the opening bracket
                    stack.pop()
                else:
                    return False
            else:
                # If the c is an opening bracket, push it onto the stack
                stack.append(c)
        # At the end, the stack should be empty
        return True if not stack else False
