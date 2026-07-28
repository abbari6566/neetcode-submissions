class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #empty graph is a valid tree
        if not n:
            return True

        visit = set()
        #build the adjaceny list
        adj_list = {}
        
        for i in range(n):
            adj_list[i] = []
        for n1, n2 in edges:
            #undirected graph so both edges
            adj_list[n1].append(n2) 
            adj_list[n2].append(n1)
        
        #dfs traversal
        def dfs(cur_node, prev_node):
            if cur_node in visit:
                return False #cycle detected
            
            #else new node found
            visit.add(cur_node)

            #dfs on other nodes from current node (node_val)
            for next_node in adj_list[cur_node]:
                if next_node == prev_node: #same node
                    continue
                if dfs(next_node, cur_node) == False: #detect cycle
                    return False

            return True

        #pass node 0 as first node and first previous node as -1
        #dfs won't check for edges/if graph connected or not
        return dfs(0, -1) and len(visit)==n

#time: O(Edges + vertices) => O(E+V)

        
        