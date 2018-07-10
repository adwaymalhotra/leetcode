class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0: return []
        ind = 0
        for i in range(k):
            if nums[i]>nums[ind]:
                ind = i

        ans = [nums[ind]]
        
        for x in range(1, len(nums)-k+1):
            if ind>=x:
                if nums[x+k-1]>nums[ind]: ind = x+k-1
            else:
                ind = x
                for i in range(x,x+k):
                    if nums[ind]<nums[i]: ind = i
            ans.append(nums[ind])
                    
        return ans
