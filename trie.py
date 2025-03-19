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

    def _search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def search(self, word):
        found = self._search(word)
        print(f"Is Word {word} in the trie?", found)
    
    def matches(self, prefix):
        response = ""
        all = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return "Not found"
            response+=char
            if node.is_end == True:
                all.append(response)
            node = node.children[char]
        self.after_match(node, response, all)
        return all

    def after_match(self, node, response, all):
        matched = response
        keys = list(node.children.keys())
        if node.is_end == True:
            all.append(response)
        for i in range(len(keys)):
            response += keys[i]
            self.after_match(node.children[keys[i]], response, all)
            response = matched

if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "apricot", "autocomplete", "best", "banana", "basket", "car", "cat", "cap",
        "dog", "door", "elephant", "engine", "engineer", "island", "jacket", "keyboard", "house"]
    for word in words:
        trie.insert(word)
    print(trie.all_words())
    prefixes = ["ap", "a", "ba", "ho", "aa", "ca", "jack"]
    for prefix in prefixes:
        print(f"Prefix: {prefix}  Autocomplete: {trie.matches(prefix)}")
    
