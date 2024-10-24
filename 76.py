class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        y, w = {}, {}
        for c in t:
            y[c] = 1 + y.get(c, 0)

        have, need = 0, len(y)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            w[c] = 1 + w.get(c, 0)

            if c in y and w[c] == y[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                w[s[l]] -= 1
                if s[l] in y and w[s[l]] < y[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""