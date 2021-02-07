class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None


class Tree():
    def __init__(self, root=None):
        self.root = root
        self.size=0

    def get_root(self):
        return self.root

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            self.size=self.size+1
            return
        queue = [self.get_root()]

        while queue:
            this_node = queue.pop(0)

            if this_node.left is not None:
                queue.append(this_node.left)
            else:
                this_node.left = node
                node.parent=this_node
                self.size=self.size+1
                self.bottomSwap(this_node)
                break
            if this_node.right is not None:
                queue.append(this_node.right)
            else:
                this_node.right = node
                node.parent=this_node
                self.size=self.size+1               
                self.bottomSwap(this_node)
                break
 
    def bottomSwap(self,this_node):
                if this_node.right is None:
                    if this_node.data>this_node.left.data:
                        temp=this_node.data
                        this_node.data=this_node.left.data
                        this_node.left.data=temp
                        if this_node.parent is not None:
                            self.bottomSwap(this_node.parent)
                else:
                    if this_node.right.data<this_node.data:
                        temp=this_node.data
                        this_node.data=this_node.right.data
                        this_node.right.data=temp
                    elif this_node.left.data<this_node.data:
                        temp=this_node.data
                        this_node.data=this_node.left.data
                        this_node.left.data=temp
                        if this_node.parent is not None:
                            self.bottomSwap(this_node.parent)

        
			

    def delete_deepest(self, last_node):
        queue = [self.root]
        while queue:
            this_node = queue.pop(0)
            if this_node.left is not None:
                if this_node.left == last_node:
                    this_node.left = None
                    del last_node
                    self.size=self.size-1
                    return
                else:
                    queue.append(this_node.left)
            elif this_node.right is not None:
                if this_node.right == last_node:
                    this_node.right = None
                    del last_node
                    self.size=self.size-1
                    return
                else:
                    queue.append(this_node.right)
            else:
                this_node=None
                self.size=self.size-1

##set root.data=last_node.data and delete last node   dequeue.
    def delete(self):

        if self.root is None:
            return
        elif self.root.left is None and self.root.right is None:
            self.root = None
            self.size=self.size-1
            return
        else:    
            queue = [self.root]
            
            while queue:
                this_node = queue.pop(0)
                if this_node.left is not None:
                    queue.append(this_node.left)
                if this_node.right is not None:
                    queue.append(this_node.right)
                    
            self.root.data = this_node.data # here this node is last node or deepest node
            self.delete_deepest(this_node)


    def swapTop(self):
        if self.root is None:
            return
        else:
            if self.root.left is None and self.root.right is None:
                return
            if self.root.left is not None and self.root.right is None:
                if self.root.data>self.root.left.data:
                    temp=self.root.data
                    self.root.data=self.root.left.data
                    self.root.left.data=temp
            if self.root.left is not None and self.root.right is not None:
                if self.root.left.data>=self.root.right.data:
                    temp=self.root.data
                    self.root.data=self.root.right.data
                    self.root.right.data=temp
                    self.swapNode(self.root.right)
                else:
                    temp=self.root.data
                    self.root.data=self.root.left.data
                    self.root.left.data=temp                
                    self.swapNode(self.root.left)

                    
    def swapNode(self,this_node):
                if this_node.left is None and this_node.right is None:
                    return
                if this_node.left is not None and this_node.right is None:
                    if this_node.data>this_node.left.data:
                        temp=this_node.data
                        this_node.data=this_node.left.data
                        this_node.left.data=temp
                if this_node.left is not None and this_node.right is not None:
                    if this_node.left.data>=this_node.right.data:
                        temp=this_node.data
                        this_node.data=this_node.right.data
                        this_node.right.data=temp
                        self.swapNode(this_node.right)
                    else:
                        temp=this_node.data
                        this_node.data=this_node.left.data
                        this_node.left.data=temp                
                        self.swapNode(this_node.left)
        
        
class PriorityQue(Tree):

    def empty(self):
        if self.root is None:
            print('empty')
        else:
            print('not empty')
            
    def peek(self):
        if self.root is None:
            print('empty')
        else:
            print(self.root.data)
        
    def Enqueue(self,data):
        self.insert(data)
        
    def Dequeue(self):
        if self.root is None:
            print('empty')
        else:
            print(self.root.data)
            self.delete()
            self.swapTop()
        
    def length(self):
        print(self.size)
        

    
