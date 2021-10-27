class MyQueue:
    def start(self):
        return self.__start

    def end(self):
        return self.__end

    def array(self):
        return self.__array

    def __init__(self, capacity=10):
        if not isinstance(capacity, int):
            raise TypeError
        if capacity < 1:
            raise ValueError
        self.__array = [None] * capacity
        self.__start = -1
        self.__end = 0

    @property
    def size(self):
        if self.__start == -1:
            return 0
        elif self.__start == self.__end:
            return len(self.__array)
        elif self.__start < self.__end:
            return (self.__end - self.__start)
        else:
            return len(self.__array) - self.__start + self.__end

    @property
    def capacity(self):
        return (len(self.__array))

    @property
    def is_full(self):
        return self.__start == self.__end

    @property
    def is_empty(self):
        return self.__start == -1

    @property
    def debug_array(self):
        return self.__array

    @property
    def debug_start(self):
        return self.__start

    @property
    def debug_end(self):
        return self.__end

    def enqueue(self, value):
        if self.__start == self.__end:
            raise RuntimeError
        self.__array[self.__end] = value
        self.__end = (self.__end + 1) % len(self.__array)
        if self.__start == -1:
            self.__start = 0

    def dequeue(self):
        if self.__start == -1:
            raise RuntimeError
        item = self.__array[self.__start]
        self.__start = (self.__start + 1) % len(self.__array)
        if self.__start == self.__end:
            self.__start = -1
            self.__end = 0
        return item

    def peek(self):
        if self.__start == -1:
            raise RuntimeError
        else:
            return self.__array[self.__start]

    def find(self, value):
        for i in range(len(self.__array)):
            if self.__array[i] == value:
                return (i)
        return -1

    def double_capacity(self):
        newq = (len(self.__array) * 2) * [None]
        length = self.size
        for i in range(length):
            newq[i] = self.dequeue()
        self.__start = 0
        self.__end = length
        self.__array = newq

    def half_capacity(self):
        if self.size > (len(self.__array) // 2):
            raise RuntimeError
        newq = [None] * (len(self.__array) // 2)
        length = self.size
        for i in range(len(newq)):
            newq[i] = self.__array[i]
        self.__start = 0
        self.__end = length % len(newq)
        self.__array = newq

    # need to fix
    def copy(self):
        capacity = len(self.__array)
        q = MyQueue(capacity)
        for elem in self.__array:
            q.enqueue(elem)
        return q

    def __str__(self):
        output = ""
        for i in range(len(self.__array)):
            next = (self.__start + i) % len(self.__array)
            output += (str(self.__array[next])) + '\n'
        return output

    @staticmethod
    def test():
        """ Method to test Queue operations

        This is called when the queue is executed as a
        a standalone script

        It will call each of the methods of the Queue class
        It DOES NOT check for proper use of exceptions
        """
        queue = MyQueue(10)
        print("===EMPTY QUEUE===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))

        for i in range(0, 20, 2):
            queue.enqueue(i)

        print("===ADD 10 ELEMENTS===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))
        print("{}".format(queue))

        print("===FIND===")
        print("Depth of 16: {}".format(queue.find(16)))
        print("Depth of 12: {}".format(queue.find(12)))
        print("Depth of  8: {}".format(queue.find(8)))
        print("Depth of  4: {}".format(queue.find(4)))
        print("Depth of  5: {}".format(queue.find(5)))

        queue.double_capacity()

        print("===DOUBLE===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))

        queue.half_capacity()

        print("===HALF===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))

        queue2 = queue.copy()

        print("===COPY===")
        print("Queue 1 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))
        print("{}".format(queue))
        print("Queue 2 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue2.size, queue2.capacity, queue2.is_empty, queue2.is_full))
        print("{}".format(queue2))

        print("===PEEK===")
        print("{}".format(queue.peek()))

        print("===POP===")
        while not queue.is_empty:
            print("{}".format(queue.dequeue()))

        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))


# Main Guard
if __name__ == "__main__":
    MyQueue.test()