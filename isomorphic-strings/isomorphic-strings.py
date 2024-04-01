class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        d1 =  {}

        d2 = {}

        for  i in range(len(s)):

            if s[i] in d1:

                if t[i] != d1[s[i]]:

                    return False
            else:

                d1[s[i]] = t[i]

        for  i in range(len(t)):

            if t[i] in d2:

                if s[i] != d2[t[i]]:

                    return False

            else:

                d2[t[i]] = s[i]

        return True
        