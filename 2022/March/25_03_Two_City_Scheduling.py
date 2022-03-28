class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        dif_costs = {}
        difs = []
        
        for i,cost in enumerate(costs):
            dif = cost[0] - cost[1]
            difs.append(dif)
            if dif not in dif_costs:
                dif_costs[dif] = [i]
            else:
                dif_costs[dif].append(i)
        
        qtd = len(costs) / 2
        res = 0
        index = 0
        
        difs.sort()
        
        for dif in difs:
            costs_indexes = dif_costs[dif]
            while len(costs_indexes) > 0:
                cost_index = costs_indexes.pop(0)
                if index < qtd:
                    res += costs[cost_index][0]
                else:
                    res += costs[cost_index][1]
                index += 1
            
        return res