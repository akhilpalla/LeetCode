class Solution(object):
    def totDif(self,vec1,vec2):
        return abs(vec1[0]-vec2[0]) + abs(vec1[1]-vec2[1])
    def totalDistance(self, s):
        """
        :type s: str
        :rtype: int
        """
        charPos = {'q':[0,0],'w':[0,1],'e':[0,2],'r':[0,3],'t':[0,4],'y':[0,5],	'u':[0,6],'i':[0,7],'o':[0,8],'p':[0,9],
'a':[1,0],'s':[1,1],'d':[1,2],'f':[1,3],'g':[1,4],'h':[1,5],'j':[1,6],'k':[1,7],'l':[1,8],	 
'z':[2,0],'x':[2,1],'c':[2,2],'v':[2,3],'b':[2,4],'n':[2,5],'m':[2,6]}
        res = self.totDif(charPos['a'],charPos[s[0]])
        for i in range(1,len(s)):
            res += self.totDif(charPos[s[i-1]],charPos[s[i]])

        return res       