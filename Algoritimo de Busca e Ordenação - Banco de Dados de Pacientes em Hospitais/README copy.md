# Sistema de Gerenciamento de Pacientes

## Contexto

Este projeto simula um sistema computacional para gerenciar pacientes em um ambiente hospitalar de emergência. O sistema realiza:

* Cadastro de pacientes com níveis diferentes de prioridade médica.
* Ordenação automática da fila de atendimento com base na gravidade e no horário de chegada.
* Atendimentos justos, guiados por critérios clínicos.
* Buscas otimizadas por prioridade ou data de admissão utilizando **algoritmo de busca binária**.

---

## Estrutura de Classes

### Classe `Paciente`

A classe `Paciente` define a estrutura e os comportamentos essenciais de um paciente no sistema. Seus atributos incluem informações pessoais, prioridade médica, data de admissão e ID do médico responsável.

```python
import datetime

class Paciente:

    def __init__(self, nome_completo, prioridade_medica, id_paciente, data_admissao=None, id_medico_atribuido=None):
        self.id_paciente = id_paciente
        self.nome_completo = nome_completo

        if not 1 <= prioridade_medica <= 5:
            raise ValueError("Prioridade médica deve estar entre 1 e 5.")
        self.prioridade_medica = prioridade_medica

        self.data_admissao = data_admissao if data_admissao else datetime.datetime.now()
        self.id_medico_atribuido = id_medico_atribuido

    def atribuir_medico(self, id_medico):
        self.id_medico_atribuido = id_medico

    def __str__(self):
        medico_info = f"ID Médico: {self.id_medico_atribuido}" if self.id_medico_atribuido else "Médico: N/A"
        return (f"Paciente: {self.nome_completo}, ID: {self.id_paciente}, Prioridade: {self.prioridade_medica}, "
                f"Admissão: {self.data_admissao.strftime('%d/%m/%Y %H:%M:%S')}, {medico_info}")

    def __repr__(self):
        return (f"Paciente(ID: {self.id_paciente}, Nome: {self.nome_completo}, "
                f"Prioridade: {self.prioridade_medica}, "
                f"Admissão: {self.data_admissao.strftime('%Y-%m-%d %H:%M')})")
````

### Classe `Medico`

Representa os profissionais da saúde vinculados a pacientes.

```python
class Medico:

    def __init__(self, nome_completo, especialidade, id_medico):
        self.id_medico: str = id_medico
        self.nome_completo: str = nome_completo
        self.especialidade: str = especialidade

    def __str__(self):
        return (f"Médico: {self.nome_completo}, ID: {self.id_medico}, Especialidade: {self.especialidade}")

    def __repr__(self):
        return (f"Medico(ID: {self.id_medico}, Nome: {self.nome_completo}, "
                f"Especialidade: {self.especialidade})")
```

---

## Ordenação e Busca

### Algoritmo de Ordenação: Insertion Sort Adaptado

O sistema utiliza uma versão adaptada do **Insertion Sort** para ordenar a lista de pacientes com base em dois critérios:

1. **Prioridade médica** — onde o nível 1 é o mais urgente.
2. **Data de admissão** — em caso de empate na prioridade, quem chegou primeiro é atendido primeiro.

**Por que usar Insertion Sort?**

* É um algoritmo simples, fácil de implementar e entender.
* Ideal para listas pequenas ou quase ordenadas.
* Facilita a customização para múltiplos critérios, como neste caso.

```python
def ordenar_pacientes(pacientes):
    for i in range(1, len(pacientes)):
        atual = pacientes[i]
        j = i - 1
        # Ordena por prioridade e desempata por data de admissão
        while j >= 0 and (
            (pacientes[j].prioridade_medica > atual.prioridade_medica) or
            (pacientes[j].prioridade_medica == atual.prioridade_medica and pacientes[j].data_admissao > atual.data_admissao)
        ):
            pacientes[j + 1] = pacientes[j]
            j -= 1
        pacientes[j + 1] = atual
```

**Exemplo prático:**

Se temos três pacientes:

| Nome  | Prioridade | Data de admissão |
| ----- | ---------- | ---------------- |
| João  | 2          | 10:00            |
| Maria | 1          | 10:05            |
| Pedro | 2          | 09:55            |

A ordenação correta será:

1. Maria (prioridade 1)
2. Pedro (prioridade 2, chegou antes)
3. João (prioridade 2, chegou depois)

---

### Algoritmo de Busca: Busca Binária

Para acelerar a localização de pacientes em listas ordenadas, o sistema usa o algoritmo de **busca binária**. Ele permite encontrar rapidamente todos os pacientes que possuem uma prioridade médica específica, aproveitando o fato de a lista já estar ordenada por prioridade.

```python
def buscar_pacientes_binaria(pacientes, prioridade):
    resultado = []
    esquerda, direita = 0, len(pacientes) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if pacientes[meio].prioridade_medica == prioridade:
            # Expande para ambos os lados para capturar todos os pacientes da mesma prioridade
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

**Vantagens da busca binária:**

* Reduz o número de comparações, operando em tempo O(log n) em listas ordenadas.
* É muito mais eficiente do que a busca linear, especialmente em listas grandes.

---

## Aplicação Prática: Sistemas Hospitalares

* **Ordenação**: permite organizar os pacientes por nome, data de admissão, prioridade médica ou ordem cronológica de chegada.
* **Busca**: possibilita localizar rapidamente pacientes por nome, CPF, ID ou condição médica.
* **Sinergia**: em triagens de emergência, a combinação de ordenação por gravidade e busca eficiente permite que o atendimento seja justo, rápido e baseado em critérios clínicos.

---

### Participantes do Projeto

| Nome Completo                      | RGM      | GitHub                                               |
| ---------------------------------- | -------- | ---------------------------------------------------- |
| Marcos Henrique Gomes Pereira      | 39316084 | [@Socram](https://github.com/vedSocram)              |
| Paulo Henrique de Melo Loiola      | 37873822 | [@\_loiolapaulo](https://github.com/loiolapaulo)     |
| Rodrigo Damasceno Santos           | 39188949 | [@RodrigoHD79](https://github.com/RodrigoHD79)       |
| Pedro Henrique Sipriano Cavalcante | 39439526 | [@pedrohsipriano](https://github.com/pedrohsipriano) |
| Filipe Pedais Carvalho             | 38823136 | [@FilipePedais](https://github.com/FilipePedais)     |