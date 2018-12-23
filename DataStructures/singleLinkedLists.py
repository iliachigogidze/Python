class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAt(self, new_node, position):
        current_position = 0
        current_node = self.head
        
        while True:
            if current_position == position:
                previous_node = new_node
                new_node = 

            previous_node = current_node    
            current_node = current_node.next
            current_position += 1
        
        current_node =
            


    def insertEnd(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def insertHead(self, new_node):
        tempNode = self.head
        self.head  = new_node
        self.head.next = tempNode

        del tempNode
    
    def listLength(self):
        pass
    
    def print_list(self):
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next

linkedlist = LinkedList()
n1 = Node('n1')
linkedlist.insertEnd(n1)

n2 = Node('n2')
linkedlist.insertEnd(n2)

n3 = Node('n3')
linkedlist.insertEnd(n3)

n4 = Node('n4')
linkedlist.insertHead(n4)

linkedlist.print_list()























# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def listLength(self):
#         last_node = self.head
#         counter = 0
#         while last_node is not None:
#             last_node = last_node.next
#             counter += 1
#             break


#     def insertHead(self, new_node):
#         tempNode = self.head
#         self.head = new_node
#         self.head.next = tempNode

#         del tempNode

#     def insertAt(self, new_node, position):
#         if position == 0:
#             self.insertHead(new_node)
#             return # es ratoa sachiroo???????/
        
#         if 0 > position > self.listLength():
#             print('Invalid Position!')
#             return # es ratoa sachiroo?????????///

#         current_node = self.head
#         counter = 0
#         while True:
#             if counter == position:
#                 previousNode.next = new_node
#                 new_node.next = current_node
#                 break
#             previousNode = current_node
#             current_node = current_node.next
#             counter += 1
    
#     def insertEnd(self, new_node):
        
#         if self.head is None:
#             self.head = new_node
#         else: # else ra sachiroa????????/
#             last_node = self.head
#             while True:
#                 if last_node.next is None:
#                     break
#                 last_node = last_node.next
#             last_node.next = new_node          
        
#     def print_list(self):
#         current_node = self.head
#         while True:
#             if current_node is None:
#                 break
#             print(current_node.data)
#             current_node = current_node.next



# linkedlist = LinkedList()

# ilia = Node('Ilia')
# linkedlist.insertEnd(ilia)

# nika = Node('nika')
# linkedlist.insertEnd(nika)

# nino = Node('nino')
# linkedlist.insertHead(nino)

# axali = Node('axali')
# linkedlist.insertAt(axali, 2)

# linkedlist.print_list()