class Solution:
  #min num of perfect squares required to sum up n
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4: return n
        
        def isPerfectSquare(n):
          x = int(n**0.5)
          return (x*x)==n
        
        q = {n}
        lvl = 0
        while q:
          lvl += 1 #distance from root
          temp = set() #buffer for new items to be evaulated in next iteration
          for i in q: 
            sqrt = int(i**0.5)
            for n in range(sqrt, 0, -1):
              if i == sqrt*sqrt: return lvl
              r = i - n*n
              if isPerfectSquare(r):
                return lvl+1
              else: temp.add(r)
          q = temp
            
        return lvl