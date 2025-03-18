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
    
    def _all_levels(self):
        levels = {}
        def _get_chilndren(node, parent, level=0):
            if node.children:
                level+=1
                if level in levels.keys():
                    if parent in levels[level].keys():
                        levels[level][parent] += [key for key in node.children.keys()]
                    else:
                        levels[level][parent] = [key for key in node.children.keys()]
                else:
                    levels[level] = {parent : [key for key in node.children.keys()]}
            for char, child in node.children.items():
                if not child:
                    level-=1             
                _get_chilndren(child, char, level)            
        _get_chilndren(self.root, "No parent")
        return levels
    
    def all_levels(self):
        levels = self._all_levels()
        for level in levels:            
            print("Level", level, [f"Parent: {parent}: {chars}"   for parent, chars in levels[level].items()])

if __name__ == "__main__":
    trie = Trie()
    words = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
    for word in words:
        trie.insert(word)
    print(trie.all_words())
    trie.all_levels()
    
    