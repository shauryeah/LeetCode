class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not self.minstack or value<=self.minstack[-1]:
            self.minstack.append(value)
        
    def pop(self):
        """
        :rtype: None
        """
        n=self.stack.pop()
        if self.minstack and n==self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()