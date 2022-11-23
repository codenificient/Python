class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.children = {}


class Trie:
    
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

            node.is_word = True

    def dfs(self, node, pre):

        if node.is_word:
            self.output.append((pre + node.char))


        for child in node.children.values():
            self.dfs(child, pre + node.char)


    def search(self, target):

        node = self.root

        for char in target:
            if char in node.children:
                node = node.children[char]

            else:
                return []

        self.output = []
        self.dfs(node, target[:-1])

        return self.output


if __name__ == "__main__":
    tr = Trie()
    tr.insert("here")
    tr.insert("hear")
    tr.insert("he")
    tr.insert("hola")
    tr.insert("mundo")
    tr.insert("express")
    tr.insert("como")
    tr.insert("her")

    print(tr.search("he"))
    print(tr.search("ho"))
    print(tr.search("exp"))
