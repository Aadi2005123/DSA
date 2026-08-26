class Solution(object):

    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        ans = ""
        min_len = float('inf')

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            cur = s[left:right + 1]

            if len(cur) < min_len:
                min_len = len(cur)
                ans = cur
            elif len(cur) == min_len and cur < ans:
                ans = cur

        return ans