# Definição da classe Fila
class Fila:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os itens da fila
        self.itens = []

    def enfileirar(self, item):
        # Adiciona um item ao final da fila
        # Exemplo: fila.enfileirar(1) -> Fila: [1]
        self.itens.append(item)

    def desenfileirar(self):
        # Remove e retorna o item do início da fila
        # Exemplo: fila.desenfileirar() -> Remove e retorna o primeiro item
        if not self.vazia():
            return self.itens.pop(0)
        else:
            # Se a fila estiver vazia, levanta uma exceção
            raise Exception("Fila vazia")

    def vazia(self):
        # Verifica se a fila está vazia
        # Retorna True se estiver vazia, False caso contrário
        return len(self.itens) == 0


# Exemplo de uso da classe Fila
if __name__ == "__main__":
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
