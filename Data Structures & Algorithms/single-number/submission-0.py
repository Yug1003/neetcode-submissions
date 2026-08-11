class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited=[]
        for i in nums:
            if i in visited:
                visited.remove(i)
            else:
                visited.append(i)
        return visited[0]