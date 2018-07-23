class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ps = {i:set() for i in range(numCourses)}
        fs = {i:set() for i in range(numCourses)}
        
        for i,j in prerequisites:
            ps[i].add(j)
            fs[j].add(i)
            
        q = collections.deque([key for key in ps if not ps[key]])
        ans = []
        c=0
        while q:
            n = q.popleft()
            ans.append(n)
            c+=1
            for i in fs[n]:
                ps[i].remove(n)
                if not ps[i]:
                    q.append(i)
        
        return ans if c==numCourses else []
        
