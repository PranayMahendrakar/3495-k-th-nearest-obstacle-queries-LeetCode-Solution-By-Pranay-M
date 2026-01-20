class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        import heapq
        result = []
        max_heap = []  # max heap (using negative values)
        
        for x, y in queries:
            dist = abs(x) + abs(y)  # Manhattan distance
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, -dist)
            elif dist < -max_heap[0]:
                heapq.heapreplace(max_heap, -dist)
            
            if len(max_heap) < k:
                result.append(-1)
            else:
                result.append(-max_heap[0])
        
        return result