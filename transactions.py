from json import dumps

class TransactionNode:
    def __init__(self,data):
        self.__txn_data = data
        self.prev=None
        self.next=None

    @property
    def txn_data(self):
        return self.__txn_data

    @txn_data.setter
    def txn_data(self,val):
        if self.__txn_data:
            return
        self.__txn_data = val


class Transactions:
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
    
    def reset(self):
        self.__head = self.__tail = None

    def append(self,data):
        txn = TransactionNode(data)
        self.length+=1
        if self.__head is None and self.__tail is None:
            self.__head = self.__tail = txn
        else:
            self.__tail.next = txn
            txn.prev = self.__tail
            self.__tail = txn
    
    def transactions(self):
        txns = []
        current = self.__head
        while current:
            txns.append(current.txn_data)
            current = current.next
        return txns

    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
            
        


