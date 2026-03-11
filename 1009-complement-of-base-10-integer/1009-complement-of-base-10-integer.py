class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        binary_representation = bin(N)[2:]  # Convert decimal to binary and remove the '0b' prefix
        complement_binary = ''.join(['1' if bit == '0' else '0' for bit in binary_representation])
        
        return int(complement_binary, 2)  # Convert binary back to decimal