class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = {}
        # result = []
        # for key in nums:
        #     if key not in hashmap:
        #         hashmap[key] = 1
        #     else:
        #         hashmap[key] += 1
        # for i in range(k):
        #     max_key = max(hashmap, key=hashmap.get)
        #     result.append(max_key)
        #     # remove it from the hashmap, to avoid getting picked in the next iteration
        #     del hashmap[max_key]
        # return result

        #the above is my solution, we can have a much simpler solution using Counter
        hashmap = Counter(nums)
        top_k = hashmap.most_common(k)
        result = []
        for key, count in top_k:
            result.append(key)
        return result
