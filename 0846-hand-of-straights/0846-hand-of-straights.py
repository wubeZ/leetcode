class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        
        length = len(hand)
        
        if length % groupSize != 0:
            return False
        
        counter = Counter(hand)
        
        for h in hand:
            if counter[h] == 0:
                continue
            for i in range(groupSize):
                new_h = h + i
                if counter[new_h] == 0:
                    return False
                else:
                    counter[new_h] -= 1
        
        
        return True