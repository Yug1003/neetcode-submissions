class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vis = {}
        for i in nums:
            vis[i] = vis.get(i , 0)+1

        arr = []
        for i , j in vis.items():
            arr.append([j , i])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
