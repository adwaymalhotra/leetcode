class Solution:
    # increasing subsequences
    def findSubsequences(self, nums):
        N=len(nums)
        ans=[]
        res={k: [] for k in range(N)}
        
        for i in range(N-2, -1, -1):
            vis = set()
            ni = nums[i]
            for j in range(i+1, N):
                nj = nums[j]
                if ni <= nj and nj not in vis:
                    vis.add(nj)
                    res[i] += [[ni] + x for x in [[nj]] + res[j]]
     
        vis = set()
        for i in range(N):
            if nums[i] not in vis:
                vis.add(nums[i])
                ans += res[i]
        return ans

# num of subsequences whose product is less than k
        def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        ans = 0
        lz = -1
        p = 1
        
        for i in range(len(nums)):
            p *= nums[i]
            while p>=k and lz<i:
                lz+=1
                p//=nums[lz]
            ans += i-lz
                    
        return ans

# find pivot. pivot: nums[i] such that some of [:i] and [i+1:] are equal
        def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        
        if N < 2: return N-1

        sums = []        
        s = 0
        for n in nums:
            s += n
            sums.append(s)
            
        if s == nums[0]: return 0
            
        for i in range(1,N):
            if (s-sums[i]) == sums[i-1]:
                return i
        return -1

# find subarray such that sum is multiple of k
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """        
        sums = {0:-1}
        s = 0
        
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        
        for i in range(len(nums)):
            s += nums[i]
            r = s%k
            if r in sums:
                if i-sums[r]>=2: return True
            else:
                sums[r] = i
        
        return False      