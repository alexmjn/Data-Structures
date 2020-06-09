from linked_list import LinkedList, Node
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     """This class implements a Queue with Python's built-in array list.
#     """
#     def __init__(self, contents=[]):
#         self.size = 0
#         self.contents = contents

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.contents.append(value)

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             front_item = self.contents.pop(0)
#             return front_item

class Queue:
    """This class implements a queue with linked lists.

    It instantiates an empty queue and builds on LinkedList methods from
    that class in order to add functionality for adding an item to the queue
    (and adjusting the tail appropriately) and removing an item from the queue
    (and adjusting the head appropriately).
    """
    def __init__(self, contents=LinkedList()):
        # Contents is a LinkedList containing nodes
        self.size = 0
        self.contents = contents

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.contents.add_to_tail(value)

    def dequeue(self):
        if self.size >= 1:
            self.size -= 1
            value = self.contents.remove_head()
            return value

        else:
            return None
