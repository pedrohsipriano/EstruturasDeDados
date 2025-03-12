# Definição da classe Fila
class Fila:
    # Método construtor da classe
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os itens da fila
        self.itens = []

    # Método para adicionar um item ao final da fila
    def enfileirar(self, item):
        # Usa o método append da lista para adicionar o item ao final da fila
        self.itens.append(item)

    # Método para remover e retornar o item do início da fila
    def desenfileirar(self):
        # Verifica se a fila está vazia usando o método vazia
        if not self.vazia():
            # Remove e retorna o primeiro item da lista (início da fila)
            return self.itens.pop(0)
        else:
            # Se a fila estiver vazia, levanta uma exceção
            raise Exception("Fila vazia")

    # Método para verificar se a fila está vazia
    def vazia(self):
        # Retorna True se a lista estiver vazia (len == 0), caso contrário, False
        return len(self.itens) == 0


# Exemplo de uso da classe Fila
# Cria uma instância da classe Fila
fila = Fila()

# Enfileira três elementos na fila
fila.enfileirar(1)  # Fila: [1]
fila.enfileirar(2)  # Fila: [1, 2]
fila.enfileirar(3)  # Fila: [1, 2, 3]

# Desenfileira e imprime o elemento do início da fila
print(fila.desenfileirar())  # Saída: 1 (Fila após desenfileirar: [2, 3])

# Desenfileira e imprime o próximo elemento do início da fila
print(fila.desenfileirar())  # Saída: 2 (Fila após desenfileirar: [3])
