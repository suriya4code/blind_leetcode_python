class Solution:
    def reorganizeString(self, s: str) -> str:
        st = set()
        for i in s:
            st.add(i)

        flag = True

        while flag:
            
            l = st.pop()
            
            st.append(l)

        pass


s = "aab"
print(Solution().reorganizeString(s))  # "aba"