from url_extractor import URLExtractor
import re


def __main__():
    url = "https://bytebank.com/cambio?currencyOrigin=real&currencyDestination=dolar&quantity=100"
    url1 = URLExtractor(url)
    url2 = URLExtractor(url)

    value = url1.get_parameter_value("currencyOrigin")
    print(value)

    print("The URL length is", len(url1))
    print(url1)

    # To compare two objects, the Python calls the "__eq__()" method, and compares the address of the objects
    print(url1 == url2)

    # To view an address of an object, just use the "id()" method
    print(id(url1))
    print(id(url2))

    print(url1.convert())


if __name__ == "__main__":
    __main__()
