from MyQueue import *
import sys


class PermutationGenerator:
    def __init__(self):
        pass

    def permutations(self, input):
        q = MyQueue(self.factorial(len(input)))
        q.enqueue("")
        output = [None] * (self.factorial(len(input)))
        index = 0
        while not q.is_empty:
            item = q.dequeue()
            if len(item) == len(input):
                output[index] = item
                index += 1
            else:
                for char in input:
                    if char not in item:
                        q.enqueue(item + char)
#                         print(item, "+", char)
        output = sorted(output)
        return output

    def factorial(self, number):
        fact = 1
        if (isinstance(number, int)):
            if number >= 0:
                for i in range(1, number + 1):
                    fact = fact * i
        return fact

    @staticmethod
    def main(args):
        """ Method to test PermutationGenerator operations

        This is called when the generator is executed as a
        a standalone script

        It will simply pass the contents of the input file to the
        permutations function and print the result

        Params:
        -------
        args: the command-line arguments
        """
        generator = PermutationGenerator()
        with open(args[1]) as scanner:
            print(generator.permutations(scanner.readline()))


if __name__ == "__main__":
    PermutationGenerator.main(sys.argv)