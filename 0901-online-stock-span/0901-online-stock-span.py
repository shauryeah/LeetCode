class StockSpanner(object):

    def __init__(self):
        self.stack=[]


    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.span=1
        while self.stack and self.stack[-1][0]<=price:
            self.span+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,self.span))
        return self.stack[-1][1]

           



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)