class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # output = []

        # for i in range(len(nums)-k+1):
        #     curMax = nums[i]
        #     for j in range(i+1, i+k):
        #         curMax = max(curMax, nums[j])
        #     output.append(curMax)

        # return output
        q = deque()  # stores indices of elements
        output = []

        for i, val in enumerate(nums):
            # remove indices that are outside the current window of size k
            if q and q[0] <= i - k:
                q.popleft()

            # remove all smaller elements from the back
            while q and nums[q[-1]] < val:
                q.pop()

            # add current element's index
            q.append(i)

            # once seen at least k elements record the window max
            if i >= k - 1:
                output.append(nums[q[0]])

        return output
        
#time - O(N)