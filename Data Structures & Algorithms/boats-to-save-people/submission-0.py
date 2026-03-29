class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        #[1,2,4,5] [1,2,2,3,3]
        boat_counter = 0
        while l <= r:
            remain = limit - people[r]
            r -= 1
            boat_counter += 1
            if l <= r and remain >= people[l]:
                l += 1
        return boat_counter
            
                
