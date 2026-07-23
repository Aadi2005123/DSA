import math

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Handle small array base cases
        if n < 3:
            return n
            
        # n.bit_length() gives the number of bits needed to represent n
        # 1 << bit_length calculation yields the next power of 2
        return 1 << n.bit_length()
