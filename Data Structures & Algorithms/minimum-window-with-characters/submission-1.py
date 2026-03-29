class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        window = {}
        have = 0
        needCount = len(need) #frequency of distinct needed letters
        res_len = float("inf")
        res_l = 0
        l = 0

        for r, ch in enumerate(s):
            window[ch] = window.get(ch,0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == needCount:
                window_len = r - l + 1
                if window_len < res_len:
                    res_len = window_len
                    res_l = l
                
                left_ch = s[l]
                window[left_ch] -= 1
                l += 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
        return "" if res_len == float("inf") else s[res_l: res_l + res_len]
                

            
