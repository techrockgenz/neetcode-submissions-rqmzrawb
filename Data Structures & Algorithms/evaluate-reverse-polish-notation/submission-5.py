class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
                match token:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "-":
                        operand1, operand2 = stack.pop(), stack.pop()
                        stack.append(operand2 - operand1)
                    case "*":
                        stack.append(stack.pop() * stack.pop())
                    case "/":
                        operand1, operand2 = stack.pop(), stack.pop()
                        stack.append(int(operand2 / operand1))
                    case _ :
                        stack.append(int(token))
        return stack[-1];