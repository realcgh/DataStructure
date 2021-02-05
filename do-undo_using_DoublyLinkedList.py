class Node(object):
    """ A Doubly-linked lists' node. """
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class dll(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        print('Empty')

    def do(self, data):
        """ Append an item to the list. """

        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        print(self.tail.data)
        """
        sort=sorted(dl.tail.data)
        reverse=list(reversed(dl.tail.data))
        append=dl.do(d.tail.data+[9])

        """
    def iter(self):
        """ Iterate through the list. """
        current = self.head #note subtle change
        cnt=self.count
        while cnt>0:
            val = current.data
            current = current.next
            cnt-=1
            yield val

    def print_all(self):
        """ Print nodes in list from first node inserted to the last . """
        cnt=self.count
        if cnt==0:
            print('Empty')
        else:
            for node in self.iter():
                print(node)

    def print_current(self):
        if self.tail is None:
            print("Empty")
        else:
            print(self.tail.data)

    def undo(self):
        if self.count<=1:
            print('No state for undo')
        elif self.count>1:
            self.tail=self.tail.prev
            self.count-=1
            print(self.tail.data)
            

    def redo(self):
        if self.tail is None:
            print('No state for redo')
        else:
            if self.tail.next is None:
                print('No state for redo')
            else:
                self.tail = self.tail.next
                self.count+=1
                print(self.tail.data)


