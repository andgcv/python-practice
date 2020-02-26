from my_array import Array

if __name__ == '__main__':
    capacity = 4
    array = Array(capacity)

    print('Array size: {}'.format(array.get_size()))                             # Should return 0
    print('Array capacity: {}'.format(array.get_capacity()))                     # Should return 4
    print('Array is empty: {}'.format(array.is_empty()))                         # Should return True
    # print('Array value at index 0: {}'.format(array.at(0)))                    # Should raise an Exception
    print('Find index of an item: {}'.format(array.find(2)))                     # Should return -1
    array._resize(capacity * 2)  # Accessing a protected member for testing purposes
    print('New capacity after resizing array: {}'.format(array.get_capacity()))  # Should return 8
