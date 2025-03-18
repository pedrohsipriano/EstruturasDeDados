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

---

## Referências Bibliográficas  

1. **CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C.** _Introduction to Algorithms_. 3. ed. Cambridge: MIT Press, 2009.

2. **SEDGEWICK, R.; WAYNE, K.** _Algorithms_. 4. ed. Boston: Addison-Wesley, 2011. 

3. **MOZILLA DEVELOPER NETWORK (MDN).** _Documentação Oficial_. Disponível em: [https://developer.mozilla.org/](https://developer.mozilla.org/). Acesso em: 14 mar. 2025. 