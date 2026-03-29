class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        maxFreq = max(freq.values())
        numMax = list(freq.values()).count(maxFreq)

        frame = (maxFreq - 1) * (n + 1) + numMax
        answer = max(len(tasks), frame)

        return answer
        