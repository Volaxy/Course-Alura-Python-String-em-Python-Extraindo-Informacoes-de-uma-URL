def __main__():
    url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    print(url)

    # The "find()" method return the index of the string parameter inside the string in which the function is called
    question_mark_index = url.find("?")

    # The empty parameter before the ":" indicates that the string will be sliced ​​from the beginning to the
    # specified position
    domain = url[:question_mark_index]
    print(domain)

    # The empty parameter after the ":" indicates that the string will be sliced ​​from position "x" to the end
    # of the string
    parameters = url[question_mark_index + 1:]
    print(parameters)


if __name__ == "__main__":
    __main__()
