class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        left = {}
        right = {}
        ans = []

        p = 1
        for i in range(n):
            left[i] = p
            p *= nums[i]

        p = 1
        for i in range(n - 1, -1, -1):
            right[i] = p
            p *= nums[i]

        for i in range(n):
            ans.append(left[i] * right[i])

        return ans