class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Pad the string to handle boundaries easily
        t = '1' + s + '1'
        ones_blocks = []
        zeros_blocks = []
        
        current_char = t[0]
        current_len = 0
        
        # Group the consecutive 1s and 0s
        for char in t:
            if char == current_char:
                current_len += 1
            else:
                if current_char == '1':
                    ones_blocks.append(current_len)
                else:
                    zeros_blocks.append(current_len)
                current_char = char
                current_len = 1
                
        if current_char == '1':
            ones_blocks.append(current_len)
        else:
            zeros_blocks.append(current_len)
            
        original_ones = s.count('1')
        
        # If there are not enough blocks to merge, return original count
        if len(ones_blocks) <= 2 or len(zeros_blocks) < 2:
            return original_ones
            
        max_gain = 0
        # Safely iterate through the available zero blocks
        for i in range(len(zeros_blocks) - 1):
            gain = zeros_blocks[i] + zeros_blocks[i+1]
            if gain > max_gain:
                max_gain = gain
                
        return original_ones + max_gain
