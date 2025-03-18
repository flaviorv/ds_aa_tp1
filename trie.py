class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def all_words(self):
        def _dfs(node, prefix, words):
            if node.is_end:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)
        words = []
        _dfs(self.root, "", words)
        return words
    
    def all_levels(self):
        levels = {}
        def _dfs(node, level=0):
            if node.children:
                level+=1
                if level in levels.keys():
                    levels[level] += [key for key in node.children.keys()]
                else:
                    levels[level] = [key for key in node.children.keys()]
            for char, child in node.children.items():
                if not child:
                    level-=1             
                _dfs(child, level)            
        _dfs(self.root)
        return levels

if __name__ == "__main__":
    trie = Trie()
    words = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
    for word in words:
        trie.insert(word)
    print(trie.all_words())
    for level, chars in trie.all_levels().items():
        print("Level", level, "Chars", chars)
    
    