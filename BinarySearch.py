import sys


class BinarySearch:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            value = int(scanner.readline())
            print(self.linear_search(array, value, 0, len(array) - 1))

    def binary_search(self, array, value, start, end):
        # base case
        if start > end:
            return -1
        mid = int((start + end) / 2)
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            return self.binary_search(array, value, start, mid - 1)
        elif array[mid] < value:
            return self.binary_search(array, value, mid + 1, end)


# main guard
if __name__ == "__main__":
    obj = BinarySearch()
    obj.main(sys.argv)
