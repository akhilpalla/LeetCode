class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        def can_map(pi, si):
            if pi == len(pattern) and si == len(s):
                return True
            if pi == len(pattern) or si == len(s):
                return False
            pchar = pattern[pi]
            if seen_pattern[ord(pchar) - ord('a')]:
                mapped_token = seen_pattern[ord(pchar) - ord('a')]
                curr_token = s[si: si + len(mapped_token)]
                return (curr_token == mapped_token 
                        and can_map(pi + 1, si + len(mapped_token)))

        
            for i in range(si, len(s)):
                token = s[si: i + 1]
                if seen_token.get(token, pchar) != pchar: continue
                seen_pattern[ord(pchar) - ord('a')] = token
                seen_token[token] = pchar
                if can_map(pi + 1, si + len(token)): return True
                del seen_token[token]
                seen_pattern[ord(pchar) - ord('a')] = None
            return False

        up, us = len(set(pattern)), len(set(s))
        if len(pattern) == up and up <= us : return True
        if len(s) < len(pattern): return False
        seen_pattern, seen_token = [None] * 26, {}
        return can_map(0, 0)