#Word Break
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def dfs(i):
          visited.add(i)
          if i==L: return True
          else:
            sub = s[i:]
            for word in wordDict:
              if sub.startswith(word) == True:
                n = i + len(word)
                if n not in visited:
                  result = dfs(n)
                  if result == True: return True
          return False
        L = len(s)
        visited = set()
        return dfs(0)

#Word Break II
class Solution:
  def wordBreak(self, s, wordDict):
    """ 
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str] 
    """
    def build(p, c, sen): 
      if c == L: 
        x = sen + " " + s[p:c] 
        ans.append(x.strip()) 
      else: for i in graph[c]: 
        build(c, i, sen + " " + s[p:c])

    ans = []
    L = len(s)
    if not s or not wordDict or L == 0 or len(wordDict) == 0: return []

    if L == 1 and s in wordDict:
      return [s]

    graph = {k: [] for k in range(L)}

    for i in range(len(s)-1, -1, -1):
      for j in range(i, L):
        word = s[i:j+1]
        if (j+1==L or len(graph[j+1])>0):
          if word in wordDict:
            graph[i].append(j+1)

    for i in graph[0]:
      build(0, i, "")

    return ans