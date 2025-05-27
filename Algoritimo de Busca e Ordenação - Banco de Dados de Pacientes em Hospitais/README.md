# Sistema de Gerenciamento de Pacientes

## Contexto

Este projeto simula um sistema de gerenciamento de pacientes em um ambiente de emergência médica. Ele é capaz de:

- Cadastrar pacientes com prioridade médica.
- Ordenar os pacientes com base na urgência e no tempo de chegada.
- Atender pacientes de forma justa e baseada em regras médicas predefinidas.
- Buscar pacientes por prioridade e/ou data de admissão usando busca binária eficiente.

---

## Classes Presentes e Onde São Usadas

### `Paciente`

A Classe `Pacriente` representa cada indivíduo na fila de atendimento. A classe encapsula os dados de cada paciente, sendo utilizada em toda a lógica do sistema.

```python
class Paciente:

    def __init__(self, nome_completo, prioridade_medica, id_paciente, data_admissao=None, id_medico_atribuido=None):
        self.id_paciente = id_paciente
        self.nome_completo = nome_completo

        if not 1 <= prioridade_medica <= 5:
            raise ValueError("Prioridade médica deve estar entre 1 e 5.")
        self.prioridade_medica = prioridade_medica

        self.data_admissao = data_admissao if data_admissao else datetime.datetime.now()
        self.id_medico_atribuido = id_medico_atribuido

    # Atribui um ID de médico a este paciente.
    def atribuir_medico(self, id_medico):
        self.id_medico_atribuido = id_medico

    # Visualização dos dados completos do paciente.
    def __str__(self):
        medico_info = f"ID Médico: {self.id_medico_atribuido}" if self.id_medico_atribuido else "Médico: N/A"
        return (f"Paciente: {self.nome_completo}, ID: {self.id_paciente}, Prioridade: {self.prioridade_medica}, "
                f"Admissão: {self.data_admissao.strftime('%d/%m/%Y %H:%M:%S')}, {medico_info}")

    def __repr__(self):
        return (f"Paciente(ID: {self.id_paciente}, Nome: {self.nome_completo}, "
                f"Prioridade: {self.prioridade_medica}, "
                f"Admissão: {self.data_admissao.strftime('%Y-%m-%d %H:%M')})")
````

Ela é utilizada para criar a lista de pacientes, ordenar, exibir e realizar a busca binária.


### `Medico`

/TODO

---

## Ordenação e Busca: Como e Por Que São Utilizadas

### Ordenação

A lista de pacientes é ordenada considerando dois critérios principais:

1. **Prioridade médica:** Quanto menor o número, maior a urgência.
2. **Data de admissão:** Em caso de empate na prioridade, quem chegou antes é atendido primeiro.

Exemplo de criação e ordenação da lista:

```python
pacientes = [
    Paciente("Paulo Henrique", 2, 1, data_admissao=datetime.datetime(2023, 10, 20, 10, 0, 0)),
    Paciente("Rodrigo Damasceno", 1, 2, data_admissao=datetime.datetime(2023, 10, 20, 10, 5, 0)),
    Paciente("Filipe Pedais", 2, 3, data_admissao=datetime.datetime(2023, 10, 20, 9, 30, 0))
]

ordenar_pacientes(pacientes)
```

Após a ordenação, a lista será:

1. Rodrigo Damasceno (prioridade 1)
2. Filipe Pedais (prioridade 2, chegou antes)
3. Paulo Henrique (prioridade 2, chegou depois)

### Busca Binária

A busca é feita com base na prioridade (e opcionalmente na data). Como a lista já está ordenada, isso permite uma **busca binária eficiente**:

```python
pacientes_encontrados = buscar_pacientes_binaria(pacientes, prioridade=2)
```

Isso retornará todos os pacientes com prioridade 2.

---

## Explicação: Como o Insertion Sort Foi Utilizado e Adaptado

O algoritmo de ordenação utilizado é o **Insertion Sort**, adaptado para comparar dois critérios:

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
