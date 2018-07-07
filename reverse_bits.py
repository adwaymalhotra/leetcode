import math

def reverseBits(n):
    bits = [0]*32
    
    while n>0:
        print(math.log(n,2))
        x = int(math.log(n,2))
        n = n-x
        bits[x] = 1
    
    print(bits)
    
    ans = 0
    for i in range(32):
        ans += bits[i]*2**i
        
    return ans
