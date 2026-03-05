class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        total = 0

        i, j = len(a) - 1, len(b) - 1
        while i>=0 or j>=0 or carry:
            a_digit = int(a[i]) if i >= 0 else 0
            b_digit = int(b[j]) if j >= 0 else 0
            total = a_digit + b_digit + carry

            res.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1

        return "".join(res[::-1]) # make string out of the array after reversing all the digits