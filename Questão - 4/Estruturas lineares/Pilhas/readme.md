Estrutura de Dados: Pilha (Stack)
Este repositório contém uma implementação simples de uma Pilha (Stack) em Python. A pilha é uma estrutura de dados fundamental que segue o princípio LIFO (Last In, First Out), onde o último elemento inserido é o primeiro a ser removido.

O que é uma Pilha?
Uma pilha é uma estrutura de dados baseada no princípio LIFO (Last In, First Out), onde o último elemento inserido é o primeiro a ser removido. As operações principais em uma pilha são:

Empilhar (Push): Adiciona um elemento no topo da pilha.

Desempilhar (Pop): Remove e retorna o elemento no topo da pilha.

Analogia com Pilha de Livros
Pense em uma pilha de livros. Você só pode adicionar um novo livro no topo da pilha (push) e só pode remover o livro que está no topo da pilha (pop). Isso é conhecido como comportamento LIFO (Last In, First Out) — o último livro que você colocou na pilha será o primeiro que você vai tirar.

Implementação da Pilha em Python
A implementação da pilha neste repositório utiliza uma lista Python para armazenar os elementos. A classe Pilha contém os seguintes métodos:

__init__():

Inicializa uma pilha vazia.

empilhar(item):

Adiciona um elemento ao topo da pilha.

desempilhar():

Remove e retorna o elemento no topo da pilha.

Se a pilha estiver vazia, levanta uma exceção com a mensagem "Pilha vazia".

vazia():

Retorna True se a pilha estiver vazia, e False caso contrário.

Exemplo de Uso
Para ver um exemplo prático de como usar a classe Pilha, consulte o arquivo example.py. Esse arquivo demonstra como empilhar e desempilhar elementos, além de mostrar a saída esperada.

Para executar o exemplo, basta rodar o arquivo example.py:

bash
Copy
python example.py
Aplicações Comuns de Pilhas
As pilhas são amplamente utilizadas em diversas áreas da computação, como:

Gerenciamento de Chamadas de Funções:

Pilhas são usadas para gerenciar a execução de funções em linguagens de programação.

Undo/Redo em Editores de Texto:

Operações como "desfazer" (undo) e "refazer" (redo) são implementadas usando pilhas.

Avaliação de Expressões:

Pilhas são usadas para avaliar expressões matemáticas, como notação polonesa reversa.

Navegação em Navegadores:

O histórico de páginas visitadas em um navegador pode ser implementado com uma pilha.

Referências Bibliográficas
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.

Livro clássico sobre algoritmos e estruturas de dados, com explicações detalhadas sobre pilhas.

Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley.

Outro livro essencial que aborda pilhas e suas aplicações.

Documentação Oficial do Python:

Disponível em: https://docs.python.org/3/

Contém informações sobre listas e métodos como append e pop, usados na implementação da pilha.

Como Contribuir
