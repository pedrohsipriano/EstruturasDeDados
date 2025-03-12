# Definição da classe Pilha
class Pilha:
    # Método construtor da classe
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os itens da pilha
        self.itens = []

    # Método para adicionar um item ao topo da pilha
    def empilhar(self, item):
        # Usa o método append da lista para adicionar o item ao final (topo da pilha)
        self.itens.append(item)

    # Método para remover e retornar o item do topo da pilha
    def desempilhar(self):
        # Verifica se a pilha está vazia usando o método vazia
        if not self.vazia():
            # Remove e retorna o último item da lista (topo da pilha)
            return self.itens.pop()
        else:
            # Se a pilha estiver vazia, levanta uma exceção
            raise Exception("Pilha vazia")

    # Método para verificar se a pilha está vazia
    def vazia(self):
        # Retorna True se a lista estiver vazia (len == 0), caso contrário, False
        return len(self.itens) == 0


# Exemplo de uso da classe Pilha
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
