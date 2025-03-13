# Estrutura de Dados: Fila (Queue)

Este repositório contém uma implementação simples de uma **Fila** (Queue) em Python. A fila é uma estrutura de dados fundamental que segue o princípio **FIFO** (First In, First Out), onde o primeiro elemento inserido é o primeiro a ser removido.

## O que é uma Fila?

Uma fila é uma estrutura de dados baseada no princípio **FIFO** (First In, First Out), onde o primeiro elemento inserido é o primeiro a ser removido. As operações principais em uma fila são:

- **Enfileirar (Enqueue)**: Adiciona um elemento no final da fila.
- **Desenfileirar (Dequeue)**: Remove e retorna o elemento no início da fila.

### Analogia com Fila de Pessoas
Imagine uma fila de pessoas esperando para comprar ingressos para um show. A primeira pessoa que chega à fila é a primeira pessoa a ser atendida e a sair da fila (**dequeue**), e qualquer nova pessoa que chegue vai para o final da fila (**enqueue**). Isso é conhecido como comportamento **FIFO** (First In, First Out) — a primeira pessoa que entra na fila é a primeira a sair.

---

## Implementação da Fila em Python

A implementação da fila neste repositório utiliza uma lista Python para armazenar os elementos. A classe `Fila` contém os seguintes métodos:

1. **`__init__()`**:
   - Inicializa uma fila vazia.

2. **`enfileirar(item)`**:
   - Adiciona um elemento ao final da fila.

3. **`desenfileirar()`**:
   - Remove e retorna o elemento no início da fila.
   - Se a fila estiver vazia, levanta uma exceção com a mensagem "Fila vazia".

4. **`vazia()`**:
   - Retorna `True` se a fila estiver vazia, e `False` caso contrário.

---

## Exemplo de Uso

Para ver um exemplo prático de como usar a classe `Fila`, consulte o arquivo **[`example.py`](example.py)**. Esse arquivo demonstra como enfileirar e desenfileirar elementos, além de mostrar a saída esperada.

---

## Aplicações Comuns de Filas

As filas são amplamente utilizadas em diversas áreas da computação, como:

1. **Sistemas de Atendimento**:
   - Filas são usadas em sistemas de atendimento ao cliente, onde o primeiro a chegar é o primeiro a ser atendido.

2. **Gerenciamento de Processos em Sistemas Operacionais**:
   - Sistemas operacionais usam filas para gerenciar processos, garantindo que o primeiro processo a entrar seja o primeiro a ser executado.

3. **Buffers de Dados**:
   - Filas são usadas em buffers de dados, como em streaming de vídeo ou áudio, onde os dados são processados na ordem em que chegam.

4. **Fila de Impressão**:
   - Impressoras usam filas para gerenciar documentos enviados para impressão, processando-os na ordem de chegada.

5. **Algoritmos de Busca em Grafos (BFS)**:
   - A busca em largura (BFS) utiliza filas para explorar nós de um grafo nível por nível.

---

## Referências Bibliográficas

1. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
   - Livro clássico sobre algoritmos e estruturas de dados, com explicações detalhadas sobre filas.

2. **Sedgewick, R., & Wayne, K.** (2011). *Algorithms* (4th ed.). Addison-Wesley.
   - Outro livro essencial que aborda filas e suas aplicações.

3. **Documentação Oficial do Python**:
   - Disponível em: [https://docs.python.org/3/](https://docs.python.org/3/)
   - Contém informações sobre listas e métodos como `append` e `pop`, usados na implementação da fila.
