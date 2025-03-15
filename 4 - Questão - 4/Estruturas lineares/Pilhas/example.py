# Definição da classe Pilha
class Pilha:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os itens da pilha
        self.itens = []

    def empilhar(self, item):
        # Adiciona um item ao topo da pilha
        # Exemplo: pilha.empilhar(1) -> Pilha: [1]
        self.itens.append(item)

    def desempilhar(self):
        # Remove e retorna o item do topo da pilha
        # Exemplo: pilha.desempilhar() -> Remove e retorna o último item
        if not self.vazia():
            return self.itens.pop()
        else:
            # Se a pilha estiver vazia, levanta uma exceção
            raise Exception("Pilha vazia")

    def vazia(self):
        # Verifica se a pilha está vazia
        # Retorna True se estiver vazia, False caso contrário
        return len(self.itens) == 0


# Exemplo de uso da classe Pilha
if __name__ == "__main__":
    # Cria uma instância da classe Pilha
    pilha = Pilha()

    # Empilha três elementos na pilha
    pilha.empilhar(1)  # Pilha: [1]
    pilha.empilhar(2)  # Pilha: [1, 2]
    pilha.empilhar(3)  # Pilha: [1, 2, 3]

    # Desempilha e imprime o elemento do topo da pilha
    print(pilha.desempilhar())  # Saída: 3 (Pilha após desempilhar: [1, 2])

    # Desempilha e imprime o próximo elemento do topo da pilha
    print(pilha.desempilhar())  # Saída: 2 (Pilha após desempilhar: [1])
