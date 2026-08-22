class Solution(object):
    def checkDivisibility(self, n):
        sum = 0
        product = 1
        temp = n

        while temp > 0:
            digit = temp % 10

            sum += digit
            product *= digit

            temp //= 10

        return n % (sum + product) == 0