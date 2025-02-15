# Array (mutable, resizable)
class Array:

    # Declare the necessary values used for the Array
    _capacity = None
    _size = None
    _array = None

    # Initialize these values with the capacity chosen
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    # Return the current size of the Array (how many items are in it)
    def get_size(self):
        return self._size

    # Return the current capacity of the Array (how many items it can hold)
    def get_capacity(self):
        return self._capacity

    # Return whether the Array is empty (True) or not (False)
    def is_empty(self):
        return True if self._size == 0 else False

    # Return the item at a given index, if the index is within bounds
    def at(self, index):
        if index < 0 or index >= self._size:      # Check if index is out of bounds
            raise IndexError('Must enter a valid index')
        return self._array[index]

    # Return the index of the item we're searching for within our array, return -1 if not found
    def find(self, item):
        for i in range(self._size):
            if self._array[i] is item:            # Check if current value of array is strictly equal to the given item
                return i                          # Found the item, return its index
        return -1                                 # Didn't find the item, return -1

    # Push an item to the end of the array
    def push(self, item):
        if self._size == self._capacity:          # Check if array size is at max capacity, adjust accordingly
            self._resize(self._capacity * 2)
        self._array[self._size] = item
        self._size += 1

    # Insert an item in the desired index of the array
    def insert(self, index, item):
        if index < 0 or index > self._size:       # Check if index is out of bounds
            raise IndexError('Must enter a valid index (for contiguous memory)')
        if self._size == self._capacity:          # Check if array size is at max capacity, adjust accordingly
            self._resize(self._capacity * 2)
        if not index == self._size:               # Check if the index I chose is the tail of my current array
            self._shift_indexes(index, True)      # If it is not the tail, shift the indexes accordingly
        else:
            self._size += 1                       # Update size manually, because ._shift_indexes wasn't called
        self._array[index] = item

    # Prepend an item at the head of the array
    def prepend(self, item):
        if self._size == self._capacity:          # Check if array size is at max capacity, adjust accordingly
            self._resize(self._capacity * 2)
        if not self.is_empty():                   # Check if array is empty, aka size is 0
            self._shift_indexes(0, True)          # If it is not empty, shift the indexes accordingly
        else:
            self._size += 1                       # Update size manually, because ._shift_indexes wasn't called
        self._array[0] = item

    # Pop the tail of the array and return it
    def pop(self):
        _temp_tail = self._array[self._size - 1]  # Store the tail of the array in a variable so we can return it later
        self._array[self._size - 1] = None        # Remove the tail of the array
        self._size -= 1
        if self._size <= self._capacity / 4:      # Check if array size is 1/4 of max capacity, adjust accordingly
            self._resize(int(self._capacity / 2))
        return _temp_tail

    # Delete the item at the given index of the array and return it
    def delete(self, index):
        if index < 0 or index >= self._size:      # Check if index is out of bounds
            raise IndexError('Must enter a valid index')
        _temp_deleted = self._array[index]        # Store the deleted item of the array in a variable to return later
        self._array[index] = None                 # Delete the item at the given index
        if not index == self._size - 1:           # If the index is not the tail, will have to shift indexes
            self._shift_indexes(index, False)
        else:
            self._size -= 1                       # Update size manually, because ._shift_indexes wasn't called
        if self._size <= self._capacity / 4:      # Check if array size is 1/4 of max capacity, adjust accordingly
            self._resize(int(self._capacity / 2))
        return _temp_deleted

    # Remove the item with the value passed in, and return its index
    def remove(self, item):
        _found_index = self.find(item)            # Store the index returned from .find() in a variable
        if _found_index is -1:                    # Check if the returned index is -1, if so, raise a ValueError
            raise ValueError('Item not found, please enter a valid value')
        self._array[_found_index] = None          # Remove the item from the array
        if not _found_index == self._size - 1:    # If the index found is not the tail, will have to shift indexes
            self._shift_indexes(_found_index, False)
        else:
            self._size -= 1                       # Update size manually, because ._shift_indexes wasn't called
        if self._size <= self._capacity / 4:      # Check if array size is 1/4 of max capacity, adjust accordingly
            self._resize(int(self._capacity / 2))
        return _found_index

    # (Private) Resize the array with the given (new) capacity
    def _resize(self, new_capacity):
        _temp_array = [None] * new_capacity       # Allocate desired memory to a temporary array
        for i in range(self._size):
            _temp_array[i] = self._array[i]       # Copy each value from the original array to the temporary array
        self._array = _temp_array                 # Update the original array to its resized version
        _temp_array = None                        # Deallocate memory from temporary array
        self._capacity = new_capacity             # Update the capacity so it matches the resized array

    # (Private) Shift indexes to the right, or to the left, and update the array's size
    def _shift_indexes(self, start_index, shift_right):
        if shift_right is True:                             # Shift indexes to the right
            for i in range(self._size, start_index, -1):    # Start from the tail of the array
                self._array[i] = self._array[i-1]
            self._size += 1
        if shift_right is False:                            # Shift indexes to the left
            for i in range(start_index, self._size - 1):    # Start from the index passed in
                self._array[i] = self._array[i+1]
            self._size -= 1
