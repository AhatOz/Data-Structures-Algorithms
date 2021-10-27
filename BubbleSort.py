import sys


class BubbleSort:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            print(self.bubble_sort(array))

    def bubble_sort(self, array):
        # loop through the array multiple times
        for i in range(len(array)):
            # consider every pair of elements except the sorted ones
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    # swap elements if they are out of order
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
            print(str(array))
        return array


# main guard
if __name__ == "__main__":
    obj = BubbleSort()
    obj.main(sys.argv)
