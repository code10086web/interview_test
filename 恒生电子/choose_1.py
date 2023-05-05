count = 0
for a in range(11):
    for b in range(a+1, 11):
        for c in range(b+1, 11):
            count += 1
print(count)  # 输出：165

class Linklist:
      def __init__(self,value=0,next=None):
          self.value=value
          self.next=next


def reversedLinklist(head):
    pre = None
    cur = head
    while cur:
        after = cur.next
        cur.next=pre
        pre=cur
        cur=after

    return pre

if __name__ == '__main__':
    nodes=[Linklist(i) for i in range(6)]
    for i in range(len(nodes)-1):
        nodes[i].next=nodes[i+1]

    node=nodes[0]
    while node:
        print(node.value)
        node=node.next
    reversed_head=reversedLinklist(nodes[0])
    while reversed_head:
        print(reversed_head.value)
        reversed_head=reversed_head.next
