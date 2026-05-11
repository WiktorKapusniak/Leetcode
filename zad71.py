class Solution:
    def simplifyPath(self, path: str) -> str:
        cumulate = ""
        for i in path:
            if cumulate and i == '/' and cumulate[-1]== '/':
                continue
            else: cumulate+=i
        stack = []

        splitted_path = path.split("/")
        splitted_path = [x for x in splitted_path if x!= '' ]

        for i in splitted_path:
            if i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else: stack.append(i)
        return "/"+"/".join(stack)

    
        

sol = Solution()
print(sol.simplifyPath("/home/user/Documents/../Pictures"))
