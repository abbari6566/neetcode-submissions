class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:

                result.append(left+1)
                result.append(right+1)
                #exit
                return result
            elif numbers[left] + numbers[right] > target:
                #move right towards left
                right -= 1
            else:
                #move left towards right
                left += 1

        