# https://leetcode.com/problems/baseball-game/
class Solution(object):
    def calPoints(self, operations):
        scoreArray = []
        for op in operations:
            if op.lstrip('-').isdigit():  # Handle numeric strings including negatives
                scoreArray.append(int(op))
            elif op == "C":
                if scoreArray:
                    scoreArray.pop()
            elif op == "D":
                if scoreArray:
                    scoreArray.append(2 * scoreArray[-1])
            elif op == "+":
                if len(scoreArray) >= 2:
                    scoreArray.append(scoreArray[-1] + scoreArray[-2])
        return sum(scoreArray)

# Test the input
sol = Solution()
print(sol.calPoints(["5", "2", "C", "D", "+"]))  # Output: 30

# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:   
                stack.append(c)
        return True if not stack else False

# https://leetcode.com/problems/min-stack/
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
        
minStack = MinStack()
minStack.push(3)
minStack.push(5)
minStack.push(2)
minStack.push(4)

# Now the stacks are:
# stack:    [3, 5, 2, 4]
# minStack: [3, 3, 2, 2]
# when you call popmethod it pop 4 from stack and 2 from minStack yo will have

# stack becomes [3, 5, 2]
# minStack becomes [3, 3, 2]
# since you work on min value added when push is called, it is immposible you to get the last elemwnt of stack greater than minStack always if you compare the last elements paralelly you got minStack less.