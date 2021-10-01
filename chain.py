class ChainNode:
    def __init__(self,data):
        self.__data = data
        self.next = None
        self.prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,val):
        self.data = val

class Chain:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.length = 0

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def append(self,data):
        node = ChainNode(data)
        self.length+=1
        if self.__head is None and self.__tail is None:
            self.__head = self.__tail = node
        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node

    def transactions(self):
        chain = []
        current = self.__head
        while current:
            chain.append(current.data)
            current = current.next
        return chain

    