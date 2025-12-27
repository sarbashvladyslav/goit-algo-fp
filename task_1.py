class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def reverse_nodes(self):
    prev = None
    curr = self.head

    while curr != None:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    
    self.head = prev

  def insertion_sort_list(self, list):
    sorted_list = None
    curr = list.head

    while curr != None:
        next_node = curr.next
        sorted_list = self.insert_in_sorted_order(sorted_list, curr)
        curr = next_node
    
    self.head = sorted_list
  
  def insert_in_sorted_order(self, sorted_list, node):
    if sorted_list == None or node.data <= sorted_list.data:
        node.next = sorted_list
        return node

    curr = sorted_list

    while curr.next != None and curr.next.data < node.data:
        curr = curr.next

    node.next = curr.next
    curr.next = node

    return sorted_list

  def merge_sorted_list(self, list1, list2):
    new_node = Node()
    end = new_node

    while list1 != None and list2 != None:
        if list1.data <= list2.data:
            end.next = list1
            list1 = list1.next
        else:
            end.next = list2
            list2 = list2.next

        end = end.next

    if list1 != None:
        end.next = list1
    else:
        end.next = list2

    return new_node.next

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

llist = LinkedList()
# llist1 = LinkedList()

# for i in range(10):
#     llist.insert_at_end(i)
#     llist1.insert_at_end(i * 2)
  
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_beginning(18)
llist.insert_at_beginning(35)

llist.insert_at_end(20)
llist.insert_at_end(25)

# llist.print_list()
# llist1.print_list()
# llist.merge_sorted_list(llist.head, llist1.head)
llist.insertion_sort_list(llist)
llist.reverse_nodes()
llist.print_list()