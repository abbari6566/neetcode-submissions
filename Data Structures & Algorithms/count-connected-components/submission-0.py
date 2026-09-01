from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #lets try to build the graph first
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        #iterative bfs
        def bfs(start):
            queue = deque([start])
            visited.add(start)

            while queue:
                curNode = queue.popleft()
                
                for neighbor in graph[curNode]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        components = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                components+=1
        return components
'''
Build graph:     O(E)
BFS traversal:   O(V + E)
Total:           O(V + E)
'''       
        