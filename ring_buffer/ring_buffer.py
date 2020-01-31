from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.current = self.storage.add_to_tail(item)
        elif len(self.storage) == self.capacity:
            if self.current.next == None:
                self.storage.remove_from_head()
                self.current = self.storage.add_to_head(item)
            else:
                self.current.next.delete()
                self.current = self.current.insert_after(item)
        else:
            print('I honestly dont know how this could have happened')

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        def rec_func(node):
            nonlocal list_buffer_contents
            if not node:
                return []
            elif node == self.storage.tail and node:
                list_buffer_contents += [node.value]
            elif node:
                list_buffer_contents += [node.value]
                rec_func(node.next)
        rec_func(self.storage.head)

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
