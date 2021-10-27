
import sys
import math


class Project:
    @staticmethod
    def main(args):
        pass

    def __init__(self):
        pass

    def quadratic_equation(self, a, b, c):
        if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
            if a != 0 and (b * b) - (4 * a * c) >= 0:
                d = (b * b) - (4 * a * c)
                if (math.sqrt(d) - b) / (2 * a) >= (-math.sqrt(d) - b) / (2 * a):
                    x = (math.sqrt(d) - b) / (2 * a)
                else:
                    x = (-math.sqrt(d) - b)
            else:
                raise ValueError()
        else:
            raise TypeError("Not correct type!")

        return x

    def time_difference(self, start_hour, start_minute, start_second, end_hour, end_minute, end_second):
        if isinstance(start_hour, int) and isinstance(start_minute, int) and isinstance(start_second, int) and isinstance(end_hour, int) and isinstance(end_minute, int) and isinstance(end_second, int):
            if not (start_hour >= 0 and start_hour <= 23 and end_hour >= 0 and end_hour <= 23):
                raise ValueError()
            if not (start_minute >= 0 and start_minute <= 59 and end_minute >= 0 and end_minute <= 59):
                raise ValueError()
            if not (start_second >= 0 and start_second <= 59 and end_second >= 0 and end_second <= 59):
                raise ValueError()
            else:
                if end_hour > start_hour:
                    start_time = start_hour * 3600 + start_minute * 60 + start_second
                    end_time = end_hour * 3600 + end_minute * 60 + end_second
                    x = end_time - start_time
                elif end_minute > start_minute:
                    start_time = start_hour * 3600 + start_minute * 60 + start_second
                    end_time = end_hour * 3600 + end_minute * 60 + end_second
                    x = end_time - start_time
                elif end_second > start_second:
                    start_time = start_hour * 3600 + start_minute * 60 + start_second
                    end_time = end_hour * 3600 + end_minute * 60 + end_second
                    x = end_time - start_time
                else:
                    raise ValueError()

        else:
            raise TypeError()
        return x

    def base_converter(self, value, base):
        if isinstance(value, str):
            if value.isdigit():
                if isinstance(base, int):
                    if base > 1 and base <= 10:
                        new_value = 0
                        base_place = 1
                        i = len(value) - 1
                        for digit in value:
                            digit = int(digit)
                            if digit >= base:
                                raise ValueError()
                            base_place = base ** i
                            new_value += digit * base_place
                            i -= 1
                    else:
                        raise ValueError()
                else:
                    raise TypeError()

            else:
                raise ValueError()
        else:
            raise TypeError()
        return new_value

    def is_palindrome(self, sentence):
        is_palindrome = True
        if isinstance(sentence, str):
            if len(sentence) >= 1:
                for char in sentence:
                    if char.isdigit():
                        raise ValueError()
                    if char.isupper():
                        raise ValueError()
                    if char == '\t' or char == '\r' or char == '\n':
                        raise ValueError()
                for i in range(len(sentence)):
                    def reverse(s):
                        str = ""
                        for i in s:
                            str = i + str
                        return str
                    if sentence[:i+1] != (reverse(sentence[-i-1:])):
                        is_palindrome = False
            else:
                raise ValueError()
        else:
            raise TypeError()
        return is_palindrome

    def is_cycle(self, array):
        if len(array) < 1:
            raise ValueError()
        for k in array:
            if k >= len(array):
                raise ValueError()
        if type(array) != list or not(isinstance(num, int) for num in array):
            raise TypeError()
        seen = []
        for i in range(len(array)):
            seen.append(False)
        cnt = 0
        element = array[0]
        newarray = []
        for i in array:
            newarray.append(element)
            a = newarray.count(element)
            if a >= 2:
                return False
            if array[element] in array:
                element = array[element]
                seen[cnt] = True
            cnt += 1
        for cond in seen:
            if not cond:
                return False
        return True


if __name__ == "__main__":
    Project.main(sys.argv)