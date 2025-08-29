class Solution:
    def shortestDistanceColor(self, c: List[int], q: List[List[int]]) -> List[int]:
    	C, A = {}, []
    	for i,j in enumerate(c):
    		if j in C: C[j].append(i)
    		else: C[j] = [i]
    	for [i,d] in q:
    		if d not in C:
    			A.append(-1)
    			continue
    		I = bisect.bisect(C[d],i)
    		A.append(min(abs(i-C[d][I-1]),abs(i-C[d][min(I,len(C[d])-1)])))
    	return(A)
		
		
 