print("restoreString")

class Solution:
    def restoreString(self, s, indices) -> str:
        str = ""
        strlist = {}
        for v in range(len(indices)):
            strlist[indices[v]] = s[v]
        strlist = sorted(strlist.items())
        for v in strlist:
            str += v[1]
        return str

string = "codeleet"
indices = [4,5,6,7,0,2,1,3]
s = Solution()
print(s.restoreString(string,indices))