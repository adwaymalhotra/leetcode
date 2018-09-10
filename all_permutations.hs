getPermutations :: [Char] -> [[Char]]
getPermutations (s:ts) = helper ([s] : []) ts

helper :: [[Char]] -> [Char] -> [[Char]]
helper ps [] = ps
helper ps (c:cs) = helper newps cs
  where
    newps = concat [strHelper p c | p <- ps]

strHelper :: [Char] -> Char -> [[Char]]
strHelper (s:[]) c = (c : s : []) : (s : c : []) : []
strHelper (s:ss) c = (c : s : ss) : [s : r | r <- (strHelper ss c)]
