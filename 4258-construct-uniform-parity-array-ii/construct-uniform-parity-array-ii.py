class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        # If there is no odd number,
        # all elements are already even.
        if min_odd == float('inf'):
            return True

        # Make everything odd.
        # Every even number must have a smaller odd number.
        return min_odd < min_even