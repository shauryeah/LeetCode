class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        dicti={}
        ans=[]
        for i in range(len(nums2)): 
            while stack and nums2[stack[-1]]<nums2[i]:
                k=stack.pop()
                dicti[nums2[k]]=nums2[i]
            stack.append(i)
        for num in nums1:
            ans.append(dicti.get(num,-1))
        return ans









            