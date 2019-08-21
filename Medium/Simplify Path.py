class Solution:
    def simplifyPath(self, path):
        s = []
        path_l = path.split('/')
        for i in path_l:
            if i != '/' and i != '..' and i != '.' and i:
                s.append(i)
            if i == '..' and s:
                s.pop()
        return '/'+'/'.join(s)

s = Solution()
print(s.simplifyPath("/home/"))
