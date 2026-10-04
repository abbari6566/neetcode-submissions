class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            #need to convert i to its binary
            binary = f"{i:b}"
            binaryStr = str(binary) #string to iterate over
            countOnes = 0

            for ones in binaryStr:
                if ones == "1": #if ones in the ith binary string add 1
                    countOnes += 1                

            result.append(countOnes)
            print(result)

        return(result)



        