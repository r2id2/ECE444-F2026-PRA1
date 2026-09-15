# create utils class
class utils:
    # create reverse function --> will take number and reverse place of all digiits
    # example: 1234 -> 4321
    def reversed(self, number):

        # check if input is int
        if type(number) != int:
            raise TypeError("Input must be an integer")

        # turn number into string
        number = str(number)

        # reverse string --> LLM used ot understand notation of string slicing
        number = number[::-1]

        # turn back into integer
        return int(number)

    # create formatter function --> will take number and return its binary and octal representations
    # example: 10 -> ("0b1010", "0o12")
    def formatter(self, number):
        # check if input is int
        if type(number) != int:
            raise TypeError("Input must be an integer")

        # convert to binary/octal using python built-in function
        binary = bin(number)
        octal = oct(number)

        # return both answers
        return binary, octal