from my_array import Array

if __name__ == '__main__':
    capacity = 4
    array = Array(capacity)

    print('Array size: {}'.format(array.get_size()))                             # Should return 0
    print('Array capacity: {}'.format(array.get_capacity()))                     # Should return 4
    print('Array is empty: {}'.format(array.is_empty()))                         # Should return True
    array.push(7)
    array.push(30)
    print('Array value at index 0: {}'.format(array.at(0)))                      # Should return 7
    print('Find index of item 30: {}'.format(array.find(30)))                    # Should return 1
    array.push(3)
    array.push(10)
    array.push(2)
    print('New Array size after pushing values: {}'.format(array.get_size()))    # Should return 5
    print('New capacity after resizing Array: {}'.format(array.get_capacity()))  # Should return 8
    print('Array is empty, after pushing values: {}'.format(array.is_empty()))   # Should return False
    print('Array value at index 4, after resizing: {}'.format(array.at(4)))      # Should return 2

