class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        ans = []

        for num in nums:
            if zeros > 1:
                ans.append(0)
            elif zeros == 1:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product // num)

        return ans