class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        
        N = len(nums)

        l,h = 0, N-1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                return True
            elif nums[l]==nums[m]==nums[h]:
                l+=1
                h-=1
            elif nums[l]<=nums[m]:#pivot to right of m
                if nums[l]<=target<nums[m]:
                    h = m-1
                else:
                    l = m+1
            else:#pivot to left of m
                if nums[m]<target<=nums[h]:
                    l = m+1
                else:
                    h = m-1
                    
        return False
