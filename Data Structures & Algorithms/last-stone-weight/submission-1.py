class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cue = stones.pop() - stones.pop()

            if cue:
                stones.append(cue)
        
        return stones[0] if stones else 0