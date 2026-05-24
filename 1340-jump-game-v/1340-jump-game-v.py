class Solution:
	def maxJumps(self, arr: List[int], d: int) -> int:

		dp = defaultdict(int)
		def dfs(i):
			if i in dp: return dp[i]
			m_path = 0
			for j in range(i+1,i+d+1):
				if j>=len(arr) or arr[j]>=arr[i]: break
				m_path = max(m_path,dfs(j))

			for j in range(i-1,i-d-1,-1):
				if j<0 or arr[j]>=arr[i]: break
				m_path = max(m_path,dfs(j))
			dp[i] = m_path+1
			return m_path+1

		res = 0
		for i in range(len(arr)):
			res = max(res,dfs(i))
		return res