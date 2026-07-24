class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #First build an empty adjaceny list
        preMap = {}
        for i in range(numCourses):
            preMap[i] = [] #empty map like {0:[], 1:[]...so on}
        #now map each course to its prereqs
        for crs, pre in prerequisites:
            preMap[crs].append(pre) # {0:[1], 1:[2] ... so on}
        
        visited = set() #to track with course have been check and detect cycles
        
        #traversal with dfs
        def dfs(crs):
            if crs in visited: return False #cyclic like example 2
            if preMap[crs] == []: return True #it means this course can be completed

            #if not base case
            visited.add(crs) #new crs haven't traversed yet
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False #even if we find 1 course that can't be completed return false
            #else it can be completed, set preMap[crs] as empty
            visited.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses): #manually iterate all course as there can be independent graphs
            if dfs(crs) == False: return False
        return True

#time: O(nodes+prereqs) => O(n+p)

        