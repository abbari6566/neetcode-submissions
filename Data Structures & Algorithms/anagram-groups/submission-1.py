from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a hashmap to store sorted string as key
        #use defaultdict() so that we don't get index error when a 
        #key is not present
        anagrams = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)

        return list(anagrams.values())
    
'''
Time Complexity 
loop n times so O(n)
sorting for each string k log k
building the tuple is k so klogk dominates
Overall becomes O(n.klogk)
'''
      

            


        