# https://leetcode.cn/problems/implement-trie-prefix-tree/description/

# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

# 请你实现 Trie 类：

#     Trie() 初始化前缀树对象。
#     void insert(String word) 向前缀树中插入字符串 word 。
#     boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
#     boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

 

# 示例：

# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]

# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True

class Node:
    def __init__(self, val, is_end=False):
        self.val = val
        self.is_end = is_end
        self.children = []
class Trie:

    def __init__(self):
        self.root = Node(-1)

    def insert(self, word: str) -> None:
        node = self.root
        
        for i, char in enumerate(word):
            flag = 0
            for child in node.children:
                if char == child.val:
                    node = child
                    if i == len(word)-1:
                        node.is_end = True
                    flag = 1
                    break
            if flag == 0:
                is_end = False if i != len(word)-1 else True
                n1 = Node(char, is_end)
                node.children.append(n1)
                node = n1
                


    def search(self, word: str) -> bool:
        node = self.root
        for i, char in enumerate(word):
            flag = 0

            for child in node.children:
                if char == child.val:
                    if i== len(word)-1: 
                        return child.is_end
                    node = child
                    flag = 1
                    
                    break
            if flag == 0:
                return False
            # if word == 'app':
            #     print(char, flag)
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i, char in enumerate(prefix):
            flag = 0
            for child in node.children:
                if char == child.val:
                    node = child
                    flag = 1
                    
                    break
            if flag == 0:
                return False
        return True

# 执行用时分布
# 141ms
# 击败59.25%使用 Python3 的用户
# 消耗内存分布
# 28.79MB
# 击败91.44%使用 Python3 的用户
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)