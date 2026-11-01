import heapq
class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj=[]
        for i in range(n):
            adj.append([])
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist=[float('inf')] * n
        ways=[0] * n
        MOD=10**9+7

        dist[0]=0
        ways[0]=1       
        min_heap=[(0,0)]
        while min_heap:
            curr_dist,node=heapq.heappop(min_heap)
            if curr_dist > dist[node]:
                continue
            for ne,w in adj[node]:
                new_dist = curr_dist + w

                if new_dist < dist[ne]:
                    dist[ne] = new_dist
                    ways[ne] = ways[node]
                    heapq.heappush(min_heap,(new_dist,ne))
                elif new_dist == dist[ne]:
                    ways[ne] = (ways[ne] + ways[node]) % MOD
        return ways[n-1]
