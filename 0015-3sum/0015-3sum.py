class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sol=[]
        for i in range(len(nums)-2):
            if i!=0 and nums[i-1]==nums[i]:
                continue
            left=i+1
            right=len(nums)-1
            while(left<right):
                target=nums[left]+nums[right]+nums[i]
                if(target==0):
                    sol.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while((left<right) and (nums[left]==nums[left-1])):
                        left+=1
                    while((left<right) and (nums[right]==nums[right+1])):
                        right-=1
                elif(target<0):
                    left+=1
                else:
                    right-=1
        return sol

                