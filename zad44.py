class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        while len(s)>0:
            
            if p[i].isalpha():
                if s[i] == p[i]:
                    s = s[1:]
                    p = p[1:]
                else: return False

            elif p[i] == '?':
                s = s[1:]
                p = p[1:]

            elif p[i] == '*':
                if p == '*':
                    return True
                else:



        if s=="" and p=="":
            return True

        