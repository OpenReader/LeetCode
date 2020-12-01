class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.trie
        for c in word:
            cur = cur.setdefault(c, {})
        cur['#'] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def searchTrie(word, i, cur):
            if i == len(word):
                return True if '#' in cur else False
            
            if word[i] in cur:
                return searchTrie(word, i+1, cur[word[i]])
            elif word[i] == '.':
                for c in cur:
                    if c != '#':
                        if searchTrie(word, i+1, cur[c]):
                            return True
            
            return False
        
        return searchTrie(word, 0, self.trie)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)