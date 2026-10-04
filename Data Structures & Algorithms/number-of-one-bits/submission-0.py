class Solution:
    def hammingWeight(self, n: int) -> int:
        #change input number to bits
        binary = f"{n:b}"

        #convert to string to iterate through
        binaryStr = str(binary)

        #count ones
        countOnes = 0

        for b in binaryStr:
            if b == "1":
                countOnes += 1
        
        return countOnes