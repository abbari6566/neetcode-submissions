class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        XOR and AND operations
        Carry until 0
        Time - O(n)
        '''
        mask = 0xffffffff
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        # convert back to a Python negative if the 32-bit sign bit is set
        return a if a <= 0x7fffffff else ~(a ^ mask)
        