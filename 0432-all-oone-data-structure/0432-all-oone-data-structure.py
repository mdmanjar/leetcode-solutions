from collections import defaultdict
import heapq


class node:
    def __init__(self,key=-1,freq=0):
        self.key=key
        self.freq=freq
        self.prev=None
        self.next=None

class dll:

    def __init__(self):
        self.head=node()
        self.tail=node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0


    def append(self,new_node):
        new_node.next=self.head.next
        new_node.prev=self.head
        self.head.next.prev=new_node
        self.head.next=new_node
        self.size+=1

    def __len__(self):
        return self.size

    def __delitem__(self, deleted_node):
        deleted_node.prev.next=deleted_node.next
        deleted_node.next.prev=deleted_node.prev
        self.size-=1

    def mru(self):
      return self.head.next.key
    def __str__(self):
        if len(self)==0:
          return '[]'
        ans=[]
        t=self.head.next
        sz=self.size
        while sz:
          ans.append(f'{t.key} : {t.freq+1}')
          sz-=1
          t=t.next
        return ', '.join(str(e) for e in ans)


class AllOne:
    def __init__(self):
      self.mp=defaultdict(lambda:None)
      self.stacks=[]
      self.hp=[]

    def inc(self, key: str) -> None:

      old_node=self.mp[key]

      if old_node:
        index=old_node.freq
        del self.stacks[index][old_node]
        index+=1

      else:
        index=0

      while len(self.stacks)<=index:
        self.stacks.append(dll())


      new_node=node(key,index)
      self.mp[key]=new_node
      self.stacks[index].append(new_node)
      if len(self.stacks[index])==1:
        heapq.heappush(self.hp,index)


    def dec(self, key: str) -> None:
      if key not in self.mp:return
      old_node=self.mp[key]
      index=old_node.freq
      del self.stacks[index][old_node]
      if index==0:
        del self.mp[key]
        return
      old_node.freq=index-1
      self.stacks[index-1].append(old_node)
      heapq.heappush(self.hp,index-1)

    def getMaxKey(self) -> str:
      while self.stacks and not self.stacks[-1]:
        self.stacks.pop()
      if not self.stacks:return ''
      return self.stacks[-1].mru()


    def getMinKey(self) -> str:

        if not self.stacks:

          if self.hp:self.hp.clear()
          return ''

        while self.hp:

          top=self.hp[0]

          if top>=len(self.stacks):
            self.hp=[]
            break

          if self.stacks[top]:break
          heapq.heappop(self.hp)

        if not self.hp:
          return ''

        return self.stacks[self.hp[0]].mru()

    def __str__(self):
      return '\n'.join(e.__str__() for e in self.stacks if e)