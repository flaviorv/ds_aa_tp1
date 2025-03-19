class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, ip):
        node = self.root
        for char in ip:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def longest_prefix_match(self, prefix):
        response = ""
        node = self.root
        iterations = 0
        for char in prefix:
            iterations+=1
            if char not in node.children:
                if response == "":
                    return response, iterations
                continue
            response+=char
            node = node.children[char]
        while node.is_end == False:
            iterations+=1
            keys = list(node.children.keys())
            response+=keys[0]
            node = node.children[keys[0]]
        return response, iterations

if __name__ == "__main__":
    trie = Trie()
    networks = ["2001:db8::/32", "2001:db8:1234::/48", "192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]
    for network in networks:
        trie.insert(network)
    prefixes = ["2001:db8", "192.168"]
    for prefix in prefixes:
        print(f"Prefix: {prefix}  Longest prefix match: {trie.longest_prefix_match(prefix)}")
