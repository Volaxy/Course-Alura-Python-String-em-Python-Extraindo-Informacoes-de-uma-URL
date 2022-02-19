def __main__():
    url = "https://bytebank.com/cambio?currencyOrigin=real&currencyDestination=dolar&quantity=100"
    print(url)

    # Sanitization is the process of deleting unnecessary characters from the string.
    # Sanitize the string
    url.replace(" ", "")
    # The "strip()" clear the blank spaces in the string
    # url.strip()
    # The "lstrip()" clear the blank spaces on the left side of the string
    # url.lstrip()
    # The "rstrip()" clear the blank spaces on the right side of the string
    # url.rstrip()

    if url == "":
        # The "ValueError" is a class which indicate that a value error has occurred
        raise ValueError("The URL is empty")

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
    commercial_e = parameters.find("&", index_value)

    if commercial_e == -1:
        value = parameters[index_value:]
    else:
        value = parameters[index_value:commercial_e]

    print(value)


if __name__ == "__main__":
    __main__()
