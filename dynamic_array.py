import ctypes


class DynamicArray:

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if (0 > index or index >= self.n):
            return IndexError("Index is out of the range")
        return self.A[index]

    def append(self, item):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = item
        self.n += 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for index in range(self.n):
            B[index] = self.A[index]
        self.A = B
        self.capacity = new_capacity
    
    def make_array(self, capacity):
        return (capacity*ctypes.py_object)()



arr = DynamicArray()
arr.append(1)
print(f'array : {arr.A}, item:{arr[0]}, item count : {arr.n}, array capacity:{arr.capacity}')
arr.append(2)
print(f'array : {arr.A}, item:{arr[1]}, item count : {arr.n}, array capacity:{arr.capacity}')
arr.append(3)
print(f'array : {arr.A}, item:{arr[2]}, item count : {arr.n}, array capacity:{arr.capacity}')
arr.append(4)
print(f'array : {arr.A}, item:{arr[3]}, item count : {arr.n}, array capacity:{arr.capacity}')
arr.append(5)
print(f'array : {arr.A}, item:{arr[4]}, item count : {arr.n}, array capacity:{arr.capacity}')



#Question: Word Split
input = ["deeplearning", "d,dll,a,deep,dee,base,lear,learning"]
output = ["deep,learning"]

def word_split(input):
    word_alphabets= list(input[0])
    pattern_list = input[1].split(",")
    for index in range(1, len(word_alphabets)):
        word_list = word_alphabets[:]
        word_list.insert(index, " ")
        first,second = "".join(word_list).split()
        if first in pattern_list and second in pattern_list:
            return [first,second]


print(word_split(input))