# Definição de operações básicas com listas em Python
    # Criação de uma lista
    minha_lista = [1, 2, 3]  # Lista inicial: [1, 2, 3]
    print("Lista inicial:", minha_lista)

    # Adicionando elementos à lista
    minha_lista.append(4)  # Adiciona o número 4 ao final da lista
    print("Após append(4):", minha_lista)  # Saída: [1, 2, 3, 4]

    minha_lista.insert(1, "Python")  # Insere "Python" na posição 1
    print('Após insert(1, "Python"):', minha_lista)  # Saída: [1, "Python", 2, 3, 4]

    # Acessando elementos da lista
    print("Elemento na posição 2:", minha_lista[2])  # Saída: 2

    # Removendo elementos da lista
    minha_lista.remove("Python")  # Remove a primeira ocorrência de "Python"
    print('Após remove("Python"):', minha_lista)  # Saída: [1, 2, 3, 4]

    elemento_removido = minha_lista.pop(1)  # Remove e retorna o elemento na posição 1 (valor 2)
    print("Elemento removido com pop(1):", elemento_removido)  # Saída: 2
    print("Lista após pop(1):", minha_lista)  # Saída: [1, 3, 4]

    # Verificando o tamanho da lista
    print("Tamanho da lista:", len(minha_lista))  # Saída: 3

    # Verificando se a lista está vazia
    if not minha_lista:
        print("A lista está vazia!")
    else:
        print("A lista não está vazia.")  # Saída: A lista não está vazia.
