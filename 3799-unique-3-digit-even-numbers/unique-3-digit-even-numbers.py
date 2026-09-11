class Solution(object):
    def totalNumbers(self, digits):
        count = 0

        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 10, 2):

                    num = [i, j, k]
                    temp = digits[:]
                    possible = True

                    for d in num:
                        if d in temp:
                            temp.remove(d)
                        else:
                            possible = False
                            break

                    if possible:
                        count += 1

        return count