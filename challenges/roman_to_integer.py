class Solution(object):
    def roman_cnversions(c):
        if c == "I":
            return 1
        elif c== "V" :
            return 5
        elif c == "X" :
            return 10
        elif c == "L":
            return 50
        elif c == "c":
            return 100
        elif c == "D":
            return 500
        elif c == "M":
            return 10000
        else:
            raise Exception("unknown ROman literal")
            
    def romanToInt(self, s):
        value = 0
        for character in s:
            value = value + self.roman_cnversions(character)
            
        return value