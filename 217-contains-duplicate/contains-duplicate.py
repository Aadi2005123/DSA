class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()

        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                return True

            left += 1
            right += 1

        return False