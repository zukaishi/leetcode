class Solution:
    def findCenter(self, edges) -> int:
        list = []
        ans = 0
        for v in edges:
            if v[0] in list:
                ans = v[0]
                break
            elif v[1] in list:
                ans = v[1]
            list.insert(0,v[0])
            list.insert(0,v[1])
        return ans

int_list = [[1,2],[2,3],[4,2]]
s = Solution()
test = s.findCenter(int_list)
print(test)
