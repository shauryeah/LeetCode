class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1={}
        stack=[]
        ans=[]
        for j in nums2[::-1]:
            while(stack and stack[-1]<=j):
                stack.pop()
            if(stack):
                num1[j]=stack[-1]
                stack.append(j)
            else:
                num1[j]=-1
                stack.append(j)
        for i in nums1:
            ans.append(num1[i])
        return ans





            