A classe `str` do Python possui diversos outros métodos e funcionalidades para facilitar nosso dia a dia, além dos que já vimos aqui no curso. Esses métodos ficam especificados na [documentação oficial do Python sobre a classe str](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods).

Será que podemos adicionar ainda mais validações à nossa URL? Por exemplo, verificar se ela começa com “https”, ou se a **base** dela termina com a string “/cambio”, indicando que estamos na página de câmbio do Bytebank.

Acesse a documentação e procure pelos métodos `str.startswith` e `str.endswith` e tente utilizá-los para validar a nossa `url_base`.

Dica: “starts with” em inglês significa “começa com” e “ends with” significa “termina com”.