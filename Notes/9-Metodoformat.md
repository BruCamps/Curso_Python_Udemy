# Método format()
Esta é outra maneira de formatarmos objetos dentro do Python.

<br>

> [!NOTE]
> Tudo em Python é objeto, porque eles geralmente tem métodos dentro dele, o que o permite realizar ações.

<br>

**Métodos** são funções que realizam ações sobre os dados do objeto. Como por exemplo o próprio format().

Dentro dos métodos é possível passar argumentos — tudo o que colocamos dentro dos parênteses —, veja a seguir:

```python
a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f}'.format(a, b, c)

print(formato)

# Saída: a=A b=B c=1.10
```

A partir do exemplo é possível notar que as chaves recebem os valores seguindo a ordem das variáveis que estão entre parênteses.

<br>

Também é possível mudar a ordem utilizando os índices, que são basicamente as posições de elementos. E os índices também nos permite repetir o mesmo elemento.

```python
a = 'A'
b = 'B'
c = 1.1

formato = 'b={1} a={0} a={0} a={0} c={2:.2f}'.format(a, b, c)

print(formato)

# Saída: b=B a=A a=A a=A c=1.10
```

### Tá, mas... porque 0, 1 e 2? Não são 3 elementos?

![image](https://github.com/user-attachments/assets/ff271187-699b-41fb-9c30-354e8f21d1c3)

Em lógica de programação quando nos referimos aos índices (posições), começamos a contar a partir do número 0, o que significa que o primeiro elemento sempre será 0, o segundo 1, o terceiro 2, e assim por diante.

-----

### Parâmetros nomeados
É o nome dado a um argumento. E a partir do momento em que um argumento é nomeado, os outros que vierem DEPOIS dele também devem ser nomeados.

Abaixo você verá que ao criar um parâmetro, dentro das chaves colocamos o nome do parâmetro. Ele funcionará da mesma forma que os índices.

```python
a = 'A'
b = 'B'
c = 1.1

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' # Colocado em uma variável separada para melhor visualização
formato = string.format(
      nome1=a,       # Parâmetro -> nome1 |  Argumento -> a
      nome2=b,       # Parâmetro -> nome2 |  Argumento -> b
      nome3=c        # Parâmetro -> nome3 |  Argumento -> c
)

print(formato)

# Saída: b=B a=A a=A a=A c=1.10
```









