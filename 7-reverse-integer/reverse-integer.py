class Solution(object):
    def reverse(self, x):

        if x < 0:
            sign = -1
            w = -x
        else:
            sign = 1
            w = x

        reverse = 0

        while w > 0:
            l = w % 10
            w = w // 10
            reverse = reverse * 10 + l

        reverse = sign * reverse

        if reverse > 2147483647:
            return 0

        if reverse < -2147483648:
            return 0

        return reverse