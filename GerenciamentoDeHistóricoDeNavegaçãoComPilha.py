# Explicação:

# Pilha de histórico (self.historico): Aqui são armazenadas as páginas visitadas. Cada vez que você visita uma nova página, ela é adicionada ao final da pilha.
# Pilha de avançar (self.avancar): Quando você clica no botão "voltar", 
# a página atual é movida para a pilha de avançar, o que permite "avançar" de volta para a página depois.
# O código contém três principais métodos:

# visitar_pagina(pagina): Adiciona uma nova página ao histórico e limpa a pilha de avançar (pois o histórico foi alterado).
# voltar(): Remove a página atual do histórico e a move para a pilha de avançar, permitindo que você volte para a página anterior.
# avancar_pagina(): Permite que você volte a uma página que foi "desfeita" pela ação de voltar, movendo uma página da pilha de avançar de volta para o histórico.
# O código é uma implementação simples que usa pilhas para simular esse comportamento de navegação de páginas, 
# onde você pode voltar e avançar para páginas com a ajuda da pilha de histórico e da pilha de avançar.


class Navegador:
    def __init__(self):
        self.historico = []  # Pilha de histórico, onde as páginas visitadas são armazenadas.
        self.avancar = []  # Pilha para armazenar as páginas que foram "voltadas" e podem ser avançadas.

    def visitar_pagina(self, pagina):
        self.historico.append(pagina)  # Adiciona a página à pilha de histórico.
        self.avancar.clear()  # Ao visitar uma nova página, limpa a pilha de avançar, pois não há mais páginas para avançar.
        print(f"Visitando: {pagina}")

    def voltar(self):
        if len(self.historico) > 1:  # Verifica se há mais de uma página no histórico para voltar.
            pagina_atual = self.historico.pop()  # Remove a página atual do histórico.
            self.avancar.append(pagina_atual)  # Adiciona a página removida à pilha de avançar.
            print(f"Voltando para: {self.historico[-1]}")  # Mostra qual página você está voltando.
        else:
            print("Não há páginas anteriores!")  # Caso não haja páginas anteriores, exibe uma mensagem.

    def avancar_pagina(self):
        if self.avancar:  # Verifica se há páginas para avançar na pilha de avançar.
            pagina = self.avancar.pop()  # Remove a página da pilha de avançar.
            self.historico.append(pagina)  # Adiciona a página de volta ao histórico.
            print(f"Avançando para: {pagina}")  # Mostra para qual página você está avançando.
        else:
            print("Não há páginas para avançar!")  # Caso não haja páginas para avançar, exibe uma mensagem.

# Exemplo de uso:
navegador = Navegador()
navegador.visitar_pagina("Google")  # Visita a página do Google.
navegador.visitar_pagina("YouTube")  # Visita a página do YouTube.
navegador.visitar_pagina("GitHub")  # Visita a página do GitHub.

navegador.voltar()  # Volta para a página do YouTube.
navegador.voltar()  # Volta para a página do Google.
navegador.avancar_pagina()  # Avança para a página do YouTube novamente.
