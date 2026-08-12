class Solution(object):
    def subsets(self, nums):
        result = []
        temp = []

        def backtrack(result, temp, nums, start):
            result.append(temp[:])

            for i in range(start, len(nums)):
                temp.append(nums[i])

                backtrack(result, temp, nums, i + 1)

                temp.pop()

        backtrack(result, temp, nums, 0)

        return result