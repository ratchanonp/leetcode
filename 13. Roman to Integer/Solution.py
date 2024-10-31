class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        prev = 0
        for c in s:
            if prev < roman[c]:
                result += roman[c] - 2 * prev
            else:
                result += roman[c]
            prev = roman[c]
            
        return result    
        
s = Solution()
print(s.romanToInt("III")) # 3
print(s.romanToInt("LVIII")) # 58
print(s.romanToInt("MCMXCIV")) # 1994