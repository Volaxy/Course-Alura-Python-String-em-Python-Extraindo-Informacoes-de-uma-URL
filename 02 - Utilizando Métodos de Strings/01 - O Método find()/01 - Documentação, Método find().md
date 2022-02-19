A gente aprendeu que podemos utilizar o método `find` para *encontrar* o **índice** de um caractere dentro de uma *string*, como em `url.find("?")`. O método `find` é um método bem flexível e pode ser usado de diversas outras maneiras como mostra a [documentação oficial do Python](https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=find#str.find).

De acordo com essa documentação, o método find tem a seguinte estrutura: `str.find(sub[, start[, end]])`

* *sub* é um parâmetro obrigatório, abreviação de *substring*. Significa que podemos passar uma *string* (e não necessariamente somente um caractere) para encontrar seu índice na *string original*.
* *start* é um parâmetro opcional, caso fornecido, a busca por *sub* vai ocorrer somente **a partir** do índice *start*.
* *end* também é opcional, caso fornecido, a busca vai **até** o índice de *end*.
* `str.find(sub)` retorna **-1** caso `sub` não seja encontrado em `str`.

Sempre que quisermos entender mais sobre algum método ou ver quais outros métodos existem, podemos recorrer à documentação oficial da linguagem. Recomendo muito que você experimente diferentes modos de usar o método find de acordo com as opções descritas acima!

Por exemplo, será que conseguimos verificar se nossa variável `url` contém o caractere "?" ou não, antes de fazermos o fatiamento? (Dica: observe o que o método `find` retorna caso não encontre a *substring* buscada).