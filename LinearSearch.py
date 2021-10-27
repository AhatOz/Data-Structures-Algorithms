import sys


class LinearSearch:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            value = int(scanner.readline())
            print(self.linear_search(value, array))

    def linear_search(self, value, array):
        for i in range(len(array)):
            if array[i] == value:
                return i
#             elif len(array) == len(set(array)):
#                 return len(array)
        return -1


# main guard
if __name__ == "__main__":
    obj = LinearSearch()
    obj.main(sys.argv)
