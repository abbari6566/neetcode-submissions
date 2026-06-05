class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        p_product = 1
        s_product = 1
        for i in range(1,len(nums)):
            p_product *= nums[i-1]
            prefix.append(p_product)
        for j in range(len(nums)-2,-1,-1):
            s_product *= nums[j+1]
            suffix.append(s_product)
        suffix.reverse()

        result = []
        for i,j in zip(prefix,suffix):
            result.append(i*j)
        return result





        