class Solution(object):
    def roman_conversions(self,c):
        if c == "I":
            return 1
        elif c== "V" :
            return 5
        elif c == "X" :
            return 10
        elif c == "L":
            return 50
        elif c == "C":
            return 100
        elif c == "D":
            return 500
        elif c == "M":
            return 1000
        else:
            raise Exception("unknown Roman literal")
            
    def romanToInt(self, s):
        value = 0
        s_iterator = iter(range(len(s)))
        for counter in s_iterator:
            try:
                if(self.roman_conversions(s[counter]) < self.roman_conversions(s[counter+1])):
                    value = value + (self.roman_conversions(s[counter+1])-self.roman_conversions(s[counter]))
                    next(s_iterator, None)

                else:
                    value = value + self.roman_conversions(s[counter])
            except IndexError:
                break
            
        return value
        
s = Solution()
print(s.romanToInt("MCMXCIV"))