# String em Python Extraindo Informações de uma URL

Curso da Alura sobre extração de dados de uma string e formas de manipula-las.

## Objetivo Final &#x1F3AF;

Criar uma classe genérica para manipulação de *strings* e métodos responsáveis por manipula-las.

URL do curso -> [String em Python Extraindo Informações de uma URL](https://cursos.alura.com.br/course/string-python-extraindo-informacoes-url)

![String em Python Extraindo Informações de uma URL](https://www.alura.com.br/assets/api/share/curso-string-python-extraindo-informacoes-url.png)

## Siglas &#x1F5FA;
* RE - **R**egular **E**xpression - Expressão Regular.

## 01 - Introdução e Fatiamento de Strings &#x1F516;
* URLs e seus formatos: como as URLs funcionam e o que cada parte de uma URL significa - base e parâmetros.
* O operador de fatiamento `[a:b]`, utilizado para obter uma substring desde o índice `a` até o índice `b - 1` da string original. Lembrando que `b - 1` pois o segundo argumento do fatiamento é exclusivo.
* A string original não é alterada ao ser fatiada devido à sua *imutabilidade*.

### 01 - Parâmetros em Páginas da Internet
* Criar uma *URL* fictícia para manipular *strings*.

### 02 - Fatiamento de Strings
* Selecionar um *caractere* de uma *string* em uma determinada posição com `string[INDEX]`.
* Fatiar uma *string* com `string[x:y]`.

## 02 - Utilizando Métodos de Strings &#x1F516;
* Uma *string* é uma cadeia de caracteres onde cada caractere tem sua própria posição ou **índice**.
Podemos omitir o primeiro ou o segundo argumento do operador de fatiamento para fatiar uma string do início até um certo índice, ou a partir de um índice até o final. Exemplo: `str[a:]` ou `str[:b]`.
* Podemos utilizar o método `str.find(palavra, inicio)` para buscar o índice de `palavra` a partir de `inicio`.
    * Caso `palavra` não seja encontrada, o método `find` retorna **-1**.
* O método `len(string)` retorna o **tamanho** (ou seja, a quantidade de caracteres) da nossa *string*.
    * Dica: o caractere que representa espaço em branco (“ “) também conta! Por exemplo: `len(" ")` retorna `1`.

### 01 - O Método find()
* Utilizar o método `find(STRING)` para achar uma *string* específica em outra *string*.

### 02 - O Método len()
* Fazer buscas de *strings* específicas com `find(STRING)`.
* Usar a função `len(OJECT)` para obter o tamanho de uma *string*.

### 03 - URL com Múltiplos Parâmetros
* Usar o método `find(STRING, BEGIN)` indicando a partir de qual posição se quer começar.

## 03 - Aplicando Orientação a Objetos no Projeto &#x1F516;
* Podemos utilizar a palavra-chave `raise` para lançar uma exceção no nosso programa, informando ao usuário qual erro ocorreu.
* Mais métodos de strings: `str.replace` e `str.strip`.
* Como transformar um código em uma classe com atributos e métodos.
* A diferença entre `None`, `””`, `0`, e como o `if` do Python funciona.
* O operador `not`.

### 01 - Validando a URL
* Lançar uma exceção com a palavra chave `raise`.
* Usar o método `replace(SEARCH, STRING)`.
* O método `strip()` limpa os espaços em branco de uma *string*.

### 02 - Criando nossa Classe
* Criar uma classe `URLExtractor`.

### 03 - None vs Empty, e o If do Python
* Fazer validação da `url`.

## 04 - Expressões Regulares &#x1F516;
* Como construir e utilizar expressões regulares, ou RegEx utilizando o módulo `re` do Python.
* Qual a diferença entre `search` e `match`.
* O que são quantificadores e intervalos em RegEx.
* A diferença entre parênteses `(..)` colchetes `[...]` na construção de padrões.
* Como utilizar expressões regulares para fazer validações complexas.

### 01 - O que são Expressões Regulares
* Utilizar a biblioteca `re` para expressões regulares.
* `re.compile(PATTERN)` recebe uma *string* com a expressão regular desejada.
* `compile(STRING)` para ver se dentro da *string* há o padrão especificado.
* Usar o `?` na *string* do padrão.

### 02 - Quantificadores e Intervalos
* Usar **quantificadores** com `{x}`.
* Usar **intervalos** com `x-y`.

### 03 - Validando nossa URL com RegEx
* Diferenças entre usar `()` e `[]`.
* Usar `match()` para verificar se uma *string* corresponde exatamente com o padrão.

## 05 - Métodos Especiais &#x1F516;
* Métodos especiais são chamados pelo próprio interpretador Python de acordo com alguma instrução.
* Como implementar métodos especiais em nossas classes para criar comportamentos customizados.
* A diferença entre igualdade (`==`) e identidade (`is`).

### 01 - O Método `__len__()`
* Implementar o método `__len__()` dentro da classe.

### 02 - O Método `__Str__()`
* Utilizar o método `__Str__()` para imprimir um objeto.

### 03 - Igualdade e Identidade
* Comparar de 2 objetos são iguais ou não.