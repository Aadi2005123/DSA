class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        
        # Generate all possible sequential digit numbers
        for length in range(2, 10):
            for start in range(1, 10 - length + 1):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    break
        
        return result