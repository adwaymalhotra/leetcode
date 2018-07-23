class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def countPairs(ns, ans):
            c = 0
            for i in range(N):
                ind = bisect.bisect_right(nums, nums[i]+ans)
                if ind == N:
                    c += sum([x for x in range(1,N-i)])
                    break
                else:
                    c += ind-i-1
            return c
        
        N = len(nums)
        if N<2: return 0
        nums.sort()
        
        lo = 0
        hi = nums[-1]-nums[0]
        
        while lo<=hi:
            ans = (lo+hi)//2
            # counting number of pairs with distance <= ans
            if countPairs(nums, ans)<k:
                lo = ans+1
            else:
                hi = ans-1
        return lo
