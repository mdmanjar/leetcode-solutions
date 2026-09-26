class Node:
    def __init__(self,key=-1,value=-1):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0
        self.mp={}
    
    def __add(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        self.size+=1
    
    def __remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.size-=1
    
    def __len__(self):return self.size
        

    def get(self, key: int) -> int:
        if key not in self.mp:return -1
        v=self.mp[key]
        if self.head.next!=v:
            self.__remove(v)
            self.__add(v)
        return v.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.get(key)
            self.mp[key].value=value
            return
        x=Node(key,value)
        self.mp[key]=x
        self.__add(x)
        if len(self)>self.capacity:
            x=self.tail.prev
            self.__remove(x)
            del self.mp[x.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)