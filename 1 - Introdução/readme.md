## Introdução às Estruturas de Dados.

## O que são estruturas de dados?

Estruturas de dados são formas de organizar e armazenar dados em um computador, de modo que possam ser acessados e modificados de forma eficiente. Elas definem a relação entre os dados e as operações que podem ser realizadas sobre eles.

## Qual a importância das estruturas de dados na ciência da computação?

A importância das estruturas de dados na ciência da computação é fundamental, pois elas permitem:

* **Organização eficiente dos dados:** Permitem que os dados sejam armazenados de forma organizada, facilitando o acesso e a manipulação.
* **Otimização de algoritmos:** A escolha da estrutura de dados correta pode melhorar significativamente o desempenho de um algoritmo, reduzindo o tempo de execução e o consumo de memória.
* **Modelagem de problemas reais:** Permitem representar e resolver problemas complexos do mundo real, como gerenciamento de informações, simulações e sistemas de busca.
* **Reutilização de código:** Estruturas de dados bem definidas podem ser reutilizadas em diferentes programas, economizando tempo e esforço no desenvolvimento de software.

## Exemplos de problemas do mundo real resolvidos com estruturas de dados:

### Gerenciamento de contatos em um celular (Lista Encadeada)
```python
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.proximo = None

class ListaContatos:
    def __init__(self):
        self.cabeca = None

    def adicionar_contato(self, nome, telefone):
        novo_contato = Contato(nome, telefone)
        if not self.cabeca:
            self.cabeca = novo_contato
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_contato

    def buscar_contato(self, nome):
        atual = self.cabeca
        while atual:
            if atual.nome == nome:
                return f"Nome: {atual.nome}, Telefone: {atual.telefone}"
            atual = atual.proximo
        return "Contato não encontrado"
```

### Roteamento de pacotes na internet (Grafo)
```python
class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_rota(self, origem, destino, custo):
        if origem not in self.vertices:
            self.vertices[origem] = []
        if destino not in self.vertices:
            self.vertices[destino] = []
        self.vertices[origem].append((destino, custo))
        self.vertices[destino].append((origem, custo))
```

### Simulação de tráfego urbano (Fila)
```python
from collections import deque

class SimulacaoTransito:
    def __init__(self):
        self.fila_veiculos = deque()

    def entrar_no_cruzamento(self, veiculo):
        self.fila_veiculos.append(veiculo)
        print(f"Veículo {veiculo} entrou na fila.")

    def liberar_veiculo(self):
        if self.fila_veiculos:
            print(f"Veículo {self.fila_veiculos.popleft()} passou pelo cruzamento.")
        else:
            print("Nenhum veículo na fila.")
```

### Sistemas de busca na web (Arvore de Busca)
```python
class NoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir_rec(self.raiz, chave)

    def _inserir_rec(self, no, chave):
        if no is None:
            return NoArvore(chave)
        if chave < no.chave:
            no.esquerda = self._inserir_rec(no.esquerda, chave)
        else:
            no.direita = self._inserir_rec(no.direita, chave)
        return no

    def buscar(self, chave):
        return self._buscar_rec(self.raiz, chave)

    def _buscar_rec(self, no, chave):
        if no is None or no.chave == chave:
            return no is not None
        if chave < no.chave:
            return self._buscar_rec(no.esquerda, chave)
        return self._buscar_rec(no.direita, chave)
```

### Repositórios de dados (Tabela Hash)
```python
class BancoDeDados:
    def __init__(self):
        self.tabela = {}

    def inserir_dado(self, chave, valor):
        self.tabela[chave] = valor

    def buscar_dado(self, chave):
        return self.tabela.get(chave, "Dado não encontrado")
```

## Referências:

CORMEN, Thomas H. et al. Algoritmos: Teoria e Prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

ALURA. Estruturas de dados: uma introdução. [S. l.], [s. d.]. Disponível em: [Alura](https://www.alura.com.br/artigos/estruturas-de-dados-introducao).
