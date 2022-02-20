from url_extractor import URLExtractor
import re


def __main__():
    url = URLExtractor("https://bytebank.com/cambio?currencyOrigin=real&currencyDestination=dolar&quantity=100")

    value = url.get_parameter_value("currencyOrigin")
    print(value)

    print("The URL length is", len(url))
    # The "__str__()" is called by the object
    print(url)


if __name__ == "__main__":
    __main__()
