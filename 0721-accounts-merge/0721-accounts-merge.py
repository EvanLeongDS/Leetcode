class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        adj = {} # see which accounts are connected to each other
        email_to_name = {}
        for index, account in enumerate(accounts):
            name = account[0]         
            first = account[1]
            for email in account[1:]:  
                if email not in email_to_name:
                    email_to_name[email] = name

                if email not in adj:
                    adj[email] = []
                
                if email != first:
                    adj[first].append(email)
                    adj[email].append(first)
        
        # find the connected graphs using dfs 
        # also establish the big list of lists and return that 
        visited = set()
        big_list = []
        for node in adj.keys():
            if node not in visited:
                combo_list = self.dfs(node, adj, visited)
                big_list.append(combo_list)

        # get the names back into the big list 
        for name_list in big_list:
            name_list.sort()                                          # NEW: sort emails
            owner = email_to_name[name_list[0]]
            name_list.insert(0, owner)
        return big_list

    def dfs(self, node, adj, visited):
        combo_list = []
        visited.add(node)
        combo_list.append(node)

        for adj_node in adj[node]:
            if adj_node not in visited:
                combo_list.extend(self.dfs(adj_node, adj, visited))  # CHANGED: catch child's list
        return combo_list