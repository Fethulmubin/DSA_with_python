# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
class Solution(object):
    def countStudents(self, students, sandwiches):
        count = 0
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students[0])
                students.pop(0)
                count += 1
            if count == len(students):
                break
        return count
    
    # https://leetcode.com/problems/implement-stack-using-queues/description/
    from collections import deque
class MyStack(object):

    def __init__(self):
         self.queue = deque()
        

    def push(self, x):
        self.queue.append(x)

        for s in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        
        

    def pop(self):
       return self.queue.popleft()
        

    def top(self):
        return self.queue[0]
        

    def empty(self):
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()