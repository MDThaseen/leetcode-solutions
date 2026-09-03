class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0,len(s) -1
        while(l<r):
            s[l], s[r] = s[r], s[l]
            l ,r  = l+1 , r-1

        # stack
        # stack = []
        # for c  in s:
        #     stack.append(c)
        # i=0
        # while stack:
        #     s[i] = stack.pop()
        #     i+=1

        # def rev(l, r):
        #     if l < r:
        #         s[l], s[r] = s[r], s[l]
        #         rev(l + 1, r - 1)
        # rev(0 , len(s)-1)
