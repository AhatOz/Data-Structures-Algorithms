
class MyStack:
    def top(self):
        return self.__top

    def array(self):
        return self.__array

    def __init__(self, capacity=10):
        self.__array = [None] * capacity
        self.__top = -1
        if not(isinstance(capacity, int)):
            raise TypeError()
        if capacity <= 0:
            raise ValueError()

    @property
    def size(self):
        return (self.__top + 1)

    @property
    def capacity(self):
        return len(self.__array)

    @property
    def is_full(self):
        return (self.__top + 1) == len(self.__array)

    @property
    def is_empty(self):
        return self.__top == -1

    @property
    def debug_array(self):
        return self.__array

    @property
    def debug_top(self):
        return self.__top

    def push(self, value):
        if (self.__top + 1) == len(self.__array):
            raise RuntimeError
            return
        else:
            self.__top += 1
            self.__array[self.__top] = value

    def pop(self):
        if self.__top == -1:
            raise RuntimeError()
            return
        else:
            self.__top -= 1
            return self.__array[self.__top + 1]

    def peek(self):
        if self.__top == -1:
            raise RuntimeError()
            return
        else:
            return self.__array[self.__top]

    def double_capacity(self):
        newstack = [None] * (len(self.__array) * 2)
        for i in range(len(self.__array)):
            newstack[i] = self.__array[i]
        self.__array = newstack

    def half_capacity(self):
        if (self.__top + 1) > (len(self.__array) / 2):
            raise RuntimeError()
        newstack = [None] * (len(self.__array) // 2)
        for i in range(len(newstack)):
            newstack[i] = self.__array[i]
        self.__array = newstack

# need to fix
    def copy(self):
        capacity = len(self.__array)
        stack = MyStack(capacity)
        for elem in self.__array:
            stack.push(elem)
            return stack
#         stack.push(self.__array)

    def find(self, value):
        for i in range(len(self.__array)):
            if self.__array[i] == value:
                return (len(self.__array) - 1 - i)
        return -1

    def __str__(self):
        output = ""
        for i in range(self.__top + 2):
            if i == 0:
                pass
            else:
                output = output + str(self.__array[-(i)]) + "\n"
        return output

    @staticmethod
    def test():
        stack = MyStack(10)
        print("===EMPTY STACK===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))

        for i in range(0, 20, 2):
            stack.push(i)

        print("===ADD 10 ELEMENTS===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
        print("{}".format(stack))

        print("===FIND===")
        print("Depth of 16: {}".format(stack.find(16)))
        print("Depth of 12: {}".format(stack.find(12)))
        print("Depth of  8: {}".format(stack.find(8)))
        print("Depth of  4: {}".format(stack.find(4)))
        print("Depth of  5: {}".format(stack.find(5)))

        stack.double_capacity()

        print("===DOUBLE===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))

        stack.half_capacity()

        print("===HALF===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))

        stack2 = stack.copy()

        print("===COPY===")
        print("Stack 1 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
        print("{}".format(stack))
        print("Stack 2 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack2.size, stack2.capacity, stack2.is_empty, stack2.is_full))
        print("{}".format(stack2))

        print("===PEEK===")
        print("{}".format(stack.peek()))

        print("===POP===")
        while not stack.is_empty:
            print("{}".format(stack.pop()))

        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
