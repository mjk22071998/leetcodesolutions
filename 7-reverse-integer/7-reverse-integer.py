class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = 2**31 - 1, -2**31
        sum = 0
        sign = 1 if x > 0 else -1
        while x:
            if not MIN/10 <= sum <= MAX/10:
                return 0
            sum *= 10
            digit = abs(x) % 10 * sign
            if MIN-digit <= sum <= MAX-digit:
                sum += digit
                x //= 10
                if sign < 0 and digit:
                    x += 1
            else:
                return 0

        return sum
        