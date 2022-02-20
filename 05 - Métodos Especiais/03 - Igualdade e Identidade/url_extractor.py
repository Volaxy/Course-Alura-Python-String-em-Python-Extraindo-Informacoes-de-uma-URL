import re


class URLExtractor:
    def __init__(self, url):
        self.url = self.sanitize(url)
        self.validate_url()

    @staticmethod
    def sanitize(url: str) -> str:
        if type(url) == str:
            return url.strip()
        else:
            return

    def validate_url(self) -> None:
        if not self.url:
            raise ValueError("The URL is empty")

        url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")

        match = url_pattern.match(self.get_base_url())

        if not match:
            raise ValueError("The URL is not valid")

    def get_base_url(self) -> str:
        question_mark_index = self.url.find("?")

        domain = self.url[:question_mark_index]
        return domain

    def get_url_parameters(self) -> str:
        question_mark_index = self.url.find("?")

        parameters = self.url[question_mark_index + 1:]
        return parameters

    def get_parameter_value(self, parameter: str) -> str:
        parameters = self.get_url_parameters()

        index_parameter = parameters.find(parameter)
        index_value = index_parameter + len(parameter) + 1
        commercial_e = parameters.find("&", index_value)

        if commercial_e == -1:
            value = parameters[index_value:]
        else:
            value = parameters[index_value:commercial_e]

        return value

    def __len__(self) -> int:
        return len(self.url)

    def __str__(self) -> str:
        return self.url

    def __eq__(self, other):
        return self.url == other.url

    def convert(self) -> float:
        currency_origin = self.get_parameter_value("currencyOrigin")
        quantity = self.get_parameter_value("quantity")

        if currency_origin == "real":
            return float(quantity) / 5.5
        else:
            return float(quantity) * 5.5
