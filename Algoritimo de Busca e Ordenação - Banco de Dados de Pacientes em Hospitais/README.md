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
```

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

### Ordenação

A lista de pacientes é ordenada considerando:

1. **Prioridade médica** (nível 1 é o mais urgente).
2. **Data de admissão** (quem chegou primeiro é atendido primeiro em caso de empate).

```python
pacientes = [
    Paciente("Paulo Henrique", 2, 1, data_admissao=datetime.datetime(2023, 10, 20, 10, 0, 0)),
    Paciente("Rodrigo Damasceno", 1, 2, data_admissao=datetime.datetime(2023, 10, 20, 10, 5, 0)),
    Paciente("Filipe Pedais", 2, 3, data_admissao=datetime.datetime(2023, 10, 20, 9, 30, 0))
]

ordenar_pacientes(pacientes)
```

Resultado:

1. Rodrigo Damasceno (prioridade 1)
2. Filipe Pedais (prioridade 2, chegou antes)
3. Paulo Henrique (prioridade 2, chegou depois)

### Busca Binária

Busca rápida por pacientes com base na prioridade médica:

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

## Algoritmo de Ordenação Usado: Insertion Sort

O sistema utiliza uma versão adaptada do Insertion Sort para considerar múltiplos critérios de ordenação:

```python
def ordenar_pacientes(pacientes):
    for i in range(1, len(pacientes)):
        atual = pacientes[i]
        j = i - 1
        while j >= 0 and (
            (atual.prioridade_medica < pacientes[j].prioridade_medica) or
            (atual.prioridade_medica == pacientes[j].prioridade_medica and atual.data_admissao < pacientes[j].data_admissao)
        ):
            pacientes[j + 1] = pacientes[j]
            j -= 1
        pacientes[j + 1] = atual
```

---

## Aplicação Prática: Sistemas Hospitalares

### Ordenação

* Por nome, data de admissão, prioridade médica ou cronologia de atendimento.

### Busca

* Por nome, CPF, ID, ou condição médica.

### Sinergia

* Em triagens de emergência, pacientes são ordenados por gravidade.
* A busca binária permite localizar rapidamente um paciente.
* O histórico do paciente pode ser acessado de forma organizada e rápida.

---

### Participantes do Projeto

| Nome Completo                       | RGM      | GitHub                                               |
| ----------------------------------- | ---------| ---------------------------------------------------- |
| Marcos Henrique Gomes Pereira       | 39316084 | [@Socram](https://github.com/vedSocram)              |
| Paulo Roberto Ferreira Brito        | 39163482 | [@_loiolapaulo](https://github.com/loiolapaulo)      |
| Rodrigo Damasceno Santos            | 39188949 | [@RodrigoHD79](https://github.com/RodrigoHD79)       |
| Pedro Henrique Sipriano Cavalcante  | 39439526 | [@pedrohsipriano](https://github.com/pedrohsipriano) |
| Filipe Pedais Carvalho              | 38823136 | [@FilipePedais](https://github.com/FilipePedais)     |

