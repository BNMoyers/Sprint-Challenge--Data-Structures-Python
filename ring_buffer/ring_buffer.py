from doubly_linked_list import DoublyLinkedList
# RingBuffer has two methods, `append` and `get`. The `append` method adds elements to the buffer. The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

# _You may not use a Python List in your implementation of the `append` method (except for the stretch goal)_

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        
        elif self.storage.length == self.capacity:
            to_remove = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if to_remove == self.current:
                self.current = self.storage.tail
            
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        current = self.current 
        list_buffer_contents.append(current.value)
                
        if current.next:
            target = current.next
        else:
            target = self.storage.head
        

        while target != current:
            list_buffer_contents.append(target.value)
            if target.next:
                target = target.next
            else: 
                target = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
