class Solution:
    def findKthSmallest(self, coins, k):

        coins.sort()

        # Remove redundant coins
        useful = []

        for c in coins:
            redundant = False

            for x in useful:
                if c % x == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(c)

        coins = useful
        n = len(coins)

        # GCD function
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # LCM function
        def lcm(a, b):
            return (a // gcd(a, b)) * b

        # Count distinct amounts <= x
        def count(x):

            ans = 0

            for mask in range(1, 1 << n):

                multiple = 1
                bits = 0
                valid = True

                for i in range(n):

                    if mask & (1 << i):

                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            valid = False
                            break

                if valid:

                    if bits % 2 == 1:
                        ans += x // multiple
                    else:
                        ans -= x // multiple

            return ans

        # Binary search
        left = 1
        right = coins[0] * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left