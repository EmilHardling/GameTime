class Node:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class Bintree:
    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        if self.root:
            self.putta(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size = self.size + 1

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return self.finns(value)

    def write(self):
        # Skriver ut trädet i inorder
        self.skriv(self.root)
        print("\n")

    def putta(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.putta(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self.putta(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, val, parent=currentNode)

    def finns(self, key):
        if self.root:
            res = self._finns(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _finns(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._finns(key, currentNode.leftChild)
        else:
            return self._finns(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.finns(key)


    def skriva(self,currentNode,inorderlist):
        if currentNode == None:
            return
        self.skriva(currentNode.leftChild,inorderlist)
        inorderlist.append(currentNode.key)
        self.skriva(currentNode.rightChild,inorderlist)
