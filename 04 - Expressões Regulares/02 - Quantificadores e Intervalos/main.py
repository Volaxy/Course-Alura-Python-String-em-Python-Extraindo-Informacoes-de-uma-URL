import re


def __main__():
    address = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

    # The "{x}" indicates which times the expression will be repeated
    # If "{x,y}" is used, the repetition will be made from "x" to "y" times
    pattern = re.compile("[0-9]{5}-{0,1}[0-9]{3}")

    result = pattern.search(address)

    if result:
        cep = result.group()
        print(cep)


if __name__ == "__main__":
    __main__()
