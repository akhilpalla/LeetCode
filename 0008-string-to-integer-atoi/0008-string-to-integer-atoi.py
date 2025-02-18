class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        idx = 0
        sign = 1 

        if s[idx] == '+':
            sign = 1
            idx += 1
        elif s[idx] == '-':
            sign = -1
            idx += 1
        
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        ans = 0
        n = len(s)
        while idx < n:
            if not s[idx].isdigit():
                break
            digit = int(s[idx])
            
            if ((ans > INT_MAX // 10) or (ans == INT_MAX // 10 and digit > INT_MAX % 10)):
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            
            ans = 10 * ans + digit
            idx += 1
        
        return sign * ans

# T = N
# S = 1