class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        def addLen(s):
            l = len(s)
            b = [chr(l >> i * 8 & 0xff) for i in range(4)]
            b.reverse()
            return ''.join(b) + s
            
        s_l = [addLen(x) for x in strs]
        return ''.join(s_l)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        def getLen(l_s):
            ret = 0
            for c in l_s:
                ret = ret * 256 + ord(c)
            return ret
        
        i, L = 0, len(s)
        s_l = []
        while i < L:
            l_s = s[i : i + 4]
            l = getLen(l_s)
            s_l.append(s[i+4 : i+l+4])
            i += 4 + l
        return s_l


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))