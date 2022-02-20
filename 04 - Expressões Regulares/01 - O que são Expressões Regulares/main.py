# The "re" is a library of RegEx
import re


def __main__():
    address = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

    # The "compile()" method compiles the pattern specified as a parameter
    # The "[]" indicates which characters are valid
    # The "?" indicates that the value may or may not be within the standard
    pattern = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789]-?"
                         "[0123456789][0123456789][0123456789]")

    # The ".search()" search if the pattern is inside the string
    result = pattern.search(address)

    if result:
        # The ".group()" return the match string which was found with the specified pattern
        cep = result.group()
        print(cep)


if __name__ == "__main__":
    __main__()
