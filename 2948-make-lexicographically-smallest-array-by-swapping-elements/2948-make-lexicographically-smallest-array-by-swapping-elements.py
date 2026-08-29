class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        arr=[]
        for i in range(len(nums)):
            arr.append((nums[i],i))
        arr.sort()
        group=[]
        curr=[arr[0]]
        for i in range(1,len(arr)):
            if arr[i][0]-arr[i-1][0]<=limit:
                curr.append(arr[i])
            else:
                group.append(curr)
                curr=[arr[i]]
        group.append(curr)
        for g in group:
            values = sorted(x[0] for x in g)
            indices = sorted(x[1] for x in g)

            for i in range(len(g)):
                nums[indices[i]] = values[i]
        return nums
        
        