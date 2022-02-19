def __main__():
    url = "https://bytebank.com/cambio?currencyOrigin=real&currencyDestination=dolar&quantity=100"
    print(url)

    # Separates the domain from parameters
    question_mark_index = url.find("?")

    domain = url[:question_mark_index]
    print(domain)

    parameters = url[question_mark_index + 1:]
    print(parameters)

    # Get the parameter value
    search_parameter = "currencyDestination"
    index_parameter = parameters.find(search_parameter)
    index_value = index_parameter + len(search_parameter) + 1
    # The second parameter indicate the start of slice
    commercial_e = parameters.find("&", index_value)

    if commercial_e == -1:
        value = parameters[index_value:]
    else:
        # Slicing returns an empty string if the value of the first argument is greater than the second
        value = parameters[index_value:commercial_e]

    print(value)


if __name__ == "__main__":
    __main__()
