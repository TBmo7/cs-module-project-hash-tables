class Solution:
    def numJewelsInStones(self, J: str, S:str) -> int:
        j = set(list(J))
        numJewels = 0
        for s in S:
            numJewels += if s in j else 0
        return numJewels