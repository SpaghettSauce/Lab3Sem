class Node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None 

class Tree:
    def __init__(self):
        self.root = None 

    def append(self, obj): 
        if self.root is None: 
            self.root = obj
            return obj

        s, p, fl_find = self.find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def find(self, node, parent, value): 
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True 

        if value < node.data:
            if node.left:
                return self.find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.find(node.right, node, value)

        return node, parent, False 

    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def find_min(self, node, parent):
        if node.left:
            return self.find_min(node.left, node)
        return node, parent


    def del_node(self, key):
        s, p, fl_find = self.find(self.root, None, key)
        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p) # s - текущая вершина, p - родительская для нее
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def show_tree_NLR(self, node): # Прямой обход
        if node is None:
            return

        print(node.data)
        self.show_tree_NLR(node.left)
        self.show_tree_NLR(node.right)

    def show_tree_LNR(self, node): # Цетнральный обход
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_tree_LRN(self, node): # Концевой обход
        if node is None:
            return

        self.show_tree_LRN(node.left)
        self.show_tree_LRN(node.right)
        print(node.data)

    def show_tree_wide(self, root): # Обход в ширину
        if not root:
            return

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop(0)
            print(node.data, end=' ')

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


v = [10, 5, 7, 16, 13, 2, 20]
t = Tree()
for x in v:
    t.append(Node(x))




t.show_tree_wide(t.root)
print(' ')
t.del_node(16)
t.show_tree_wide(t.root)

x = t.find(Node(5),Node(10),5)



print(' ')
t.append(Node(100))
t.show_tree_wide(t.root)