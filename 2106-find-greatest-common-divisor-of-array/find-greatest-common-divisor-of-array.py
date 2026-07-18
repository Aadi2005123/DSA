class Solution(object):
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)

        while largest:
            smallest, largest = largest, smallest % largest

        return smallest