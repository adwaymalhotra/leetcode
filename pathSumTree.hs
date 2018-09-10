data Tree2 a
  = Null
  | Node a
         (Tree2 a)
         (Tree2 a)
  deriving (Show, Eq)

pathSumHelper t c p Null = []
pathSumHelper t c p (Node val t1 t2) =
  end ++
  (pathSumHelper t nc np t1) ++
  (pathSumHelper t nc np t2) ++
  (pathSumHelper t 0 [] t1) ++ (pathSumHelper t 0 [] t2)
  where
    nc = c + val
    np = p ++ [val]
    end
      | t - c == val = [np]
      | otherwise = []

pathSum _ Null = []
pathSum target tree = (pathSumHelper target 0 [] tree)
