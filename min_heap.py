# Course: CS261 - Data Structures
# Assignment 5 - Hash Map and Min Heap Implementation (Portfolio Assignment)
#   Part 2 - Min Heap
# Student: Steven Ouk
# Description: Implement the MinHeap class by completing the provided skeleton code.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        params: A node (object)
        returns: None
        Adds a new object to the MinHeap maintaining heap property.
        Runtime complexity must be O(logN).
        """
        # put the element at the end of the array
        self.heap.append(node)
        index = self.heap.length() - 1
        while index:
            # compute the inserted element’s parent index ((i - 1) / 2)
            p_index = (index-1)//2
            p_node = self.heap.get_at_index(p_index)
            # compare the value of the inserted element with the value of its parent
            if p_node <= node:  # if node is in the correct spot, return
                return
            # else, swap the node and parent node
            self.heap.swap(index, p_index)
            index = p_index
        

    def get_min(self) -> object:
        """
        params: None
        returns: An object
        Returns an object with a minimum key without removing it from the heap.
        Runtime complexity must be O(1).
        """
        if self.heap.length() == 0:
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        params: None 
        returns: An object
        Returns an object with a minimum key and removes it from the heap.
        Runtime complexity must be O(logN).
        """
        if self.heap.length() == 0:
            raise MinHeapException
        elif self.heap.length() == 1:     # if only one element, remove it and return it
            node = self.heap.get_at_index(0)
            self.heap = DynamicArray()
            return node
        elif self.heap.length() == 2:     # if there are two elements left
            node = self.heap.get_at_index(0)
            self.heap.swap(0, 1)
            self.heap.pop()
            return node
        node = self.heap.get_at_index(0)
        index = 0
        # replace the value of the first element in the array with the value of the last element
        self.heap.swap(0, self.heap.length()-1)
        node2 = self.heap.get_at_index(0)
        # remove the last element of the array
        self.heap.pop()
        # initialize first children indices of array
        left, right = 1, 2
        # add a check to see if children exist at these indices
        if right > self.heap.length() - 1:
            right = None
        while left or right:
            if left and not right:      # if only left child
                minimum = self.heap.get_at_index(left)
                new_index = left
            elif not left and right:    # if only right child
                minimum = self.heap.get_at_index(right)
                new_index = right
            # if right child is smaller than left child
            elif self.heap.get_at_index(right) < self.heap.get_at_index(left):
                minimum = self.heap.get_at_index(right)
                new_index = right
            else:
                minimum = self.heap.get_at_index(left)
                new_index = left
            if node2 > minimum:  # if replacement node is greater than the min child's value, swap
                self.heap.swap(index, new_index)
                # set the current index to the new index
                index = new_index
                left_child = 2 * index + 1
                right_child = left_child + 1
                # if neither child exists in the array
                if left_child > self.heap.length() - 1:
                    break
                # if only the left child exists
                elif right_child > self.heap.length() - 1:
                    right = None
                    left = left_child
                else:   # if both children exist
                    left = left_child
                    right = right_child
            else:
                return node
        return node


    def build_heap(self, da: DynamicArray) -> None:
        """
        params: A DynamicArray
        returns: None
        Receives a DynamicArray with objects in any order and builds a proper MinHeap from them.
        Current content of the MinHeap is lost.
        Runtime complexity must be O(N).
        """
        self.heap = DynamicArray()
        for i in da:
            self.heap.append(i)
        if self.heap.length() < 3:
            return
        # look for the last element of the array
        last = self.heap.length() - 1
        # find the parent index and start there
        current = (last - 1) // 2
        while current >= 0:
            node = self.heap.get_at_index(current)
            # calculate indices of child nodes
            left = 2 * current + 1
            right = left + 1
            # if right child doesn't exist
            if right > self.heap.length() - 1:
                # if current node is greater than left child, swap
                if node > self.heap.get_at_index(left):
                    self.heap.swap(current, left)
                # decrement current
                current -= 1
            else:   # if both children exist
                # find the smaller of the two children
                left_child = self.heap.get_at_index(left)
                right_child = self.heap.get_at_index(right)
                if left_child < right_child:
                    minimum = left_child
                    minimum_index = left
                else:
                    minimum = right_child
                    minimum_index = right
                # if current is greater than smallest child, swap
                if node > minimum:
                    self.heap.swap(current, minimum_index)
                    current -= 1
                current -= 1

            



# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
