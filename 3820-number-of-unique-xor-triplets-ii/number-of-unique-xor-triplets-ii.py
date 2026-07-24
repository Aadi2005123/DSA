class Solution:
    def uniqueXorTriplets(self, nums):
        N = 2048

        a = [0] * N
        for x in set(nums):
            a[x] = 1

        def fwht(f):
            n = len(f)
            step = 1
            while step < n:
                jump = step * 2
                for i in range(0, n, jump):
                    for j in range(step):
                        u = f[i + j]
                        v = f[i + j + step]
                        f[i + j] = u + v
                        f[i + j + step] = u - v
                step <<= 1

        fwht(a)

        for i in range(N):
            a[i] = a[i] ** 3

        fwht(a)

        ans = 0
        for x in a:
            if x != 0:
                ans += 1

        return ans