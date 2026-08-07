class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into 2, 3, 5, 7
        t_factors = {2: 0, 3: 0, 5: 0, 7: 0}
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                t_factors[p] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"

        def get_factors(d: int):
            f = {2: 0, 3: 0, 5: 0, 7: 0}
            if d in (2, 4, 8):
                f[2] = 1 if d == 2 else (2 if d == 4 else 3)
            elif d == 6:
                f[2], f[3] = 1, 1
            elif d in (3, 9):
                f[3] = 1 if d == 3 else 2
            elif d == 5:
                f[5] = 1
            elif d == 7:
                f[7] = 1
            return f

        def get_min_digit_counts(req):
            c2, c3 = max(0, req[2]), max(0, req[3])
            c5, c7 = max(0, req[5]), max(0, req[7])
            
            c9 = c3 // 2
            c3 %= 2
            
            c8 = c2 // 3
            c2 %= 3
            
            c4 = c2 // 2
            c2 %= 2
            
            c6 = 0
            if c2 == 1 and c3 == 1:
                c2, c3, c6 = 0, 0, 1
            elif c3 == 1 and c4 == 1:
                c2, c6, c3, c4 = 1, 1, 0, 0

            return {2: c2, 3: c3, 4: c4, 5: c5, 6: c6, 7: c7, 8: c8, 9: c9}

        def construct_digits(d_counts):
            res = []
            for d in range(2, 10):
                res.extend([str(d)] * d_counts[d])
            return res

        n = len(num)
        
        # Build prefix factors up to the first '0'
        prefix_factors = [{2: 0, 3: 0, 5: 0, 7: 0}]
        first_zero = -1
        
        for i, ch in enumerate(num):
            d = int(ch)
            if d == 0:
                first_zero = i
                break
            f = get_factors(d)
            curr = {p: prefix_factors[-1][p] + f[p] for p in t_factors}
            prefix_factors.append(curr)

        # Check if original num is valid (if no zeros present)
        if first_zero == -1:
            if all(prefix_factors[-1][p] >= t_factors[p] for p in t_factors):
                return num

        # Search for same-length solution from right to left
        search_limit = first_zero if first_zero != -1 else n - 1

        for i in range(search_limit, -1, -1):
            curr_pref = prefix_factors[i]
            d = int(num[i])
            space_after = n - 1 - i
            
            # Choose a larger digit at index i
            for bigger in range(d + 1, 10):
                f_bigger = get_factors(bigger)
                
                needed = {
                    p: t_factors[p] - curr_pref[p] - f_bigger[p]
                    for p in t_factors
                }
                
                d_counts = get_min_digit_counts(needed)
                total_digits_needed = sum(d_counts.values())
                
                if total_digits_needed <= space_after:
                    fill_ones = space_after - total_digits_needed
                    suffix = "1" * fill_ones + "".join(construct_digits(d_counts))
                    return num[:i] + str(bigger) + suffix

        # Fallback: Extend string length if no same-length candidate exists
        needed = t_factors.copy()
        d_counts = get_min_digit_counts(needed)
        total_digits = sum(d_counts.values())
        target_len = max(n + 1, total_digits)
        
        fill_ones = target_len - total_digits
        return "1" * fill_ones + "".join(construct_digits(d_counts))