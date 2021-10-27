import sys


class Quicksort:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            print(self.quicksort(array, 0, len(array) - 1))

    def quicksort(self, array, start, end):
        if start >= end:
            return
        pvtind = self.partition(array, start, end)
        self.quicksort(array, start, pvtind - 1)
        self.quicksort(array, pvtind + 1, end)
        print(str(array))
        return array

    def partition(self, array, start, end):
        pvtval = array[end]
        pvtind = start
        for i in range(start, end + 1):
            if array[i] <= pvtval:
                temp = array[i]
                array[i] = array[pvtind]
                array[pvtind] = temp
                pvtind += 1
        return (pvtind - 1)


# main guard
if __name__ == "__main__":
    obj = Quicksort()
    obj.main(sys.argv)
