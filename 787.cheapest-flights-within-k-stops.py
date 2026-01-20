#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
       
        for u, v, w, in flights:
            graph[u].append((v,w))

        dist = {i: float('inf') for i in range(1, n+1)}

        dist[src] = 0
        heap = [(0, src, 0)]

        while heap:
            price, node, stops = heapq.heappop(heap)

            if node == dst:
                return price

            if stops > k:
                continue

            for nei, weight in graph[node]:
                new_price = price + weight
                if (nei, stops+1) not in dist or new_price < dist[(nei, stops+1)]:
                    dist[(nei, stops+1)] = new_price
                    heapq.heappush(heap, (new_price, nei, stops+1))

        return -1
        
# @lc code=end

