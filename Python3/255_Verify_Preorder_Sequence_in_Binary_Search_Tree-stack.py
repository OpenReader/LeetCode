class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        st = []
        cur_min = float('-inf')
        for n in preorder:
            if n < cur_min:
                return False
            while st and n > st[-1]:
                cur_min = st.pop()
            st.append(n)
        
        return True