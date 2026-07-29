from sortedcontainers import SortedDict

class Solution:
    mod = 109930813984377167
    maxi = int(1e4)
    fact = [1] * (maxi + 1)
    for i in range(1, maxi + 1):
        fact[i] = (fact[i - 1] * i) % mod
    inv = [1]*maxi + [pow(fact[maxi], mod - 2, mod)]
    for i in range(maxi, 0, -1):
        inv[i - 1] = (inv[i] * i) % mod
    
    def calculatePermu(self, dec):
        tot = 0
        for j in dec:
            tot += dec[j]
        upper = self.fact[tot]
        for j in dec:
            upper = (upper * self.inv[dec[j]]) % self.mod
        return upper


    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        t = ""
        dec = SortedDict()
        for i in range(n//2):
            if s[i] in dec:
                dec[s[i]] += 1
            else:
                dec[s[i]] = 1
        #print(dec)
        if k > self.calculatePermu(dec):
            return ""
        for i in range(n//2):
            for j in dec:
                if dec[j] > 0:
                    dec[j] -= 1
                    tot = self.calculatePermu(dec)
                    #print(tot, dec)
                    if k <= tot:
                        t += j
                        break
                    k -= tot
                    dec[j] += 1
        if n % 2 == 0:
            return t + t[::-1]
        return t + s[n//2] + t[::-1]
        
            
