def __main__():
    url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    print(url)

    text = "text"
    print(text)

    # To select a character in the string, just put the index between the "[]"
    print(text[0])

    # To select a range of a string, just put the value of init in the "[x:]" (<-), and the end "[x:y]" (->)
    # In slicing, the first argument is inclusive, but the second argument, the final argument, is exclusive, that is,
    # it will not include the character at that position.
    print(text[0:2])

    # Getting the domain and the URL parameters
    domain = url[0:27]
    print(domain)

    parameters = url[28:]
    print(parameters)

    """
    Slicing is one of the characteristics of strings in Python, because strings are immutable, once they are created
    they cannot be changed, you can usually just extract pieces of it, which will actually be new copies of it.
    """
    print(url)


if __name__ == "__main__":
    __main__()
