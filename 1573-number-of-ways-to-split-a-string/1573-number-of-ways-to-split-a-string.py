class Solution:

	def __init__(self) -> None:
		self.modulo = 10**9 + 7

	def _num_zeroes(self, s: str, num_ones: int) -> int:
		idx = -1
		for _ in range(num_ones):
			idx = s.find('1', idx + 1)
		return s.find('1', idx + 1) - idx

	def numWays(self, s: str) -> int:
		count_ones = s.count('1')
		if count_ones == 0:
			return comb(len(s) - 1, 2)%self.modulo
		elif count_ones%3 > 0:
			return 0

		ones_in_group = count_ones//3
		return (self._num_zeroes(s, ones_in_group)*self._num_zeroes(s[::-1], ones_in_group))%self.modulo