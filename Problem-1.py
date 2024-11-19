#Approach
#maintain prev and current number do the operation when we find the sign incase of */ we need to multiply with prev and current


#Complexities:
#Time: O(n)
#Space: O(1)


class Solution:
    def calculate(self, s: str) -> int:
        calculated = 0
        prevNum = 0
        currNum = 0
        sign = "+"

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                currNum = 10 * currNum + int(char)

            if char in ["+", "-", '/', "*"] or (i == len(s)-1 and(char==" " or char.isdigit())) :
                if sign == "*":
                    calculated = calculated - prevNum + (prevNum * currNum)
                    prevNum = currNum * prevNum
                elif sign == "+":
                    calculated += currNum
                    prevNum = currNum

                elif sign == "-":
                    calculated -= currNum
                    prevNum = -currNum

                elif sign == "/":
                    calculated = calculated - prevNum + int(prevNum / currNum)
                    prevNum = int(prevNum / currNum)
                sign = char
                currNum = 0

        return calculated

s=  Solution()
print(s.calculate(" 3/2 "))