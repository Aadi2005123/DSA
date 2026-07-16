import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        # स्टेप 1: बिना कोई एरे बनाए, ऑरिजिनल एरे में ही इन-प्लेस GCD की वैल्यूज डालें (Memory Savings)
        current_max = nums[0]
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            nums[i] = math.gcd(nums[i], current_max)
            
        nums.sort()
        total_gcd_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_gcd_sum += math.gcd(nums[left], nums[right])
            left += 1
            right -= 1
            
        return total_gcd_sum
