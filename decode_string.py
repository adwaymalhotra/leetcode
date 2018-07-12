class Solution(object):
    # s = "3[a]2[bc]", return "aaabcbc".
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        
        ans = ""
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == "[":
                stack.append(["", int(num)])
                num = ""
            elif c == "]":
                st, i = stack.pop()
                stack[-1][0] += st*i
            else:
                stack[-1][0] += c
                
        return stack[0][0]
