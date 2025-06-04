# Sistema de Gerenciamento de Pacientes

## Introdução

Este projeto simula um sistema computacional para gerenciar pacientes em um ambiente hospitalar de emergência. O sistema realiza:

* Cadastro de pacientes com níveis diferentes de prioridade médica.
* Ordenação automática da fila de atendimento com base na gravidade e no horário de chegada.
* Atendimentos justos, guiados por critérios clínicos.
* Buscas otimizadas por prioridade ou data de admissão utilizando **algoritmo de busca binária**.

---

### Lógica de Atendimento Simulado

O sistema simula o comportamento de um hospital de emergência, onde:

- Pacientes graves são atendidos primeiro, respeitando níveis de prioridade médica.
- Médicos são atribuídos dinamicamente aos pacientes conforme disponibilidade e necessidade.
- A combinação de busca e ordenação otimizam o tempo de resposta, principalmente quando há muitos pacientes na fila, garantindo eficiência e justiça no atendimento.

---

## Estrutura de Classes e Gerenciadores

### Classe `Paciente`

Representa um paciente no sistema, contendo dados essenciais como:

- `id_paciente`: Identificador único do paciente.
- `nome_completo`: Nome completo do paciente.
- `prioridade_medica`: Um valor inteiro de 1 a 5 que indica a gravidade (1 = mais urgente).
- `data_admissao`: Momento em que o paciente foi registrado/admitido.
- `id_medico_atribuido`: Referência ao médico responsável pelo atendimento (pode ser `None` até ser atribuído).

```python
class Paciente:
    def __init__(self, nome_completo, prioridade_medica, id_paciente, data_admissao=None, id_medico_atribuido=None):
        # validação e atribuição de atributos
        ...
    def atribuir_medico(self, id_medico):
        # atribui um médico responsável
        ...
````

Essa classe permite controlar o estado do paciente e registrar o médico que o atende.

---

### Classe `Medico`

Define os profissionais médicos cadastrados no sistema, com os seguintes atributos:

* `id_medico`: Identificador único do médico.
* `nome_completo`: Nome completo do médico.
* `especialidade`: Área médica do profissional (ex: cardiologia, clínica geral).

```python
class Medico:
    def __init__(self, nome_completo, especialidade, id_medico):
        # definição de atributos
        ...
```

Serve para manter o cadastro e facilitar a atribuição de médicos aos pacientes.

---

### Classe `Gerenciador_Pacientes`

Esta classe é responsável por:

* Armazenar a lista de pacientes.
* Realizar operações de cadastro, remoção e busca de pacientes.
* Ordenar a lista com base na prioridade médica e data de admissão.
* Gerenciar atribuições de médicos aos pacientes.

Exemplo simplificado:

```python
class Gerenciador_Pacientes:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)
        self.ordenar_pacientes()

    def ordenar_pacientes(self):
        # Implementação do insertion sort baseado em prioridade e data
        ...

    def buscar_por_prioridade(self, prioridade):
        # Busca binária para localizar pacientes com prioridade específica
        ...

    def atribuir_medico(self, id_paciente, id_medico):
        # Atribui médico a paciente pelo ID
        ...
```

Essa classe abstrai a lógica de manipulação dos pacientes, garantindo a integridade da lista e eficiência nas operações.

---

### Classe `Gerenciador_Medicos`

Semelhante ao gerenciador de pacientes, mantém e manipula a lista de médicos:

* Cadastro e remoção de médicos.
* Busca por ID ou especialidade.
* Facilita a atribuição rápida em casos de emergência.

Exemplo:

```python
class GerenciadorMedicos:
    def __init__(self):
        self.medicos = []

    def adicionar_medico(self, medico):
        self.medicos.append(medico)

    def buscar_por_id(self, id_medico):
        # Busca linear para localizar médico pelo ID
        ...
```

---

## Ordenação e Busca

### Algoritmo de Ordenação: Insertion Sort Adaptado

O sistema utiliza uma versão adaptada do **Insertion Sort** para ordenar a lista de pacientes com base em dois critérios:

1. **Prioridade médica** — onde o nível 1 é o mais urgente.
2. **Data de admissão** — em caso de empate na prioridade, quem chegou primeiro é atendido primeiro.

```python
def ordenar_pacientes(pacientes):
    for i in range(1, len(pacientes)):
        atual = pacientes[i]
        j = i - 1
        while j >= 0 and (
            (pacientes[j].prioridade_medica > atual.prioridade_medica) or
            (pacientes[j].prioridade_medica == atual.prioridade_medica and pacientes[j].data_admissao > atual.data_admissao)
        ):
            pacientes[j + 1] = pacientes[j]
            j -= 1
        pacientes[j + 1] = atual
```

### Algoritmo de Busca: Busca Binária

Para acelerar a localização de pacientes em listas ordenadas, o sistema usa o algoritmo de **busca binária**.

```python
def buscar_pacientes_binaria(pacientes, prioridade):
    resultado = []
    esquerda, direita = 0, len(pacientes) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if pacientes[meio].prioridade_medica == prioridade:
            i = meio
            while i >= 0 and pacientes[i].prioridade_medica == prioridade:
                resultado.insert(0, pacientes[i])
                i -= 1
            i = meio + 1
            while i < len(pacientes) and pacientes[i].prioridade_medica == prioridade:
                resultado.append(pacientes[i])
                i += 1
            break
        elif pacientes[meio].prioridade_medica < prioridade:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return resultado
```

---

## Aplicação Prática: Sistemas Hospitalares

* **Ordenação**: organiza pacientes para atendimento correto conforme urgência e tempo de espera.
* **Busca**: encontra rapidamente pacientes com características específicas.
* **Gerenciamento**: associa médicos a pacientes, facilitando o fluxo do atendimento.

---

### Participantes do Projeto

| Nome Completo                      | RGM      | GitHub                                               |
| ---------------------------------- | -------- | ---------------------------------------------------- |
| Marcos Henrique Gomes Pereira      | 39316084 | [@Socram](https://github.com/vedSocram)              |
| Paulo Henrique de Melo Loiola      | 37873822 | [@\_loiolapaulo](https://github.com/loiolapaulo)     |
| Rodrigo Damasceno Santos           | 39188949 | [@RodrigoHD79](https://github.com/RodrigoHD79)       |
| Pedro Henrique Sipriano Cavalcante | 39439526 | [@pedrohsipriano](https://github.com/pedrohsipriano) |
| Filipe Pedais Carvalho             | 38823136 | [@FilipePedais](https://github.com/FilipePedais)     |
