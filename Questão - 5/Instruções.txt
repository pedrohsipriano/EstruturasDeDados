5. Aplicação Prática:

Escolha um problema prático que possa ser resolvido com o uso de uma das estruturas de dados lineares (listas, filas ou pilhas).
Descreva o problema e explique como a estrutura de dados escolhida pode ser usada para resolvê-lo.
No Repositório do GitHub, na pasta raiz, crie um arquivo readme.md explicando o problema prático escolhido e um arquivo .py ou .js com a resolução do problema prático utilizando a estrutura de dados escolhida.


# Gerenciamento de Histórico de Navegação com Pilha  

Este repositório apresenta um estudo sobre como **pilhas (stacks)** podem ser utilizadas para gerenciar o histórico de navegação em navegadores web. A estrutura de **pilha** é amplamente usada para implementar a funcionalidade de "voltar" e "avançar" entre páginas visitadas.  

## O que é uma Pilha?  

Uma **pilha** é uma estrutura de dados baseada no princípio **LIFO** (*Last In, First Out*), onde o último elemento inserido é o primeiro a ser removido. As operações principais em uma pilha são:  

- **Empilhar (Push)**: Adiciona um elemento no topo da pilha.  
- **Desempilhar (Pop)**: Remove e retorna o elemento no topo da pilha.  

### Analogia com o Histórico de Navegação  

Os navegadores web utilizam pilhas para armazenar páginas visitadas. Quando o usuário navega para uma nova página, ela é empilhada no histórico. Se o usuário clicar no botão "Voltar", a página atual é removida da pilha de histórico e movida para uma **pilha auxiliar**, permitindo avançar novamente caso desejado.  

---

## Como a Pilha é Usada no Histórico de Navegação?  

O gerenciamento do histórico de navegação pode ser feito utilizando **duas pilhas**:  

1. **Pilha de histórico:** Armazena as páginas visitadas na ordem de acesso.  
2. **Pilha de avançar:** Guarda as páginas quando o usuário pressiona "Voltar", permitindo que ele possa retorná-las caso deseje.  

### Funcionamento  

- Quando o usuário **acessa uma nova página**, ela é adicionada ao topo da **pilha de histórico**.  
- Ao pressionar **"Voltar"**, a página atual é removida da **pilha de histórico** e inserida na **pilha de avançar**.  
- Se o usuário pressionar **"Avançar"**, a página é removida da **pilha de avançar** e recolocada no topo da **pilha de histórico**.  
- Caso uma nova página seja acessada após pressionar "Voltar", a **pilha de avançar é esvaziada**, pois não há mais um caminho possível para avançar.  

---

## Aplicações Comuns de Pilhas em Navegadores  

Além do histórico de navegação, pilhas são utilizadas em outras funcionalidades dos navegadores:  

1. **Navegação por guias (tabs)**  
   - Algumas implementações permitem alternar entre guias abertas usando pilhas.  

2. **Undo/Redo em formulários e editores de texto**  
   - O navegador pode armazenar alterações feitas pelo usuário, permitindo desfazer e refazer ações.  

3. **Backtracking em formulários**  
   - Alguns sites utilizam pilhas para armazenar estados de formulários preenchidos.  

4. **Verificação de sintaxe em JavaScript e HTML**  
   - Navegadores utilizam pilhas para validar marcações e parênteses balanceados no código das páginas web.  

---

## Referências Bibliográficas  

1. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.  
   - Livro clássico sobre algoritmos e estruturas de dados, com explicações detalhadas sobre pilhas.  

2. **Sedgewick, R., & Wayne, K.** (2011). *Algorithms* (4th ed.). Addison-Wesley.  
   - Livro essencial que aborda pilhas e suas aplicações em navegação e outras áreas da computação.  

3. **Documentação Oficial do Mozilla Developer Network (MDN)**.  
   - Disponível em: [https://developer.mozilla.org/](https://developer.mozilla.org/)  
   - Explica como os navegadores gerenciam histórico de navegação.  
