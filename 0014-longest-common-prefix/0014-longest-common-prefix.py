class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty, return an empty string
        if len(strs) == 0:
            return ""
        #If only one word
        if len(strs) == 1:
            return strs[0]

        ans = ""
        # Loop through each character index of the first word
        for index, value in enumerate(strs[0]):

            # Compare this character with the characters at the same index in all other words
            for j in range(1,len(strs)):

                # If the current index not exceeds the length of any word, or not mismatch is found
                if ( index < len(strs[j]) and value == strs[j][index]):
                    pass
                else:
                    return ans     
            ans = ans + value  

        return ans

# if there are n strings of equal size of m then NM comparisons
# S = 1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs)
        maxi = max(strs)
        ans  = 0
        for i in range(min(len(mini),len(maxi))):
            if mini[i] == maxi[i]:
                ans+=1
            else:
                break 

        return mini[:ans]

        
