class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        prefix = [[0] * len(s) for i in range(5)]
        prefix[int(s[0])][0] = 1

        for i in range(1, len(s)):
            for j in range(5):
                prefix[j][i] = prefix[j][i - 1]
            prefix[int(s[i])][i] += 1

        maximum = -30000
        for i in range(1, 5):
            for j in range(i):
                even_even_one = [[None] * 3 for a in range(len(s)+1)]
                even_even_two = [[None] * 3 for a in range(len(s)+1)]
                even_odds_one = [[None] * 3 for a in range(len(s)+1)]
                even_odds_two = [[None] * 3 for a in range(len(s)+1)]
                odds_even_one = [[None] * 3 for a in range(len(s)+1)]
                odds_even_two = [[None] * 3 for a in range(len(s)+1)]
                odds_odds_one = [[None] * 3 for a in range(len(s)+1)]
                odds_odds_two = [[None] * 3 for a in range(len(s)+1)]
                
                for x in range(len(s)):
                    if prefix[i][x]%2 == 1 and prefix[j][x]%2 == 0:
                        one = prefix[i][x] - prefix[j][x]
                        if odds_even_one[x][0] == None:
                            odds_even_one[x] = [prefix[i][x],prefix[j][x],one]
                        elif one < odds_even_one[x][2]:
                            odds_even_one[x] = [prefix[i][x],prefix[j][x],one]
                        if odds_even_two[x][0] == None:
                            odds_even_two[x] = [prefix[i][x],prefix[j][x],one]
                        elif one > odds_even_two[x][2]:
                            odds_even_two[x] = [prefix[i][x],prefix[j][x],one]
                    elif prefix[j][x]%2 == 1 and prefix[i][x]%2 == 0:
                        one = prefix[j][x] - prefix[i][x]
                        if even_odds_one[x][0] == None:
                            even_odds_one[x] = [prefix[i][x],prefix[j][x],one]
                        elif one < even_odds_one[x][2]:
                            even_odds_one[x] = [prefix[i][x],prefix[j][x],one]
                        if even_odds_two[x][0] == None:
                            even_odds_two[x] = [prefix[i][x],prefix[j][x],one]
                        elif one > even_odds_two[x][2]:
                            even_odds_two[x] = [prefix[i][x],prefix[j][x],one]
                    elif prefix[i][x]%2 == 0 and prefix[j][x]%2 == 0:
                        one = prefix[i][x] - prefix[j][x]
                        if even_even_one[x][0] == None:
                            even_even_one[x] = [prefix[i][x],prefix[j][x],one]
                        elif one < even_even_one[x][2]:
                            even_even_one[x] = [prefix[i][x],prefix[j][x],one]
                        if even_even_two[x][0] == None:
                            even_even_two[x] = [prefix[i][x],prefix[j][x],one]
                        elif one > even_even_two[x][2]:
                            even_even_two[x] = [prefix[i][x],prefix[j][x],one]
                    elif prefix[j][x]%2 == 1 and prefix[i][x]%2 == 1:
                        one = prefix[j][x] - prefix[i][x]
                        if odds_odds_one[x][0] == None:
                            odds_odds_one[x] = [prefix[i][x],prefix[j][x],one]
                        elif one < odds_odds_one[x][2]:
                            odds_odds_one[x] = [prefix[i][x],prefix[j][x],one]
                        if odds_odds_two[x][0] == None:
                            odds_odds_two[x] = [prefix[i][x],prefix[j][x],one]
                        elif one > odds_odds_two[x][2]:
                            odds_odds_two[x] = [prefix[i][x],prefix[j][x],one]
                    
                    if x >= k-1:
                        if prefix[i][x]%2 == 1 and prefix[j][x]%2 == 0 and prefix[j][x]!=0:
                            one = prefix[i][x] - prefix[j][x]
                            maximum = max(maximum, one)
                            for y in range(x-k, -1, -1):
                                if even_even_one[y][1] == None:
                                    break
                                if even_even_one[y][1] < prefix[j][x]:
                                    maximum = max(maximum, one - even_even_one[y][2])
                                    break
                            for y in range(x-k, -1, -1):
                                if odds_odds_one[y][0] == None:
                                    break
                                if odds_odds_one[y][0] < prefix[i][x]:
                                    maximum = max(maximum, -one - odds_odds_one[y][2])
                                    break

                        elif prefix[j][x]%2 == 1 and prefix[i][x]%2 == 0 and prefix[i][x]!=0:
                            one = prefix[j][x] - prefix[i][x]
                            maximum = max(maximum, one)
                            for y in range(x-k, -1, -1):
                                if even_even_two[y][0] == None:
                                    break
                                if even_even_two[y][0] < prefix[i][x]:
                                    maximum = max(maximum, one + even_even_two[y][2])
                                    break
                            for y in range(x-k, -1, -1):
                                if odds_odds_one[y][1] == None:
                                    break
                                if odds_odds_two[y][1] < prefix[j][x]:
                                    maximum = max(maximum, -one + odds_odds_two[y][2])
                                    break

                        elif prefix[i][x]%2==0 and prefix[j][x]%2==0 and prefix[i][x]!=0 and prefix[j][x]!=0:
                            one = prefix[i][x] - prefix[j][x]
                            for y in range(x-k, -1, -1):
                                if odds_even_one[y][1] == None:
                                    break
                                if odds_even_one[y][1] < prefix[j][x]:
                                    maximum = max(maximum, one - odds_even_one[y][2])
                                    break
                            for y in range(x-k, -1, -1):
                                if even_odds_one[y][0] == None:
                                    break
                                if even_odds_one[y][0] < prefix[i][x]:
                                    maximum = max(maximum, -one - even_odds_one[y][2])
                                    break

                        elif prefix[j][x]%2 == 1 and prefix[i][x]%2 == 1:
                            one = prefix[j][x] - prefix[i][x]
                            for y in range(x-k, -1, -1):
                                if odds_even_two[y][0] == None:
                                    break
                                if odds_even_two[y][0] < prefix[i][x]:
                                    maximum = max(maximum, one + odds_even_two[y][2])
                                    break
                            for y in range(x-k, -1, -1):
                                if even_odds_two[y][1] == None:
                                    break
                                if even_odds_two[y][1] < prefix[j][x]:
                                    maximum = max(maximum, -one + even_odds_two[y][2])
                                    break
                    even_even_one[x+1] = even_even_one[x]
                    even_even_two[x+1] = even_even_two[x]
                    even_odds_one[x+1] = even_odds_one[x]
                    even_odds_two[x+1] = even_odds_two[x]
                    odds_even_one[x+1] = odds_even_one[x]
                    odds_even_two[x+1] = odds_even_two[x]
                    odds_odds_one[x+1] = odds_odds_one[x]
                    odds_odds_two[x+1] = odds_odds_two[x]

        return maximum          