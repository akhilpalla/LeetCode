class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        subsequenceD = {}
        userVisitedpagesDict = {}
        for i in range(len(username)):
            if username[i] in userVisitedpagesDict:
                userVisitedpagesDict[username[i]].append((timestamp[i],website[i]))
            else:
                userVisitedpagesDict[username[i]] = [(timestamp[i],website[i])]
        
        
        def subsequence(index, userList, currentlst, cnt, user):
            if cnt == 3:
                currentlst = tuple(currentlst)
                if currentlst[:] not in subsequenceD:
                    subsequenceD[currentlst[:]] = [user]
                else:
                    if user not in subsequenceD[currentlst[:]]:
                        subsequenceD[currentlst[:]].append(user)
                return
            if index >= len(userList):
                return
            # take
            currentlst.append(userList[index][1])
            subsequence(index+1, userList, currentlst, cnt+1, user)
            currentlst.pop(-1)
            # not take
            subsequence(index+1, userList, currentlst, cnt, user)
        
        for user in userVisitedpagesDict:
            userArr = userVisitedpagesDict[user]
            userArr.sort(key=lambda x:x[0])
            subsequence(0,userArr, [], 0, user)
        
        for i in subsequenceD:
            subsequenceD[i] = len(subsequenceD[i])
        maxValOfValues = max(subsequenceD.values())
        
        result = []
        
        
        for s in subsequenceD:
            if subsequenceD[s] == maxValOfValues:
                result.append(list(s))
        result.sort()
        
        
        return result[0]

        