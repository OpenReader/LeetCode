class Solution:
    def calculate(self, s: str) -> int:
        ret = 0
        st = []
        i = 0
        L = len(s)
        flag = False
        while i < L:
            if s[i].isdigit():
                num = 0
                while i < L and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                st.append(num)
                if flag:
                    b, o, a = st.pop(), st.pop(), st.pop()
                    if o == '*':
                        st.append(a * b)
                    elif o == '/':
                        st.append(a // b)
                    flag = False
            
            elif s[i] == '+' or s[i] == '-':
                st.append(s[i])
                i += 1
                
            elif s[i] == '*' or s[i] == '/':
                st.append(s[i])
                flag = True
                i += 1
            else:
                i += 1
         
        if len(st) == 1:
            return st[0]
        
        st.reverse()
        while st:
            a, o, b = st.pop(), st.pop(), st.pop()
            if o == '+':
                st.append(a+b)
            elif o == '-':
                st.append(a-b)
            if len(st) == 1:
                ret = st[0]
                break
                
        return ret