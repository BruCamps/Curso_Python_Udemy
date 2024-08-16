# Comentários de Código

<h3>Uso da Cerquilha / Hastag "#"</h3>
<p>Quando utilizamos a hastag no código, o interpretador ignora tudo o que está depois desse símbolo, ou seja, nada após a hastag será exibido ou executado. O que nos permite escrever um comentário.</p>
<br>

```python
# O interpretador ignora esta linha e lê a próxima

print(1) # Nesta linha apenas o print(1) é executado
```
<br>

>[!IMPORTANT]
> O comentário de cerquilha funciona apenas em uma linha, ou seja, para cada linha que você precisa comentar, deve colocar uma cequilha. Em casos de textos maiores, evite a cerquilha. 

<br>

<h3>DocString """ """</h3>
<p>Este recurso não é um comentário, mas podemos utilizar para fazer anotações como a hastag. Pois, apesar do interpretador ler essas linhas, em alguns casos os desenvolvedores costumam usar o DocString como comentários para múltiplas linhas.
</p>

<br>

```python
""" 
Podemos escrever diversas linhas através do DocString, como nesse exemplo
"""

'''
O DocString pode ter tanto aspas simples '' quanto aspas duplas "", mas não mesclando os 2
'''
```

<br>
<h3>Para que servem os comentários?</h3>
<p>Você pode utilizá-los caso precise fazer notas sobre o que está aprendendo ou para explicar o seu código. 

Os comentários nos auxiliam também a entender o que está sendo feito em algoritmos e projetos mais complexos a partir das descrições do papel de cada função naquele sistema.</p>
