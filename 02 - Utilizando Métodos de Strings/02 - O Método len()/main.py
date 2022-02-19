def __main__():
    url = "https://bytebank.com/cambio?currencyOrigin=real&currencyDestination=dolar&quantity=100"
    print(url)

    question_mark_index = url.find("?")

    domain = url[:question_mark_index]
    print(domain)

    parameters = url[question_mark_index + 1:]
    print(parameters)

    search_parameter = "currencyOrigin"
    index_parameter = parameters.find(search_parameter)
    # The "len()" method return the length of string
    value = parameters[index_parameter + len(search_parameter) + 1:]
    print(value)


if __name__ == "__main__":
    __main__()
