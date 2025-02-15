#Roman Numeral to Decimal
class Solution:
    def roman_to_decimal(self, s: str) -> int:
        roman_values = { #values
            'I':1, 'V':5, 'X':10, 'L':50,
            'C':100, 'D':500, 'M':1000
        }

        total = 0

        for i in range (len(s) -1):
            if roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]] #subtract if next value is greater
            else:
                total += roman_values[s[i]] #add if next value is smaller or equal

        total += roman_values[s[-1]] #add to last char
        return total

user_input = input("Enter a roman numeral: ").upper() #converts to uppercase

sol = Solution()

result = sol.roman_to_decimal(user_input)

print(f"Your roman numeral {user_input} is {result} in decimal.")
