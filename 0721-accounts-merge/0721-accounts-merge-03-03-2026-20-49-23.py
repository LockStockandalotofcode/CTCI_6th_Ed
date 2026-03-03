class UnionFind:

    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i]) # Path compression
            # all nodes are made to directly point to the root node for quicker lookups
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for i in range(1, len(account)):
                email = account[i]
                email_to_name[email] = name
                uf.union(first_email, email)
            
        # Group emails by their root parent
        components = {}
        for email in email_to_name:
            root = uf.find(email)
            if root not in components:
                components[root] = []
            components[root].append(email)
        
        # Format final output as desired, emails sorted
        result = []
        for root in components:
            result.append([email_to_name[root]] + sorted(components[root]))
        
        return result