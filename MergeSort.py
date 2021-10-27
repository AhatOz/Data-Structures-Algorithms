import sys


class MergeSort:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            print(self.merge_sort(array, 0, len(array) - 1))

    def merge_sort(self, array, start, end):
        # base case size == 1
        if end - start + 1 == 1:
            return
        # base case size == 2
        if end - start + 1 == 2:
            # check if elements are out of order
            if array[start] > array[end]:
                # swap if so
                temp = array[start]
                array[start] = array[end]
                array[end] = temp
            return
        # find midpoint
        half = int((start + end) / 2)
        # sort first half
        self.merge_sort(array, start, half)
        # sort second half
        self.merge_sort(array, half + 1, end)
        # merge halves
        self.merge(array, start, half, end)
        print(str(array))
        return array

    def merge(self, array, start, half, end):
        temparray = []
        for i in range(end - start + 1):
            temparray.append(0)
        ind1 = start
        ind2 = half + 1
        newind = 0
        ind1 = start
        ind2 = half + 1
        newind = 0
        while ind1 <= half and ind2 <= end:
            if array[ind1] < array[ind2]:
                # print(len(temparray), len(array), newind, ind1)
                temparray[newind] = array[ind1]
                ind1 += 1
            else:
                temparray[newind] = array[ind2]
                ind2 += 1
            newind += 1
        while ind1 <= half:
            temparray[newind] = array[ind1]
            ind1 += 1
            newind += 1
        while ind2 <= end:
            temparray[newind] = array[ind2]
            ind2 += 1
            newind += 1
        for i in range(len(temparray)):
            array[i + start] = temparray[i]


# main guard
if __name__ == "__main__":
    obj = MergeSort()
    obj.main(sys.argv)
