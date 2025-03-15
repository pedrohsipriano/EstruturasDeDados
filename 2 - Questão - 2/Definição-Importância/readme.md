# Importância das Estruturas de Dados

As estruturas de dados desempenham um papel essencial no desempenho de um programa. Uma escolha inadequada pode resultar em maior uso de memória, tempo de processamento mais lento e dificuldades na manutenção do código.

## Exemplo de Impacto na Performance

Suponha que precisamos buscar um elemento em uma lista. Se usarmos uma lista desordenada, a busca será O(n) no pior caso. Já com uma estrutura adequada, como um **dicionário (hash map)** ou uma **árvore balanceada**, podemos reduzir a complexidade para O(1) ou O(log n), melhorando significativamente a eficiência.

No código a seguir, demonstramos a diferença entre um código sem tratamento adequado e um código otimizado.
 
# 🔴 Código ineficiente (sem estrutura adequada)

 ```python
 # Busca ineficiente em uma lista não ordenada (O(n))
lista = [10, 23, 45, 70, 11, 15, 9]

def busca_ineficiente(valor):
    for item in lista:
        if item == valor:
            return True
    return False

print(busca_ineficiente(70))  # Demora mais à medida que a lista cresce

```

# ✅ Código otimizado usando dicionário (estrutura adequada)

```python 
# Busca eficiente usando um dicionário (O(1))
dados = {10: True, 23: True, 45: True, 70: True, 11: True, 15: True, 9: True}

def busca_eficiente(valor):
    return valor in dados

print(busca_eficiente(70))  # Muito mais rápido
```