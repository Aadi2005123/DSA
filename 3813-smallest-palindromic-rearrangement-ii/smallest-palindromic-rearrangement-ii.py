from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        mid = ""
        cnt = [0] * 26
        half_len = 0

        for ch, f in freq.items():
            if f & 1:
                mid = ch
            cnt[ord(ch) - 97] = f // 2
            half_len += f // 2

        LIMIT = k

        def count_perm(cnt):
            rem = sum(cnt)
            ans = 1
            for x in cnt:
                if x:
                    ans *= comb(rem, x)
                    if ans > LIMIT:
                        return LIMIT + 1
                    rem -= x
            return ans

        if count_perm(cnt) < k:
            return ""

        left = []

        for _ in range(half_len):
            for c in range(26):
                if cnt[c] == 0:
                    continue

                cnt[c] -= 1
                ways = count_perm(cnt)

                if ways >= k:
                    left.append(chr(c + 97))
                    break

                k -= ways
                cnt[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]